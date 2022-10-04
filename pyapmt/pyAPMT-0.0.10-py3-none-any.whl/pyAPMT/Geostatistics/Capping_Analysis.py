# -*- coding: utf-8 -*-
"""

Module dedicated to Capping Analysis Analysis.
Code inspired by the development of Ilkay Cevik @ SRK - 2021
as part of the Python Package for internal use at SRK. Thanks!

"""

# Author: Sebastian Avalos <sebastian.avalos@apmodtech.com>
#         Advanced Predictive Modeling Technology
#         www.apmodtech.com/pyAPMT/
#         September-2022
#
# License: MIT License


# All submodules and packages
import pandas as pd
import numpy as np
import probscale
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1)
sns.set_style("whitegrid")


import logging
logging.getLogger().setLevel(logging.CRITICAL)

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

def ProbPlot(tVec, Label = "Label", Title="Title", Axes=None, pVec=None, 
             CatLabel=None, Capp=None, Perc=True, X_Lims=[None, None]):
    probscale.probplot(tVec, 
                       plottype='prob',
                       problabel='Standard Normal Probabilities',
                       color = "black",
                       weights = None,
                       probax = 'y', 
                       datalabel = None, 
                       scatter_kws = dict(marker='.', linestyle = 'none', markersize = 2),
                           ax = Axes,
                          label = Label)
  
    
    if X_Lims[0] < 0.001:
        Axes.set_xlim(0.001, X_Lims[1])
    else:
        Axes.set_xlim(X_Lims)
    

    
    if Capp != None:
        Axes.axvline(x=Capp, lw=0.9, ls='-', color="red", label="Capping : %s"%(Capp))
    
    Axes.set_xscale('symlog', linthreshx=0.01)
    Axes.grid(True, which="both")  
    locmaj = ticker.LogLocator(base=10,numticks=20)
    locmin = ticker.LogLocator(base=10.0,subs=tuple(np.arange(0.1,1,0.1)),numticks=20)
    Axes.xaxis.set_major_locator(locmaj)
    Axes.xaxis.set_minor_locator(locmin)
    #Axes.set_xticks([1,10,100, 1000, 10000, 100000]) # Zn
    #Axes.set_xticks([0, 1,10,100, 1000, 10000, 100000]) # Pb
    #Axes.set_xticks([10, 100, 1000, 10000, 100000]) # Cu
    #Axes.set_xticks([0, 0.01, 0.1,1,10,100]) # Au
    
    Axes.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.4f'))
    Axes.xaxis.set_major_formatter(ticker.ScalarFormatter())
    Axes.set_ylim(bottom=0.1, top=99.9)
    Axes.set_title(Title)
    Axes.set_xlabel(CatLabel)
    Axes.legend(loc='upper left')
    
    if Perc == True:
        Axes.axvline(x=pVec[0], lw=0.5, ls='--', color="darkviolet", label="$p95$")
        Axes.axvline(x=pVec[1], lw=0.5, ls='--', color="green", label="$p98$")
        Axes.axvline(x=pVec[2], lw=0.5, ls='--', color="darkblue", label="$p99$") 
    Axes.grid(True)
    
    return None



  
def Histogram(tVec, Label = "Label", Title="Title", Axes=None, pVec=None, 
              CatLabel=None, Capp=None, Perc=True, X_Lims=[None, None]):
    def describe_helper(series):
        splits = str(series).split()
        keys, values = "", ""
        for i in range(0, len(splits) - 2, 2):
            keys += "{:8}\n".format(splits[i])
            values += "{:>8}\n".format(splits[i+1])
        return keys, values
  
    Axes.hist(tVec, bins=50, edgecolor='white', color='#403E3E')
    
    count, division = np.histogram(tVec, bins=50)
    #print(count, division)
    Axes.set_xlim(X_Lims)
    #Axes.set_xticks([1,50000, 100000, 150000, 200000]) # Zn
    Axes.set_title(Title)
    Axes.set_xlabel(CatLabel)  
    Axes.set_ylabel("Frequency") 
    

    if Capp != None:
        Axes.axvline(x=Capp, lw=0.9, ls='-', color="red", label="Capping : %s"%(Capp))
    
    stat_dict = {
        'Count': f"{len(tVec):,d}",
              'Mean': f"{np.mean(tVec):,.3f}",
              'Std': f"{np.std(tVec):,.3f}",
              'CoV':f"{np.std(tVec) / np.mean(tVec):,.3f}",
              'Max': f"{np.max(tVec):,.3f}",
              'Q3': f"{np.percentile(tVec, 75):,.3f}",
              'Median': f"{np.percentile(tVec, 50):,.3f}",
              'Q1': f"{np.percentile(tVec, 25):,.3f}",
              'Min': f"{np.min(tVec):,.3f}"
    }  
    
    stat_dict_pd = pd.Series(stat_dict)
    
    stat_x = int(np.max(division)/2) 
    
    stat_y = int(np.max(count)/2)*0.9  
    Delta = np.max(division)/4
    
    
    t = Axes.text(stat_x, stat_y, describe_helper(stat_dict_pd)[0], {'multialignment':'left'})
    t.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='white'))
    t = Axes.text(stat_x + Delta, stat_y, describe_helper(stat_dict_pd)[1], {'multialignment':'right'})
    t.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='white'))
    
    if Perc == True:
        Axes.axvline(x=pVec[0], lw=0.5, ls='--', color="darkviolet", label="$p95$")
        Axes.axvline(x=pVec[1], lw=0.5, ls='--', color="green", label="$p98$")
        Axes.axvline(x=pVec[2], lw=0.5, ls='--', color="darkblue", label="$p99$") 
    
    Axes.grid(True)
    return None

