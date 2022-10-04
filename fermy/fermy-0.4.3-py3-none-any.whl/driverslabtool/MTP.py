"""
Created the 2022/10/04
v0.1 First version
@author: Nicolas Hardy

This file is part of Fermy.

    Fermy is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Fermy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Fermy.  If not, see <https://www.gnu.org/licenses/>.
"""

__version__ = 0.1

import pandas as pd
from typing import List, Dict, Iterable, Tuple, Union
import math
from . import errorslabtools

class MTPReader():
    """Class that allow to read MTP data need filepath and readername
    """
    
    def __init__(self, filepath:str, readername:str):
        """Initialisation of reader
        """
        self.readername = readername
        self.plate = pd.DataFrame()
        self.filepath = filepath
        self.dicoreader = {"Epoch2" : self.readepochtwo,
                            "fakeMTP" : self.readfakemtp
                            } # linker between MTP and reading function
    
    def convstringtohours(self, string: str) -> float:
        """"Function to transform a string like hours:minutes:seconds
        or aaa-mm-dd hh:mm:ss to a float of hours
        return float
        """
        if len(string.split(" ")) == 1:
            spliting = string.split(':')
            timefloat = float(spliting[0])+float(spliting[1])/60+float(spliting[2])/3600
        else:
            spliting = string.split(" ")
            timefloat = float(spliting[0].split('-')[2])*24
            timefloat = timefloat + float(spliting[1].split(':')[0])
            timefloat = timefloat + float(spliting[1].split(':')[1])/60
            timefloat = timefloat + float(spliting[1].split(':')[2])/3600
        return timefloat
    
    def readepochtwo(self):
        """Function to return formated dataframe from reader Epoch
        """
        
        rawtable = pd.read_excel(self.filepath, sheet_name=0)
        numline = int(rawtable[rawtable["Unnamed: 0"]=="Layout"].index.values) +2
        del rawtable
        tabledata = pd.read_excel(self.filepath, sheet_name=0, usecols="B:CU", index_col=None, skiprows=numline+13, skipfooter=36, dtype={"Time":str})  #data robot
        tabledata["Time"] = tabledata["Time"].apply(self.convstringtohours)  # converrt time from hh:mm:ss to float
        tabledata.drop(["Time", "T° 600"], axis=1, inplace=True, errors = "ignore")  # Drop Time columns
        tabledata = tabledata.applymap(lambda data: data.strip("*") if isinstance(data, str) else data)  # clean *
        tabledata = tabledata.astype('float64')
        tabledata.dropna(axis=0, how="all", subset=tabledata.columns[2:], inplace=True)  # clear empty data
        return tabledata
    
    def readfakemtp(self):
        """Function to return a fake formated dataframe
        """
        # time 5 minutes steps in hours for 6 hours
        time = [time/60 for time in range(0, 60*6, 5)]
        lagtime = time[20]  # 1.66 h
        fakedataset = [0.01]*20+[0.01*math.exp(0.5*(time-lagtime)) for time in time[20:]]
        datadico = {}
        for line in ["A", "B", "C","D", "E", "F", "G", "H"]:
            for column in range(1,13):
                datadico[f"{line}{column}"] = fakedataset
        tabledata = pd.DataFrame(data= datadico, index=time)
        return tabledata
    
    def readMTP(self) -> pd.DataFrame:
        """Load a file and provide a formated DataFrame
        """
        #read the input file if the reader name is known 
        if self.readername in self.dicoreader.keys():
            try:
                self.plate = self.dicoreader[self.readername]()
            except Exception as err:
                raise errorslabtools.MTPError(f"Wrong device '{self.readername}' or corrupted file")
        return self.plate
    
    def readerslist(self) -> List[str]:
        """Provide the names of readers avaible
        """
        listofreaders = list(self.dicoreader.keys())
        return listofreaders

