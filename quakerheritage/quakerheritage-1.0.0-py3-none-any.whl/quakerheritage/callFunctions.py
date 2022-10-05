# quakerheritage/build.py

"""Unifies the functional modules and runs the main code to create a formatted Pandas DataFrame from pdfs held by Britain Yearly Meeting.

This module runs automatically when opened, in concert with the other modules in this package. 

This module contains the following functions:

- `getOnlineData(url)` - Collects pdfs from webpage, extracts text to dictionary, creates DataFrame from all dicitonaries and hygienes data.

"""

import tkinter as tk
from tkinter import filedialog

import pandas as pd

import getWebData as gwd
import cleanseData as cd

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
    for pdf in pdfList: 
        dictList.append(gwd.pdfDataExtract(pdf))
    df = cd.createDataFrame(dictList)
    df = cd.hygieneDataFrame(df)
    return df
    

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory() + '\quakerHeritageDB.csv'
    db = getOnlineData(url)
    cd.saveToCSV(db, file_path)