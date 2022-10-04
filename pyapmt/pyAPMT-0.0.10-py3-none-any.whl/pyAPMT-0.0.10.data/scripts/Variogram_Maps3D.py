
# -*- coding: utf-8 -*-
"""

Module dedicated to 3D variogram maps

"""

# Author: Sebastian Avalos <sebastian.avalos@apmodtech.com>
#         Advanced Predictive Modeling Technology
#         www.apmodtech.com/pyAPMT/
#         September-2022
#
# License: MIT License


# All submodules and packages
import numpy as np
import pandas as pd
import subprocess
import matplotlib.pyplot as plt
import os
import ot
import seaborn as sns
sns.set(font_scale=1)
sns.set_style("whitegrid")


import logging
logging.getLogger().setLevel(logging.CRITICAL)

CREATE_NO_WINDOW = 0x08000000

def ComputeVariogramMaps3D(DH_DB, Variable, NLags='Auto', DLags='Auto', Title='Title',
                           MinPairs=4, Trim=[-99999,99999], Sted=True, 
                           OutputImage=None, Dom=None, PlotBool=True, SubDom=None):
    
    Standardized = 1 if Sted == True else 0
    

    varstr = '''              Parameters for VARMAP
                  *********************
                  
START OF PARAMETERS:
tempData.txt                   -file with data
1   4                          -   number of variables: column numbers
{Trim[0]}   {Trim[1]}               -   trimming limits
0                            -1=regular grid, 0=scattered values
 500    500    100               -if =1: nx,     ny,   nz
1.0  1.0  1.0                -       xsiz, ysiz, zsiz
1   2   3                    -if =0: columns for x,y, z coordinates
temp_varmap.out                   -file for variogram output
 {NLags[0]}   {NLags[1]}    {NLags[2]}               -nxlag, nylag, nzlag
{DLags[0]}   {DLags[1]}    {DLags[2]}              -dxlag, dylag, dzlag
{MinPairs}                            -minimum number of pairs
{Standardized}                            -standardize sill? (0=no, 1=yes)
1                            -number of variograms
1   1   1                    -tail, head, variogram type


type 1 = traditional semivariogram
     2 = traditional cross semivariogram
     3 = covariance
     4 = correlogram
     5 = general relative semivariogram
     6 = pairwise relative semivariogram
     7 = semivariogram of logarithms
     8 = semimadogram
     9 = indicator semivariogram - continuous
     10= indicator semivariogram - categorical
'''
    
    
    if Dom == None:
        tempDataSet = DH_DB.DB[[DH_DB.East, DH_DB.North, DH_DB.Elevation, Variable]].to_numpy()
    else:
        SubSet1 = DH_DB.DB[DH_DB.DB[Dom] == SubDom]
        tempDataSet = SubSet1[[DH_DB.East, DH_DB.North, DH_DB.Elevation, Variable]].to_numpy()

    
    np.savetxt("tempData.txt", X=tempDataSet, fmt='%.5f', delimiter='\t', newline='\n', 
               header='DataGSLib\n4\nEast\nNorth\nElevation\nAttribute', comments='')
    
    
    if NLags == 'Auto':
        NLags = [15,15,15]
    if DLags == 'Auto':
        Coord = tempDataSet[:,:3]
        if Coord.shape[0] > 2000:
            Coord = Coord[np.random.choice(Coord.shape[0], 2000, replace=False), :]
        Dist_Mat = ot.dist(Coord, Coord, metric='euclidean')
        p50 = np.percentile(Dist_Mat, 50)        
        tDl = int(p50/15)
        DLags = [tDl, tDl, tDl]
    
    
    
    DictArg = {"Trim" : Trim,
      "NLags" : NLags,
      "DLags" : DLags,
      "MinPairs" : MinPairs,
      "Standardized" : Standardized
    }
    
    
    
    
    
    Temp = varstr.format(**DictArg)
    
    text_file = open("varmap.par", "w")
    n = text_file.write(Temp)
    text_file.close()
    
    
    
    subprocess.call("varmap.exe varmap.par", creationflags=CREATE_NO_WINDOW)
    os.remove("varmap.par")
    os.remove("tempData.txt")
    
    
    Output = pd.read_csv("temp_varmap.out", skiprows=8, delimiter="\s+", names=["V1", "V2", "V3", "V4", "V5", "V6"])
    os.remove("temp_varmap.out")
    Output = Output.to_numpy()
    VarValues = Output[:,0]
    Var3D_vals = np.zeros((2*NLags[0]+1, 2*NLags[1]+1, 2*NLags[2]+1))
    
    pos = 0
    for i_z in range(2*NLags[2]+1):
        for i_y in range(2*NLags[1]+1):
            for i_x in range(2*NLags[0]+1):
                Var3D_vals[i_x, i_y, i_z] = VarValues[pos]
                pos += 1
    # #######################    
    Var3D_vals[Var3D_vals == -999] = np.NaN

    # #######################
    fig = plt.figure(figsize=(16,4))
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.4   # the amount of width reserved for blank space between subplots
    hspace = 0.3   # the amount of height reserved for white space between subplots
    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
    
    # #######################
    ax1 = plt.subplot(131)
    MapVal = Var3D_vals[:,:,NLags[2]]
    c = ax1.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', extent=[-NLags[0]*DLags[0],NLags[0]*DLags[0],-NLags[1]*DLags[1],NLags[1]*DLags[1]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax1.set_xlabel("East")
    ax1.set_ylabel("North")
    ax1.grid(False)
    ax1.set_title(Title+" - XY plane")
    ax1.set_aspect((NLags[0]*DLags[0])/(NLags[1]*DLags[1]))
    # #######################
    ax2 = plt.subplot(132)
    MapVal = Var3D_vals[:,NLags[1], :]
    c = ax2.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', extent=[-NLags[0]*DLags[0],NLags[0]*DLags[0],-NLags[2]*DLags[2],NLags[2]*DLags[2]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax2.set_xlabel("East")
    ax2.set_ylabel("Elevation")
    ax2.grid(False)
    ax2.set_title(Title+" - XZ plane")
    ax2.set_aspect((NLags[0]*DLags[0])/(NLags[2]*DLags[2]))
    #ax2.set_aspect('equal', 'datalim')
    # #######################
    ax3 = plt.subplot(133)
    MapVal = Var3D_vals[NLags[0],:, :]
    c = ax3.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', extent=[-NLags[1]*DLags[1],NLags[1]*DLags[1],-NLags[2]*DLags[2],NLags[2]*DLags[2]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax3.set_xlabel("North")
    ax3.set_ylabel("Elevation")
    ax3.grid(False)
    ax3.set_title(Title+" - YZ plane")
    ax3.set_aspect((NLags[1]*DLags[1])/(NLags[2]*DLags[2]))
    # #######################
    if PlotBool == True:
        plt.show()
    # #######################
    if OutputImage != None:
        fig.savefig(OutputImage, dpi=300, bbox_inches='tight')
    # #######################
    return plt.close()