def MeanVSCapped(tVec, Zone = "Label", Title="Title", Axes=None, pVec=None, 
                 CatLabel=None, Capp=None, Perc=True, X_Lims=[None, None]):
    #tR = np.arange(0,tVec.max(),100, dtype=int)
    #tR = np.arange(0,tVec.max(),100)
    #print(tVec)
    #print(tR)
    #Rango = np.arange(tVec.min()*2,tVec.max(),len(tR), dtype=int)
    #Rango = np.arange(tVec.min()*2,tVec.max(),len(tR))
    
    MaxLim = np.max(tVec)
    MinLim = np.min(tVec)
    Rango = np.arange(MinLim, MaxLim, (MaxLim-MinLim)/100)
    
    Res = np.zeros((len(Rango), 3))
    j = 0
    for ii in Rango:
        tV = tVec.copy()
        Res[j,0] = ii
        Res[j,2] = len(tV[tV >= ii])
        
        tV[tV >= ii] = ii
        
        Res[j,1] = tV.mean()
        j += 1
      
    

    
    if Capp != None:
        Axes.axvline(x=Capp, lw=0.9, ls='-', color="red")
    
    #Axes.set_xticks([1,50000, 100000, 150000, 200000]) # Zn
    #Axes.set_xticks([0,1,2,3,4,5]) # Au
    #Axes.set_xlim(X_Lims[0], X_Lims[1])
    Axes.set_title(Title)
    Axes.set_xlabel(CatLabel)  
    Axes.set_ylabel("Mean")   
    Axes.plot(Res[:,0], Res[:,1], color="black", label="Mean")
    ax2 = Axes.twinx()
    ax2.set_ylabel("Number of capped data")  
    ax2.plot(Res[:,0], Res[:,2], color="orange", label="Number of capped data")  
    
    if Perc == True:
        Axes.axvline(x=pVec[0], lw=0.5, ls='--', color="darkviolet", label="$p95$")
        Axes.axvline(x=pVec[1], lw=0.5, ls='--', color="green", label="$p98$")
        Axes.axvline(x=pVec[2], lw=0.5, ls='--', color="darkblue", label="$p99$") 
    
    Axes.legend(loc='center right')
    ax2.legend(loc='upper left')
    Axes.grid(False)
    ax2.grid(False)
    return None
  



def CV_vs_MetalLost(tVec, Zone = "Label", Title="Title", Axes=None, pVec=None, 
                    CatLabel=None, Capp=None, Perc=True, X_Lims=[None, None]):
    #tR = np.arange(0,tVec.max(),100, dtype=int)
    #Rango = np.arange(tVec.min()*2+0.001,tVec.max(),len(tR), dtype=int)
    
    MaxLim = np.max(tVec)
    MinLim = np.min(tVec)
    Rango = np.arange(MinLim, MaxLim, (MaxLim-MinLim)/100)
    
    Res = np.zeros((len(Rango), 3))
    
    OrgMetal = tVec.mean()
    
    j = 0
    for ii in Rango:
        if j > 0:
            tV = tVec.copy()
            Res[j,0] = ii
            
            tV[tV >= ii] = ii
            
            Res[j,1] = tV.std()/tV.mean()
            Res[j,2] = (OrgMetal  - tV.mean())/OrgMetal*100
        j += 1
    
  

    if Capp != None:
        Axes.axvline(x=Capp, lw=0.9, ls='-', color="red")
  
  
    
    #Axes.set_xticks([1,50000, 100000, 150000, 200000]) # Zn
    #Axes.set_xlim(X_Lims[0], X_Lims[1])
    Axes.set_title(Title)
    Axes.set_xlabel(CatLabel)  
    Axes.set_ylabel("Coeff. Var.")   
    Axes.plot(Res[1:,0], Res[1:,1], color="black", label="Coeff. Var.")
    ax2 = Axes.twinx()
    ax2.set_ylabel("Metal Lost (%)")  
    ax2.plot(Res[1:,0], Res[1:,2], color="orange", label="Metal Lost (%)") 
    
    if Perc == True:
        Axes.axvline(x=pVec[0], lw=0.5, ls='--', color="darkviolet", label="$p95$")
        Axes.axvline(x=pVec[1], lw=0.5, ls='--', color="green", label="$p98$")
        Axes.axvline(x=pVec[2], lw=0.5, ls='--', color="darkblue", label="$p99$") 
    
    Axes.legend(loc='center right')
    ax2.legend(loc='upper left')
    Axes.grid(False)
    ax2.grid(False)
    
    return None


