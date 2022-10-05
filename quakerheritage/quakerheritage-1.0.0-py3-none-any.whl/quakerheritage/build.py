# quakerheritage/build.py

"""Unifies the functional modules and runs the main code to create a formatted Pandas DataFrame from pdfs held by Britain Yearly Meeting.

This module runs automatically when opened, in concert with the other modules in this package. Please note, the import structure of the local files is designed only to work in CLI. 
You will receive a ModuleNotFoundError if you attempt to run this code in IDE. Replace lines 19 and 20 with the following to work locally in IDE:
    import get_web_data as gwd
    import cleanse_data as cd

This module contains the following functions:

- `get_online_data(url)` - Collects pdfs from webpage, extracts text to dictionary, creates DataFrame from all dicitonaries and hygienes data.
- `main()` - executes automatically to run the entire project
"""

import tkinter as tk
from tkinter import filedialog

import pandas as pd

import get_web_data as gwd
import cleanse_data as cd

url = "https://heritage.quaker.org.uk/"

def get_online_data(url: str) -> pd.DataFrame: 
    """Collect online data and merge it into a Pandas DataFrame
    
    Args:
        url (string): A fixed URL for the Quaker Meeting House Heritage Project's pdf storage.
        
    Returns:
        df (Pandas DataFrame): A transformed and hygiened DataFrame.
    """
    pdf_list = gwd.get_urls(url)
    dict_list = []
    for pdf in pdf_list[1:]: 
        dict_list.append(gwd.pdf_data_extract(pdf))
    df = cd.create_dataframe(dict_list)
    df = cd.bulk_hygiene_dataframe(df)
    return df

def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory() + '\quakerHeritageDB.csv'
    db = get_online_data(url)
    cd.save_to_csv(db, file_path)

if __name__ == '__main__':
    main()
    