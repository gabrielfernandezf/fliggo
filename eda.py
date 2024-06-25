import plotly.express as px

class EDA:
    def __init__(self, dataframe):
        self.df = dataframe

    def plot_distribution_by_hotel(self):
        fig = px.histogram(self.df, x='hotel', title='Distribution of Bookings by Hotel Type')
        fig.show()

    def plot_previous_cancellations(self):
        fig = px.histogram(self.df, x='previous_cancellations', title='Distribution of Previous Cancellations')
        fig.show()

    def plot_price_distribution(self):
        fig = px.box(self.df, x='hotel', y='average_daily_rate', title='Price Distribution by Hotel Type')
        fig.show()

    def plot_stays_distribution(self):
        fig = px.box(self.df, x='hotel', y='stays_in_week_nights', title='Weeknight Stays Distribution by Hotel Type')
        fig.show()
        fig = px.box(self.df, x='hotel', y='stays_in_weekend_nights', title='Weekend Stays Distribution by Hotel Type')
        fig.show()

    def plot_children_distribution(self):
        fig = px.histogram(self.df, x='children', title='Distribution of Reservations with Children')
        fig.show()

    def plot_seasonality(self):
        fig = px.histogram(self.df, x='arrival_month', title='Seasonality of Reservations')
        fig.show()

    def plot_market_segment(self):
        fig = px.histogram(self.df, x='market_segment', title='Distribution of Reservations by Market Segment')
        fig.show()

    def plot_total_previous_cancellations_by_customer_type(self):
        total_previous_cancellations = self.df.groupby('customer_type')['previous_cancellations'].sum().reset_index()
        total_previous_cancellations.columns = ['customer_type', 'total_previous_cancellations']
        fig = px.bar(total_previous_cancellations, x='customer_type', y='total_previous_cancellations', title='Total Previous Cancellations by Customer Type')
        fig.show()

    def plot_average_stay_duration(self):
        avg_stay = self.df.groupby('hotel')['total_nights'].mean().reset_index()
        fig = px.bar(avg_stay, x='hotel', y='total_nights', title='Average Stay Duration by Hotel Type')
        fig.show()

    def plot_meal_distribution(self):
        fig = px.histogram(self.df, x='meal', title='Distribution of Meal Types Booked')
        fig.show()

    def apply_all_eda(self):
        self.plot_distribution_by_hotel()
        self.plot_previous_cancellations()
        self.plot_price_distribution()
        self.plot_stays_distribution()
        self.plot_children_distribution()
        self.plot_seasonality()
        self.plot_market_segment()
        self.plot_total_previous_cancellations_by_customer_type()
        self.plot_average_stay_duration()
        self.plot_meal_distribution()