def ComputeCappingAnalysis(DH_DB, Variable, kls='Global', Capp=None, Perc=None,
                           OutputImage=None, Dom=None, PlotBool=True, SubDom=None,
                           X_Lims=[None, None]):
    
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.4   # the amount of width reserved for blank space between subplots
    hspace = 0.4   # the amount of height reserved for white space between subplots
    

    if Dom == None:
        tVec = DH_DB.DB[[Variable]].to_numpy()
    else:
        SubSet1 = DH_DB.DB[DH_DB.DB[Dom] == SubDom]
        tVec = SubSet1[[Variable]].to_numpy()
    p95 = np.around(np.percentile(tVec, 95), decimals=2)
    p98 = np.around(np.percentile(tVec, 98), decimals=2)
    p99 = np.around(np.percentile(tVec, 99), decimals=2)
    pVec = [p95, p98, p99]
    
    fig, ax = plt.subplots(2,2, figsize=(12, 10)) 
    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
    
    if Dom == None:
        Histogram(tVec=tVec, Title=f"Histogram - {Variable}", Axes=ax[0,0], 
                  Label=kls, CatLabel=Variable, pVec=pVec, Capp=Capp, Perc=Perc,
                  X_Lims=X_Lims)
        ProbPlot(tVec=tVec, Title=f"Cumulative Prob. Plot - {Variable}", Axes=ax[0,1], 
                 Label=kls, CatLabel=Variable, pVec=pVec, Capp=Capp, Perc=Perc,
                 X_Lims=X_Lims)
        MeanVSCapped(tVec=tVec, Title=f"Mean vs Number of capped samples", Axes=ax[1,0], 
                     Zone=kls, CatLabel=Variable, pVec=pVec, Capp=Capp, Perc=Perc,
                     X_Lims=X_Lims)
        CV_vs_MetalLost(tVec=tVec, Title=f"Coeff of Variation vs Metal Lost (%)", Axes=ax[1,1], 
                        Zone=kls, CatLabel=Variable, pVec=pVec, Capp=Capp, Perc=Perc,
                        X_Lims=X_Lims)
    else:
        Histogram(tVec=tVec, Title=f"Histogram - {Variable} - {SubDom}", Axes=ax[0,0], 
                  Label=kls, CatLabel=Variable, pVec=pVec, Capp=Capp, Perc=Perc,
                  X_Lims=X_Lims)
        ProbPlot(tVec=tVec, Title=f"Cumulative Prob. Plot - {Variable} - {SubDom}", Axes=ax[0,1], 
                 Label=kls, CatLabel=Variable, pVec=pVec, Capp=Capp, Perc=Perc,
                 X_Lims=X_Lims)
        MeanVSCapped(tVec=tVec, Title=f"Mean vs Number of capped samples - {SubDom}", Axes=ax[1,0], 
                     Zone=kls, CatLabel=Variable, pVec=pVec, Capp=Capp, Perc=Perc,
                     X_Lims=X_Lims)
        CV_vs_MetalLost(tVec=tVec, Title=f"Coeff of Variation vs Metal Lost (%) - {SubDom}", Axes=ax[1,1], 
                        Zone=kls, CatLabel=Variable, pVec=pVec, Capp=Capp, Perc=Perc,
                        X_Lims=X_Lims)        
    
    # #######################
    if PlotBool == True:
        plt.show()
    # #######################
    if OutputImage != None:
        fig.savefig(OutputImage, dpi=300, bbox_inches='tight')
    # #######################
    return plt.close()