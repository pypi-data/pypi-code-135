# -*- coding: utf-8 -*-
"""

Class dedicated to Drill-Holes database

"""

# Author: Sebastian Avalos <sebastian.avalos@apmodtech.com>
#         Advanced Predictive Modeling Technology
#         www.apmodtech.com/pyAPMT/
#         Jan-2022
#
# License: MIT License


# All submodules and packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


# pyAPMT functions
from . import Contact_Analysis
from .Contact_Analysis import PlotContacs
from .Probability_plots import ProbabilityPlot
from .Slides_2D import Plot2DSlides
from .Nearest_Neighbor import ComputeNearestNeighbor
from .Variogram_Maps3D import ComputeVariogramMaps3D
from .Capping_Analysis import ComputeCappingAnalysis
from .AdjustVarMod3D import AutomaticVariogramModel3D


__all__ = ['DrillHoles', 'PlotContacs', 'ProbabilityPlot', 'Plot2DSlides',\
           'ComputeNearestNeighbor', 'ComputeVariogramMaps3D', 'ComputeCappingAnalysis',\
           'AutomaticVariogramModel3D']

class DrillHoles:
	
	def __init__(self, DH_DB, East, North, Elevation, \
	             HoleID=None, From = None, To = None, Length = None):
		self.DB = pd.read_csv(DH_DB, low_memory=False)
		self.East = East
		self.North = North
		self.Elevation = Elevation
		self.HoleID = HoleID		
		self.From = From
		self.To = To
		self.Length = Length
		self.Header = list(self.DB.columns.values)
		
	def Describe(self):
		return self.DB.describe()
	
	def ElemInDom(self, Dom):
		'''Categorical elements as list on a selected column'''
		Cat = []
		for ii in self.DB[Dom]:
			if ii not in Cat:
				Cat.append(ii)
		return Cat	
		
	def SampleLength(self):
		if 'Length' not in self.Header:
			self.DB['Length'] = self.DB['From'] - self.DB['To'] 
		return None
	
	def ContactAnalysis(self, Dom, Var, MaxDis, Spacing=5,\
	                    SubDom =  None, OutputImage=None, PlotBool=True): 
		return PlotContacs(DH_DB=self.DB, Domains=Dom, Element=Var, MaxDistance=MaxDis, \
		                   East=self.East , North=self.North, Spacing=Spacing, \
		                   Elevation=self.Elevation, Zones = SubDom, ImName = OutputImage,
		                   PlotBool=PlotBool)
	
	
	def Plot_2D_Slides(self, Var, scale_factor=5, BWidth = 20, cmap = "rainbow", \
	                   Axes=None, East_lims = None, North_lims = None, \
	                   Elev_lims = None, VMin = 0, VMax = None):

		return Plot2DSlides(dB=self.DB, Var=Var, scale_factor=scale_factor, BWidth = BWidth, cmap = cmap, \
	                   Axes=Axes, East_lims = East_lims, North_lims = North_lims, \
	                   Elev_lims = Elev_lims, VMin = VMin, VMax = VMax,\
		               East=self.East, North=self.North, Elevation=self.Elevation)	
	
	
	def ProbPlot(self, Dom, Var, SubDom, Axes=None, CatLabel=None, \
	             Label = "UE :", Title="Probability Plots",\
	             Log_Scale=True, mSi = 2, markerscale=5, XMinMax = [0.01, 50], \
	             X_ticks = [0.01, 0.1, 1, 10, 50]):
		
		return ProbabilityPlot(DH_DB=self.DB, Dom=Dom, Var=Var, SubDom=SubDom,\
		     Label = Label, Title=Title, mSi = mSi, markerscale=markerscale, \
		     color="blue", XMinMax = XMinMax, X_ticks = X_ticks, \
             Axes=Axes, CatLabel=CatLabel, Log_Scale=Log_Scale)
	
	
	def NearestNeighbor(self, db_BH, VarBH, NNVar = None):
		return ComputeNearestNeighbor(db_DH = self, db_BH=db_BH, VarBH=VarBH,\
			                      NNVar = NNVar)
	
	def VariogramMaps3D(self, Var, NLags='Auto', DLags='Auto', Title='Title',
	                    MinPairs=4, Trim=[-1e21,1e21], Sted=True, 
	                    OutputImage='VariogramMaps.png', Dom=None, PlotBool=True, 
	                    SubDom=None):	
		
		return ComputeVariogramMaps3D(DH_DB=self, Variable=Var, NLags=NLags, DLags=DLags, 
		                              Title=Title, MinPairs=MinPairs, 
		                              Trim=Trim, Sted=Sted, OutputImage=OutputImage, 
		                              Dom=Dom, PlotBool=PlotBool, SubDom=SubDom)
	
	def CappingAnalysis(self, Var, kls='Global', Capp=None, Perc=True,
	                    OutputImage=None, Dom=None, PlotBool=True, SubDom=None,
	                    X_Lims=[None,None]):

		return ComputeCappingAnalysis(DH_DB=self, Variable=Var, kls=kls, Capp=Capp, Perc=Perc,
		                OutputImage=OutputImage, Dom=Dom, PlotBool=PlotBool, SubDom=SubDom,
		                X_Lims=X_Lims)
	
	def AutoFit_VariogramModel3D(self, Var, NLags='Auto', DLags='Auto', Title='Title',
	                    MinPairs=4, Trim=[-1e21,1e21], Sted=True, 
	                    OutputImage='VariogramMaps.png', Dom=None, PlotBool=True, 
	                    SubDom=None, OutputParam=False,):	

		return AutomaticVariogramModel3D(DH_DB=self, Variable=Var, NLags=NLags, DLags=DLags, 
		                              Title=Title, MinPairs=MinPairs, 
		                              Trim=Trim, Sted=Sted, OutputImage=OutputImage, 
		                              Dom=Dom, PlotBool=PlotBool, SubDom=SubDom,
		                              OutputParam=OutputParam)	