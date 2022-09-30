import pytest
import sys
import importlib

def load_assessment( name ):

    assessment_test = importlib.__import__( 'testing.assessments', fromlist=[name] )
    assessment_module = getattr( assessment_test, name )
    
    return assessment_module

def run_test( module ):

    return_code = 0
    try:
        module.test()
    except:
        return_code = 1 

    raise SystemExit( return_code )
