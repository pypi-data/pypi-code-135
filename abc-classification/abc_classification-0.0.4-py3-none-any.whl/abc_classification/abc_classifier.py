"""Module for ABC classification in business analysis."""
import pandas as pd
import numpy as np


class ABCClassifier:
    """ABC classification class"""

    def __init__(self, data: pd.DataFrame):
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Provided object is not pd.DataFrame')

        self.data = data

    def classify(self, abc_column: str, criterion: str) -> pd.DataFrame:
        """Make ABC classification for values from abc_column.
        Dataframe must be grouped by abc_column.
        Args:
            abc_column (str) - column with values to classify.
            criterion (str) - column with criterion for classification.
        Return:
            abc_df (pd.DataFrame) - classified dataframe."""
        if not isinstance(abc_column, str):
            raise ValueError(f'Column name must be string not {type(abc_column)}')
        if not isinstance(criterion, str):
            raise ValueError(f'Column name must be string not {type(criterion)}')

        abc_df = self.data[[abc_column, criterion]].copy()
        abc_df.sort_values(by=criterion, inplace=True, ascending=False)
        total = self.data[criterion].sum()
        abc_df['percentage'] = abc_df[criterion] / total
        abc_df[f'cumulative_{criterion}'] = abc_df['percentage'].cumsum()
        conditions = [(abc_df[f'cumulative_{criterion}'] <= 0.8),
                      (abc_df[f'cumulative_{criterion}'] <= 0.95),
                      (abc_df[f'cumulative_{criterion}'] > 0.95)]
        values = ['A', 'B', 'C']
        abc_df['class'] = np.select(conditions, values)
        abc_df.drop(['percentage', f'cumulative_{criterion}'], axis=1, inplace=True)
        return abc_df

    def brief_abc(self, abc_df: pd.DataFrame) -> pd.DataFrame:
        """Return aggregated by class dataframe with brief information about class.
        Args:
            abc_df (pd.DataFrame) - DataFrame for brief information calculation."""
        return abc_df.groupby('class').sum()
