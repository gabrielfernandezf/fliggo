import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

class FeatureImportanceAnalysis:
    def __init__(self, X_train_balanced, y_train_balanced, X_test, y_test):
        self.X_train_balanced = X_train_balanced
        self.y_train_balanced = y_train_balanced
        self.X_test = X_test
        self.y_test = y_test

    def plot_correlation_matrix(self):
        plt.figure(figsize=(15, 10))
        correlation_matrix = pd.concat([self.X_train_balanced, pd.DataFrame(self.y_train_balanced, columns=[self.y_train_balanced.name])], axis=1).corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Matrix')
        plt.show()

    def get_feature_importances(self):
        model = RandomForestClassifier(random_state=42)
        model.fit(self.X_train_balanced, self.y_train_balanced)
        
        importances = model.feature_importances_
        feature_names = self.X_train_balanced.columns
        feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
        
        return feature_importance_df

    def plot_feature_importances(self, feature_importance_df):
        plt.figure(figsize=(10, 8))
        sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
        plt.title('Feature Importances from Random Forest')
        plt.show()
