# quakerheritage/cleanseData.py

"""Runs Pandas functionality to merge text data into workable DataFrame and creates consistent data quality.

This module allows the user to take the raw data from the Quaker Heritage Project's pdfs and enhances usefulness of data points and types.

This module contains the following functions:

- `createDataframe(url)` - Takes a list of dictionaries with varied values and keys and unifies them into a single Pandas DataFrame.
- `hygieneDataFrame(df)` - Takes the varied data in the DataFrame and applies a regular schema to it for data quality purposes.
"""

import pandas as pd
import numpy as np

# collate all data
def createDataFrame(dictList: list) -> pd.DataFrame:
    """Concatenates dictionary values and transforms them into a Pandas DataFrame.

    Args:
        dictList (array): A list object of dictionaries created from pdfs.

    Return:
        df (Pandas DataFrame): A raw and unhygiened Pandas DataFrame.
    """
    data = []
    data.append([i for i in dictList[0].keys()])
    for dct in dictList:
        data.append([i for i in dct.values()])
    df = pd.DataFrame(data, columns = data[0])
    df = df.rename(columns=df.iloc[0]).drop(df.index[0]).reset_index(drop=True)
    return df

def hygieneDataFrame(df: pd.DataFrame) -> pd.DataFrame:
    """Data quality function that iterates through selected columns within the DataFrame and corrects variant values.

    Example:
        'Date of Visit': 
            Old Value: 5th July 2015
            Hygiened Value: 2015-07-05
        'Date':
            Old Value: c1864-70, 1965; 2005
            Hygiened Value: 1864

    Args:
        df (Pandas DataFrame): A raw and unhygiened DataFrame.

    Return:
        df (Pandas DataFrame): The same DataFrame with all formatting applied for data quality.
    """
    df.rename(columns={'Historic Environment Scotland': 'Historic locality', 'Reference': 'Listing Reference'}, inplace = True)
    try:
        df['Listed status'] = df['Listed status'].apply(lambda x: 'Not listed' if 'No' in x else x)
        df['Listing Reference'] = df['Listing Reference'].apply(lambda x: 'N/A' if ('Not applicable' in x or x.upper() == 'N/A') else x)
        df['Heritage at Risk'] = np.where(df['Listed status'].str.upper() == 'NOT LISTED', 'No', df['Heritage at Risk'])
        df['Date'] = df['Date'].str.extract(r'^(\d{4})', expand=False)
        df['Architect'] = df['Architect'].replace({'Not established': 'Unknown', 'not established': 'Unknown', 'None': 'Unknown',',':';'}, regex = True)
        df['Name of contact made on site'] = df['Name of contact made on site'].replace(' and ', ';')
        df['Date of visit'] = pd.to_datetime(df['Date of visit']).apply(lambda x: x.date())
        df['Associated buildings and sites'] = df['Associated buildings and sites'].apply(lambda x: 'N/A' if ('Not applicable' in x or 'None' in x) else x)
    except:
        pass
    
    return df

def saveToCSV(df: pd.DataFrame, filepath: str) -> None:
    """Small function to save CSV with appropriate format.
    
    Args:
        df (Pandas DataFrame): collection of data for Pandas to convert to CSV.
        filepath (string): desired location for file creation.
    """
    df.to_csv(filepath, encoding='utf-8-sig')
