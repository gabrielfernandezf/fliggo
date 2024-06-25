import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

class DataCleaningAndTransformation:
    def __init__(self, dataframe):
        self.df = dataframe
        self.label_encoders = {}

    def transform_children(self):
        self.df['children'] = self.df['children'].replace({'none': 0, 'children': 1}).astype(int)
        return self.df

    def move_children_column(self):
        cols = list(self.df.columns)
        cols.insert(1, cols.pop(cols.index('children')))
        self.df = self.df[cols]
        return self.df

    def transform_arrival_date(self):
        self.df['arrival_month'] = pd.to_datetime(self.df['arrival_date']).dt.month
        self.df.drop(columns=['arrival_date'], inplace=True)
        return self.df

    def transform_parking_spaces(self):
        self.df['required_car_parking_spaces'] = self.df['required_car_parking_spaces'].replace({'none': 0, 'parking': 1}).astype(int)
        return self.df

    def handle_missing_country(self):
        self.df = self.df.dropna(subset=['country'])
        return self.df

    def apply_label_encoding(self):
        categorical_columns = ['hotel', 'meal', 'country', 'market_segment', 'distribution_channel',
                               'reserved_room_type', 'assigned_room_type', 'deposit_type', 'customer_type']
        for col in categorical_columns:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col])
            self.label_encoders[col] = le
        return self.df

    def apply_all_transformations(self):
        self.transform_children()
        self.move_children_column()
        self.transform_arrival_date()
        self.transform_parking_spaces()
        self.handle_missing_country()
        self.apply_label_encoding()
        return self.df
