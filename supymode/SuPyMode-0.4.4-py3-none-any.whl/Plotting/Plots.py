#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, numpy
import matplotlib.pyplot     as plt
from matplotlib              import colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.backends.backend_pdf import PdfPages

from SuPyMode.Plotting.PlotsUtils  import FieldMap, MidPointNorm
from dataclasses import dataclass


try:
    from mayavi     import mlab
    from tvtk.tools import visual
except ImportError:
    logging.warning('Mayavi package could not be loaded! Not 3D rendering available.')


import matplotlib
matplotlib.style.use('ggplot')


@dataclass
class ColorBar:
    Color: str = 'viridis'
    Discreet: bool = False
    Position: str = 'left'
    Orientation: str = "vertical"
    Symmetric: bool = False

    def Render(self, Ax, Scalar, Image):
        divider = make_axes_locatable(Ax._ax)
        cax = divider.append_axes(self.Position, size="10%", pad=0.15)

        if self.Discreet:
            Norm = colors.BoundaryNorm(numpy.unique(Scalar), 200, extend='both')
            Image.set_norm(Norm)
            ticks = numpy.unique(Scalar)
            plt.colorbar(mappable=Image, norm=Norm, boundaries=ticks, ticks=ticks, cax=cax, orientation=Ax.Colorbar.Orientation)

        if self.Symmetric:
            Norm = colors.CenteredNorm()
            Image.set_norm(Norm)
            plt.colorbar(mappable=Image, norm=Norm, cax=cax, orientation=self.Orientation)

        else:
            plt.colorbar(mappable=Image, norm=None, cax=cax, orientation=self.Orientation)



@dataclass
class Contour:
    X: numpy.ndarray
    Y: numpy.ndarray
    Scalar: numpy.ndarray
    ColorMap: str = 'viridis'
    xLabel: str = ''
    yLabel: str = ''
    IsoLines: list = None

    def Render(self, Ax):
        Image = Ax.contour(self.X,
                            self.Y,
                            self.Scalar,
                            level = self.IsoLines,
                            colors="black",
                            linewidth=.5 )

        Image = Ax.contourf(self.X,
                            self.Y,
                            self.Scalar,
                            level = self.IsoLines,
                            cmap=self.ColorMap,
                            norm=colors.LogNorm() )


@dataclass
class Mesh:
    X: numpy.ndarray
    Y: numpy.ndarray
    Scalar: numpy.ndarray
    ColorMap: str = 'viridis'
    Label: str = ''

    def Render(self, Ax):
        Image = Ax._ax.pcolormesh(self.X, self.Y, numpy.flip(self.Scalar.T, axis=0), cmap=self.ColorMap, shading='auto')

        if Ax.Colorbar is not None:
            Ax.Colorbar.Render(Ax=Ax, Scalar=self.Scalar, Image=Image)

        return Image


@dataclass
class Line:
    X: numpy.ndarray
    Y: numpy.ndarray
    Label: str = None
    Fill: bool = False
    Color: str = None

    def Render(self, Ax):

        Ax._ax.plot(self.X, self.Y, label=self.Label)

        if self.Fill:
            Ax._ax.fill_between(self.X, self.Y.min(), self.Y, color=self.Color, alpha=0.7)






class Scene:
    UnitSize = (10, 3)
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams["font.size"]       = 8
    plt.rcParams["font.family"]     = "serif"
    plt.rcParams['axes.edgecolor']  = 'black'
    plt.rcParams['axes.linewidth']  = 1.5
    plt.rcParams['legend.fontsize'] = 'small'

    def __init__(self, Title='', UnitSize=None):
        self.Axis = []
        self.Title = Title
        self.nCols = 1
        self.nRows = None
        if UnitSize is not None: self.UnitSize = UnitSize


    def AddAxes(self, *Axis):
        for ax in Axis:
            self.Axis.append(ax)

    def NextColumn(self, Axis):
        MaxCol, MaxRow = self.GetMaxColsRows()
        Axis.Col = MaxCol
        self.AddAxes(Axis)


    def GetMaxColsRows(self):
        RowMax, ColMax = 0,0
        for ax in self.Axis:
            RowMax = ax.Row if ax.Row > RowMax else RowMax
            ColMax = ax.Col if ax.Col > ColMax else ColMax

        return RowMax, ColMax


    def GenerateAxis(self):
        RowMax, ColMax = self.GetMaxColsRows()

        self.nRows = len(self.Axis)

        FigSize = [ self.UnitSize[0]*(ColMax+1), self.UnitSize[1]*(RowMax+1) ]

        self.Figure, Ax  = plt.subplots(ncols=ColMax+1, nrows=RowMax+1, figsize=FigSize)

        Ax = numpy.atleast_2d(Ax).reshape([RowMax+1, ColMax+1] )

        self.Figure.suptitle(self.Title)

        for ax in self.Axis:
            ax._ax = Ax[ax.Row, ax.Col]


    def Render(self):
        logging.info("Rendering Scene...")
        self.GenerateAxis()

        for ax in self.Axis:
            ax.Render()

        plt.tight_layout()

        return self


    def Show(self):
        self.Render()
        plt.show()




@dataclass
class Axis:
    Row: int
    Col: int
    xLabel: str = ''
    yLabel: str = ''
    Title: str = ''
    Grid: bool = True
    Legend: bool = False
    xScale: str = 'linear'
    yScale: str = 'linear'
    xLimits: list = None
    yLimits: list = None
    Equal: bool = False
    Colorbar: ColorBar = None
    WaterMark: str = ''
    Figure: Scene = None

    def __post_init__(self):

        self._ax = None
        self.Artist  = []


    @property
    def Labels(self):
        return {'x': self.xLabel,
                'y': self.yLabel,
                'Title': self.Title}


    def AddArtist(self, *Artist):
        for art in Artist:
            self.Artist.append(art)

    def Render(self):
        logging.info("Rendering Axis...")

        for art in self.Artist:
            Image = art.Render(self)

        if self.Legend:
            self._ax.legend(fancybox=True, facecolor='white', edgecolor='k')


        self._ax.grid(self.Grid)

        if self.xLimits is not None: self._ax.set_xlim(self.xLimits)
        if self.yLimits is not None: self._ax.set_ylim(self.yLimits)

        self._ax.set_xlabel(self.Labels['x'])
        self._ax.set_ylabel(self.Labels['y'])
        self._ax.set_title(self.Labels['Title'])

        self._ax.set_xscale(self.xScale)
        self._ax.set_yscale(self.yScale)

        self._ax.text(0.5, 0.1, self.WaterMark, transform=self._ax.transAxes,
                fontsize=30, color='white', alpha=0.2,
                ha='center', va='baseline', rotation='0')

        if self.Equal:
            self._ax.set_aspect("equal")










def Multipage(filename, figs=None, dpi=200):
    logging.info("Rendering Multipage...")
    logging.info(f'Saving results into {filename}...')

    pp = PdfPages(filename)

    for fig in figs:
        fig.Figure.savefig(pp, format='pdf')


    pp.close()





# -
