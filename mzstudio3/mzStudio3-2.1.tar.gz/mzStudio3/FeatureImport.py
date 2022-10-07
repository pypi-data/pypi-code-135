
import pickle
import time
from multiplierz.mzTools.featureDetector import Feature


def run_test():
    pass#print "***********************************************************************************"
    pass#print "***********************************************************************************"
    a = time.time()
    pickle_file = open(r'D:\SBF\2015-01-13-CSF\FEATURES.pkl', "r")
    scanToF = cPickle.load(pickle_file)
    scanFToPeaks = cPickle.load(pickle_file)
    featureToPSMs = cPickle.load(pickle_file)     
    pickle_file.close()   
    pass#print "Loaded"
    b = time.time()
    pass#print b-a
    pass#print "***********************************************************************************"
    pass#print "***********************************************************************************"    
    #pass#print scanToF[5279]
    #pass#print scanFToPeaks[5279, 16]
    
    return scanToF, scanFToPeaks, featureToPSMs
    
#run_test()

def import_features(filename):
    pass#print "***********************************************************************************"
    pass#print "***********************************************************************************"
    a = time.time()
    pickle_file = open(filename, "r")
    scanToF = cPickle.load(pickle_file)
    scanFToPeaks = cPickle.load(pickle_file)
    featureToPSMs = cPickle.load(pickle_file)     
    pickle_file.close()   
    pass#print "Loaded"
    b = time.time()
    pass#print b-a
    pass#print "***********************************************************************************"
    pass#print "***********************************************************************************"    
    #pass#print scanToF[5279]
    #pass#print scanFToPeaks[5279, 16]
    
    return scanToF, scanFToPeaks, featureToPSMs