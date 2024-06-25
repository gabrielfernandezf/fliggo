import pandas as pd
import numpy as np

class FeatureEngineering:
    def __init__(self, dataframe):
        self.df = dataframe

    def create_total_nights(self):
        self.df['total_nights'] = self.df['stays_in_week_nights'] + self.df['stays_in_weekend_nights']
        return self.df

    def create_is_weekend_stay(self):
        self.df['stays_in_weekend_nights'] = pd.to_numeric(self.df['stays_in_weekend_nights'], errors='coerce')
        self.df['is_weekend_stay'] = np.where(self.df['stays_in_weekend_nights'] > 0, 1, 0)
        return self.df

    def apply_all(self):
        self.create_total_nights()
        self.create_is_weekend_stay()
        return self.df
