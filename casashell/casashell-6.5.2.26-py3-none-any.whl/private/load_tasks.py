###########################################################################
########################## generated by setup.py ##########################
###########################################################################
__casashell_state__ = {}
from casatasks import casalog
try:
    casalog.showconsole(config.flags.log2term)
except:
    print("WARN:unable to configure logger. There may be issues with logging")

from casashell.private.builtin_mgr import register_builtin
from casashell.private.imhead import imhead
register_builtin("imhead")
from casashell.private.immoments import immoments
register_builtin("immoments")
from casashell.private.imhistory import imhistory
register_builtin("imhistory")
from casashell.private.applycal import applycal
register_builtin("applycal")
from casashell.private.bandpass import bandpass
register_builtin("bandpass")
from casashell.private.blcal import blcal
register_builtin("blcal")
from casashell.private.calstat import calstat
register_builtin("calstat")
from casashell.private.concat import concat
register_builtin("concat")
from casashell.private.split import split
register_builtin("split")
from casashell.private.listobs import listobs
register_builtin("listobs")
from casashell.private.flagdata import flagdata
register_builtin("flagdata")
from casashell.private.flagcmd import flagcmd
register_builtin("flagcmd")
from casashell.private.setjy import setjy
register_builtin("setjy")
from casashell.private.cvel import cvel
register_builtin("cvel")
from casashell.private.cvel2 import cvel2
register_builtin("cvel2")
from casashell.private.importuvfits import importuvfits
register_builtin("importuvfits")
from casashell.private.importfits import importfits
register_builtin("importfits")
from casashell.private.exportfits import exportfits
register_builtin("exportfits")
from casashell.private.exportuvfits import exportuvfits
register_builtin("exportuvfits")
from casashell.private.partition import partition
register_builtin("partition")
from casashell.private.listpartition import listpartition
register_builtin("listpartition")
from casashell.private.flagmanager import flagmanager
register_builtin("flagmanager")
from casashell.private.mstransform import mstransform
register_builtin("mstransform")
from casashell.private.tclean import tclean
register_builtin("tclean")
from casashell.private.deconvolve import deconvolve
register_builtin("deconvolve")
from casashell.private.immath import immath
register_builtin("immath")
from casashell.private.vishead import vishead
register_builtin("vishead")
from casashell.private.uvsub import uvsub
register_builtin("uvsub")
from casashell.private.spxfit import spxfit
register_builtin("spxfit")
from casashell.private.splattotable import splattotable
register_builtin("splattotable")
from casashell.private.specsmooth import specsmooth
register_builtin("specsmooth")
from casashell.private.specflux import specflux
register_builtin("specflux")
from casashell.private.smoothcal import smoothcal
register_builtin("smoothcal")
from casashell.private.specfit import specfit
register_builtin("specfit")
from casashell.private.imstat import imstat
register_builtin("imstat")
from casashell.private.slsearch import slsearch
register_builtin("slsearch")
from casashell.private.delmod import delmod
register_builtin("delmod")
from casashell.private.imsubimage import imsubimage
register_builtin("imsubimage")
from casashell.private.accor import accor
register_builtin("accor")
from casashell.private.asdmsummary import asdmsummary
register_builtin("asdmsummary")
from casashell.private.clearcal import clearcal
register_builtin("clearcal")
from casashell.private.conjugatevis import conjugatevis
register_builtin("conjugatevis")
from casashell.private.exportasdm import exportasdm
register_builtin("exportasdm")
from casashell.private.importasdm import importasdm
register_builtin("importasdm")
from casashell.private.clearstat import clearstat
register_builtin("clearstat")
from casashell.private.fixplanets import fixplanets
register_builtin("fixplanets")
from casashell.private.fixvis import fixvis
register_builtin("fixvis")
from casashell.private.phaseshift import phaseshift
register_builtin("phaseshift")
from casashell.private.fluxscale import fluxscale
register_builtin("fluxscale")
from casashell.private.ft import ft
register_builtin("ft")
from casashell.private.gaincal import gaincal
register_builtin("gaincal")
from casashell.private.gencal import gencal
register_builtin("gencal")
from casashell.private.testconcat import testconcat
register_builtin("testconcat")
from casashell.private.apparentsens import apparentsens
register_builtin("apparentsens")
from casashell.private.hanningsmooth import hanningsmooth
register_builtin("hanningsmooth")
from casashell.private.imcollapse import imcollapse
register_builtin("imcollapse")
from casashell.private.imcontsub import imcontsub
register_builtin("imcontsub")
from casashell.private.imdev import imdev
register_builtin("imdev")
from casashell.private.imfit import imfit
register_builtin("imfit")
from casashell.private.impbcor import impbcor
register_builtin("impbcor")
from casashell.private.importasap import importasap
register_builtin("importasap")
from casashell.private.importatca import importatca
register_builtin("importatca")
from casashell.private.importfitsidi import importfitsidi
register_builtin("importfitsidi")
from casashell.private.importgmrt import importgmrt
register_builtin("importgmrt")
from casashell.private.importnro import importnro
register_builtin("importnro")
from casashell.private.importvla import importvla
register_builtin("importvla")
from casashell.private.impv import impv
register_builtin("impv")
from casashell.private.imrebin import imrebin
register_builtin("imrebin")
from casashell.private.imreframe import imreframe
register_builtin("imreframe")
from casashell.private.imregrid import imregrid
register_builtin("imregrid")
from casashell.private.imsmooth import imsmooth
register_builtin("imsmooth")
from casashell.private.imtrans import imtrans
register_builtin("imtrans")
from casashell.private.imval import imval
register_builtin("imval")
from casashell.private.initweights import initweights
register_builtin("initweights")
from casashell.private.listcal import listcal
register_builtin("listcal")
from casashell.private.listfits import listfits
register_builtin("listfits")
from casashell.private.listhistory import listhistory
register_builtin("listhistory")
from casashell.private.listsdm import listsdm
register_builtin("listsdm")
from casashell.private.listvis import listvis
register_builtin("listvis")
from casashell.private.makemask import makemask
register_builtin("makemask")
from casashell.private.polcal import polcal
register_builtin("polcal")
from casashell.private.polfromgain import polfromgain
register_builtin("polfromgain")
from casashell.private.predictcomp import predictcomp
register_builtin("predictcomp")
from casashell.private.rerefant import rerefant
register_builtin("rerefant")
from casashell.private.rmfit import rmfit
register_builtin("rmfit")
from casashell.private.rmtables import rmtables
register_builtin("rmtables")
from casashell.private.sdatmcor import sdatmcor
register_builtin("sdatmcor")
from casashell.private.sdbaseline import sdbaseline
register_builtin("sdbaseline")
from casashell.private.sdcal import sdcal
register_builtin("sdcal")
from casashell.private.sdfit import sdfit
register_builtin("sdfit")
from casashell.private.sdfixscan import sdfixscan
register_builtin("sdfixscan")
from casashell.private.sdgaincal import sdgaincal
register_builtin("sdgaincal")
from casashell.private.sdimaging import sdimaging
register_builtin("sdimaging")
from casashell.private.sdsmooth import sdsmooth
register_builtin("sdsmooth")
from casashell.private.tsdimaging import tsdimaging
register_builtin("tsdimaging")
from casashell.private.nrobeamaverage import nrobeamaverage
register_builtin("nrobeamaverage")
from casashell.private.sdtimeaverage import sdtimeaverage
register_builtin("sdtimeaverage")
from casashell.private.simalma import simalma
register_builtin("simalma")
from casashell.private.simobserve import simobserve
register_builtin("simobserve")
from casashell.private.simanalyze import simanalyze
register_builtin("simanalyze")
from casashell.private.feather import feather
register_builtin("feather")
from casashell.private.statwt import statwt
register_builtin("statwt")
from casashell.private.virtualconcat import virtualconcat
register_builtin("virtualconcat")
from casashell.private.uvcontsub_old import uvcontsub_old
register_builtin("uvcontsub_old")
from casashell.private.uvcontsub import uvcontsub
register_builtin("uvcontsub")
from casashell.private.uvmodelfit import uvmodelfit
register_builtin("uvmodelfit")
from casashell.private.visstat import visstat
register_builtin("visstat")
from casashell.private.widebandpbcor import widebandpbcor
register_builtin("widebandpbcor")
from casashell.private.importmiriad import importmiriad
register_builtin("importmiriad")
from casashell.private.plotweather import plotweather
register_builtin("plotweather")
from casashell.private.plotants import plotants
register_builtin("plotants")
from casashell.private.fringefit import fringefit
register_builtin("fringefit")
from casashell.private.plotbandpass import plotbandpass
register_builtin("plotbandpass")
from casashell.private.sdintimaging import sdintimaging
register_builtin("sdintimaging")
from casashell.private.sdpolaverage import sdpolaverage
register_builtin("sdpolaverage")
from casashell.private.sdsidebandsplit import sdsidebandsplit
register_builtin("sdsidebandsplit")
from casashell.private.plotprofilemap import plotprofilemap
register_builtin("plotprofilemap")
from casashell.private.imbaseline import imbaseline
register_builtin("imbaseline")

