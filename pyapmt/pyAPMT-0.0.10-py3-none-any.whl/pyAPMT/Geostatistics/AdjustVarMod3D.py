
# -*- coding: utf-8 -*-
"""

Module for 3D Var map parameters inference

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
from pygeostat.transformations.rotations import azmdip
import warnings
import logging

sns.set(font_scale=1)
sns.set_style("whitegrid")
logging.getLogger().setLevel(logging.CRITICAL)
np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})
CREATE_NO_WINDOW = 0x08000000



class Ellipsoid(object):
    """Class inspired by MicroStructPy
    To support, please visit:
    https://docs.microstructpy.org/en/latest/api/geometry/ellipsoid.html
    
    
    """
    def __init__(self, **kwargs):
        # Position
        if 'center' in kwargs:
            self.center = kwargs['center']

        elif 'position' in kwargs:
            self.center = kwargs['position']

        else:
            self.center = (0, 0, 0)


    def best_fit(self, points):

        pts = np.array(points)
        pts_mean = pts.mean(axis=0)
        trans_pts = pts - pts_mean

        x, y, z = trans_pts.T

        L = np.zeros((len(x), 9), dtype='float')
        L[:, 0] = x * x + y * y - 2 * z * z
        L[:, 1] = x * x - 2 * y * y + z * z
        L[:, 2] = 4 * x * y
        L[:, 3] = 2 * x * z
        L[:, 4] = 2 * y * z
        L[:, 5] = x
        L[:, 6] = y
        L[:, 7] = z
        L[:, 8] = 1

        e = x * x + y * y + z * z

        u, v, m, n, p, q, r, s, t = np.linalg.lstsq(L, e, rcond=None)[0]
        axx = 1 - u - v
        ayy = 1 - u + 2 * v
        azz = 1 + 2 * u - v
        axy = -4 * m
        axz = -2 * n
        ayz = -2 * p
        ax = - q
        ay = - r
        az = - s
        ac = - t

        hom_mat = np.array([[axx, 0.5 * axy, 0.5 * axz, 0.5 * ax],
                            [0.5 * axy, ayy, 0.5 * ayz, 0.5 * ay],
                            [0.5 * axz, 0.5 * ayz, azz, 0.5 * az],
                            [0.5 * ax, 0.5 * ay, 0.5 * az, ac]])

        cen = np.linalg.lstsq(-hom_mat[:3, :3], hom_mat[-1, :3], rcond=None)[0]
        glbl_cen = cen + pts_mean

        T = np.eye(4)
        T[-1, :3] = cen
        R = T.dot(hom_mat.dot(T.T))
        evals, evecs = np.linalg.eigh(- R[:3, :3] / R[-1, -1])
        axes = 1 / np.sqrt(np.abs(evals))
        ori_matrix = evecs
        axes = axes.tolist()        
        return axes, ori_matrix


def Optimize(VarValues, NLags, DLags, Standardized):
    
    Angs = [0,0,0]
    Str1 = [0,0,0]
    
    SubBl = VarValues[NLags[0],NLags[1],NLags[2]]
    
    if SubBl == 0:
        SubBl = 0.2  
    

    
    #SubBl[SubBl == -999] = np.NaN
    Sill1 = np.around(1 - np.nanmean(SubBl), decimals=2)
    
    
    if Sill1 > 1: # Impossing standard variogram
        Sill1 = 1
    #elif Sill1 < 0.8: # Impossing Nugget of at most 0.2
        #Sill1 = 0.8
    
    
    VarValues[VarValues == -999] = 1
    VarValues[VarValues > 1] = 1
    VarValues[VarValues < 1] = 0
    
    
    PadVarValues = np.ones((VarValues.shape[0]+2, VarValues.shape[1]+2, VarValues.shape[2]+2))
    PadVarValues[1:-1, 1:-1, 1:-1] = VarValues
        
    Contour = np.zeros_like(VarValues)
    f_tol_min = 18
    f_tol_max = 24
    
    for ii in range(VarValues.shape[0]):
        for jj in range(VarValues.shape[1]):
            for kk in range(VarValues.shape[2]):
                tFil = PadVarValues[ii-1:ii+2, jj-1:jj+2,kk-1:kk+2]
                tSum = np.sum(tFil)
                if (tSum >= f_tol_min) and (tSum <= f_tol_max):
                    Contour[ii,jj,kk] = 1
                
    tPos = np.where(Contour == 1)
    Positions = np.vstack((tPos[0], tPos[1], tPos[2]))
    Positions = Positions.T
    
    ListPositions = Positions.tolist()
    
    EllipsoidObject = Ellipsoid()
    
    RangesNorm, RotMatrix = EllipsoidObject.best_fit(points=ListPositions)
    
    Str1[0] = np.around(RangesNorm[0]*DLags[0], decimals=0)
    Str1[1] = np.around(RangesNorm[1]*DLags[1], decimals=0)
    Str1[2] = np.around(RangesNorm[2]*DLags[2], decimals=0)
    

    Angs[0] = np.around(azmdip(RotMatrix[:,0])[0], decimals=0)
    Angs[1]  = np.around(azmdip(RotMatrix[:,0])[1], decimals=0)
    Angs[2] =  np.around(np.degrees(np.arccos((RotMatrix[2,2]/np.cos(np.radians(Angs[1]))))), decimals=0)
    
    if Angs[0] > 180:
        Angs[0] = Angs[0] - 180   
        Angs[1] = -Angs[1]
    Nugget = np.around(1-Sill1, decimals=2)
    print("\n--------------------------")
    print("Fitted parameters:")
    print("- Structure 1 -")
    print(f"    Nugget   {Nugget}")
    print(f"    Sill     {Sill1}")
    print("    ang1     ang2     ang3")
    print("{: >8} {: >8} {: >8}".format(*Angs))
    print("    a_hmax,  a_hmin, a_vert")
    print(" {: >8} {: >8} {: >8}".format(*Str1))    
    print("--------------------------")

    return Angs, Str1, Sill1


def FitVariogram(NLags, DLags, Standardized, Angs, Str1, Sill1):

    
    # Auto fitting 3D
    
    
    varmapmodstr = f'''                  Parameters for VARMAP_MOD
                  *********************

START OF PARAMETERS:
varmap_mod.out                   -file for variogram output
 {NLags[0]}   {NLags[1]}    {NLags[2]}               -nxlag, nylag, nzlag
{DLags[0]}   {DLags[1]}    {DLags[2]}              -dxlag, dylag, dzlag
{Standardized}                            -standardize sill? (0=no, 1=yes)
1    {1-Sill1}                     -nst, nugget effect
1    {Sill1}  {Angs[0]}   {Angs[1]}    {Angs[2]}     -it,cc,ang1,ang2,ang3
         {Str1[0]}   {Str1[1]}    {Str1[2]}    -a_hmax, a_hmin, a_vert
'''   
    

    VarModMapArg = {"NLags" : NLags,
                    "DLags" : DLags,
                    "Standardized" : Standardized,
                    "Angs" : Angs,
                    "Str1" : Str1,
                    "Sill1" : Sill1
                    }



    Temp = varmapmodstr.format(**VarModMapArg)

    text_file = open("varmap_mod.par", "w")
    n = text_file.write(Temp)
    text_file.close()
    
    

    subprocess.call("varmap_mod.exe varmap_mod.par", creationflags=CREATE_NO_WINDOW)
    os.remove("varmap_mod.par")
    
    Output_mod = pd.read_csv("varmap_mod.out", skiprows=3, delimiter="\s+", 
                         names=["Model"])
    os.remove("varmap_mod.out")
    Output_mod = Output_mod.to_numpy()
    VarValues_mod = Output_mod[:,0]
    Var3D_vals_mod = np.zeros((2*NLags[0]+1, 2*NLags[1]+1, 2*NLags[2]+1))

    pos = 0
    for i_z in range(2*NLags[2]+1):
        for i_y in range(2*NLags[1]+1):
            for i_x in range(2*NLags[0]+1):
                Var3D_vals_mod[i_x, i_y, i_z] = VarValues_mod[pos]
                pos += 1
    # #######################    
    
    return VarValues_mod, Var3D_vals_mod

def AutomaticVariogramModel3D(DH_DB, Variable, NLags='Auto', DLags='Auto', Title='Title',
                           MinPairs=4, Trim=[-99999,99999], Sted=True, OutputParam=False,
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
    
    Testing = True
    
    if Testing == True:
        Angs = [45,25,20]
        #Angs = [97,10,-160]
        #Angs = [120,40,-160]
        Str1 = [800,500,200]
        Sill1 = 0.8
    
        VarValues, Var3D_vals = FitVariogram(NLags, DLags, Standardized, 
                                                    Angs, 
                                                    Str1, 
                                                    Sill1)    
    
    else:
        Temp = varstr.format(**DictArg)
        
        text_file = open("varmap.par", "w")
        n = text_file.write(Temp)
        text_file.close()
        
        
        print("Computing experimental variogram map")
        subprocess.call("varmap.exe varmap.par", creationflags=CREATE_NO_WINDOW)
        os.remove("varmap.par")
        os.remove("tempData.txt")
        
        
        Output = pd.read_csv("temp_varmap.out", skiprows=8, delimiter="\s+", 
                             names=["V1", "V2", "V3", "V4", "V5", "V6"])
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

    
    # ########
    # Optimization
    # ########
    print("Optimizing parameters inference")
    Val_mat = np.copy(Var3D_vals)
    Angs, Str1, Sill1 = Optimize(Val_mat, NLags, DLags, Standardized)

    VarValues_mod, Var3D_vals_mod = FitVariogram(NLags, DLags, Standardized, 
                                                Angs, 
                                                Str1, 
                                                Sill1)

    Var3D_vals[Var3D_vals == -999] = np.NaN
    Var3D_vals[Var3D_vals > 1] = 1    


    # #######################
    fig = plt.figure(figsize=(16,8))
    left  = 0.125  
    right = 0.9    
    bottom = 0.1 
    top = 0.9   
    wspace = 0.4  
    hspace = 0.3  
    plt.subplots_adjust(left=left, bottom=bottom, 
                        right=right, top=top, 
                        wspace=wspace, hspace=hspace)
    
    # #######################
    
    ax1 = plt.subplot(231)
    MapVal = Var3D_vals[:,:,NLags[2]]
    c = ax1.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', 
                   extent=[-NLags[0]*DLags[0],NLags[0]*DLags[0],-NLags[1]*DLags[1],NLags[1]*DLags[1]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax1.set_xlabel("East")
    ax1.set_ylabel("North")
    ax1.grid(False)
    ax1.set_title("Samples - "+ Title +" - XY plane")
    ax1.set_aspect((NLags[0]*DLags[0])/(NLags[1]*DLags[1]))
    # #######################
    ax2 = plt.subplot(232)
    MapVal = Var3D_vals[:,NLags[1], :]
    c = ax2.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', 
                   extent=[-NLags[0]*DLags[0],NLags[0]*DLags[0],-NLags[2]*DLags[2],NLags[2]*DLags[2]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax2.set_xlabel("East")
    ax2.set_ylabel("Elevation")
    ax2.grid(False)
    ax2.set_title("Samples - "+ Title+" - XZ plane")
    ax2.set_aspect((NLags[0]*DLags[0])/(NLags[2]*DLags[2]))
    #ax2.set_aspect('equal', 'datalim')
    # #######################
    ax3 = plt.subplot(233)
    MapVal = Var3D_vals[NLags[0],:, :]
    c = ax3.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', 
                   extent=[-NLags[1]*DLags[1],NLags[1]*DLags[1],-NLags[2]*DLags[2],NLags[2]*DLags[2]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax3.set_xlabel("North")
    ax3.set_ylabel("Elevation")
    ax3.grid(False)
    ax3.set_title("Samples - "+ Title+" - YZ plane")
    ax3.set_aspect((NLags[1]*DLags[1])/(NLags[2]*DLags[2]))
    
    # #######################
    
    ax4 = plt.subplot(234)
    MapVal = Var3D_vals_mod[:,:,NLags[2]]
    c = ax4.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', 
                   extent=[-NLags[0]*DLags[0],NLags[0]*DLags[0],-NLags[1]*DLags[1],NLags[1]*DLags[1]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax4.set_xlabel("East")
    ax4.set_ylabel("North")
    ax4.grid(False)
    ax4.set_title("Model - "+ Title +" - XY plane")
    ax4.set_aspect((NLags[0]*DLags[0])/(NLags[1]*DLags[1]))
    # #######################
    ax5 = plt.subplot(235)
    MapVal = Var3D_vals_mod[:,NLags[1], :]
    c = ax5.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', 
                   extent=[-NLags[0]*DLags[0],NLags[0]*DLags[0],-NLags[2]*DLags[2],NLags[2]*DLags[2]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax5.set_xlabel("East")
    ax5.set_ylabel("Elevation")
    ax5.grid(False)
    ax5.set_title("Model - "+ Title+" - XZ plane")
    ax5.set_aspect((NLags[0]*DLags[0])/(NLags[2]*DLags[2]))
    #ax5.set_aspect('equal', 'datalim')
    # #######################
    ax6 = plt.subplot(236)
    MapVal = Var3D_vals_mod[NLags[0],:, :]
    c = ax6.imshow(MapVal.T, cmap ='jet', vmin = 0, vmax = 1.2, origin='lower', 
                   extent=[-NLags[1]*DLags[1],NLags[1]*DLags[1],-NLags[2]*DLags[2],NLags[2]*DLags[2]])
    plt.colorbar(c, fraction=0.046, pad=0.04)
    ax6.set_xlabel("North")
    ax6.set_ylabel("Elevation")
    ax6.grid(False)
    ax6.set_title("Model - "+ Title+" - YZ plane")
    ax6.set_aspect((NLags[1]*DLags[1])/(NLags[2]*DLags[2]))

    # #######################
    if PlotBool == True:
        plt.show()
    # #######################
    if OutputImage != None:
        fig.savefig(OutputImage, dpi=300, bbox_inches='tight')
    # #######################
    plt.close()
    if OutputParam == True:
        DictParam = {"Angs" : Angs,
          "Str1" : Str1,
          "Sill1" : Sill1
          }        
        return DictParam
    else:
        return None