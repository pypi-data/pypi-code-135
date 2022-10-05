# quakerheritage/cleanse_data.py

"""Runs Pandas functionality to merge text data into workable DataFrame and creates consistent data quality.

This module allows the user to take the raw data from the Quaker Heritage Project's pdfs and enhances usefulness of data points and types.

This module contains the following functions:

- `create_dataframe(url)` - Takes a list of dictionaries with varied values and keys and unifies them into a single Pandas DataFrame.
- `hygiene_dataframe(df)` - Takes the varied data in the DataFrame and applies a regular schema to it for data quality purposes.
"""

import pandas as pd
import numpy as np

# collate all data
def create_dataframe(data_list: list) -> pd.DataFrame:
    """Concatenates dictionary values and transforms them into a Pandas DataFrame.

    Args:
        data_list (list): A list object of dictionaries created from pdfs.

    Return:
        df (Pandas DataFrame): A raw and unhygiened Pandas DataFrame.
    """
    headers = ['Meeting House Name', 'Meeting House Full Name', 'Address', 'National Grid Reference', 'Area Meeting', 'Property Registration Number', 'Owner', 'Local Planning Authority', 'Historic Locality', 'Civil Parish', 'Listed Status', 'Listing Reference', 'Conservation Area', 'Scheduled Ancient Monument', 'Heritage at Risk', 'Date', 'Architect(s)', 'Date of visit', 'Name of report author', 'Name of contact', 'Associated buildings and sites', 'Attached burial ground']
    df = pd.DataFrame(data_list, columns = headers)
    #df = df.rename(columns=df.iloc[0]).drop(df.index[0]).reset_index(drop=True)
    return df

def bulk_hygiene_dataframe(df: pd.DataFrame) -> pd.DataFrame:
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
    try:
        df['Listed Status'] = df['Listed Status'].apply(lambda x: 'Not listed' if 'No' in x else x)
        df['Listing Reference'] = df['Listing Reference'].apply(lambda x: 'N/A' if ('Not applicable' in x or x.upper() == 'N/A') else x)
        df['Heritage at Risk'] = np.where(df['Listed Status'].str.upper() == 'NOT LISTED', 'No', df['Heritage at Risk'])
        df['Date'] = df['Date'].str.extract(r'^(\d{4})', expand=False)
        df['Architect(s)'] = df['Architect(s)'].replace({'Not established': 'Unknown', 'not established': 'Unknown', 'None': 'Unknown',',':';'}, regex = True)
        df['Name of contact'] = df['Name of contact'].replace(' and ', ';')
        df['Associated buildings and sites'] = df['Associated buildings and sites'].apply(lambda x: 'N/A' if ('Not applicable' in x or 'None' in x) else x)
        for row in df['Date of visit']:
            try:
                df['Date of visit'] = pd.to_datetime(df['Date of visit'].replace('rd', '').replace('th',''))
            except:
                df['Date of visit'] = pd.to_datetime(df['Date of visit'].replace('215','2015'))
        for row in df['Meeting House Name']:
            df['Meeting House Name'] = df['Meeting House Name'].replace('Heritage Report AHP Jan 2017', '')

    except:
        pass
    
    return df

def save_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """Small function to save CSV with appropriate format.
    
    Args:
        df (Pandas DataFrame): collection of data for Pandas to convert to CSV.
        file_path (string): desired location for file creation.
    """
    df.to_csv(file_path, encoding='utf-8-sig')
