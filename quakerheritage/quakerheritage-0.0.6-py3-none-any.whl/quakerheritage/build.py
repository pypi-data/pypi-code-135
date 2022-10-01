# quakerheritage/build.py

"""Unifies the functional modules and runs the main code to create a formatted Pandas DataFrame from pdfs held by Britain Yearly Meeting.

This module runs automatically when opened, in concert with the other modules in this package. Please note, the import structure of the local files is designed only to work in CLI. 
You will receive a ModuleNotFoundError if you attempt to run this code in IDE. Replace lines 19 and 20 with the following to work locally in IDE:
    import getWebData as gwd
    import cleanseData as cd

This module contains the following functions:

- `getOnlineData(url)` - Collects pdfs from webpage, extracts text to dictionary, creates DataFrame from all dicitonaries and hygienes data.
- `main()` - executes automatically to run the entire project
"""
print(__package__, __name__)
import tkinter as tk
from tkinter import filedialog

import pandas as pd

from quakerheritage.utils import getWebData as gwd
from quakerheritage.utils import cleanseData as cd

url = "https://heritage.quaker.org.uk/"

def getOnlineData(url: str) -> pd.DataFrame: 
    """Collect online data and merge it into a Pandas DataFrame
    
    Args:
        url (string): A fixed URL for the Quaker Meeting House Heritage Project's pdf storage.
        
    Returns:
        df (Pandas DataFrame): A transformed and hygeined DataFrame.
    """
    pdfList = gwd.getUrls(url)
    dictList = []
    for pdf in pdfList[1:3]: 
        dictList.append(gwd.pdfDataExtract(pdf))
    df = cd.createDataFrame(dictList)
    df = cd.hygieneDataFrame(df)
    return df

def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory() + '\quakerHeritageDB.csv'
    db = getOnlineData(url)
    cd.saveToCSV(db, file_path)

if __name__ == '__main__':
    main()