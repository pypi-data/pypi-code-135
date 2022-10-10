import pytest
import pandas as pd
import sys
import pkgutil
from io import BytesIO
sys.path.insert(0, '../src/checkContaminants')
from checkContaminants.checkContaminants import location_contamination

def test_repeats():
    data = pkgutil.get_data(__name__, 'data/gentests/repeatedspecies.csv')
    data = pd.DataFrame(pd.read_csv(BytesIO(data)))
    # data = pd.read_csv('../gentests/repeatedspecies.csv')
    loc = location_contamination()
    with pytest.raises(Exception) as excinfo:
        loc.check_data(data)
    assert str(excinfo.value) == 'You have a repeated Species names!'

def test_non_numerics():
    data = pkgutil.get_data(__name__, 'data/gentests/nonnumeric.csv')
    data = pd.DataFrame(pd.read_csv(BytesIO(data)))
    # data = pd.read_csv('../gentests/nonnumeric.csv')
    loc = location_contamination()
    with pytest.raises(Exception) as excinfo:
        loc.check_data(data)
    assert str(excinfo.value) == 'Columns must only contain numeric values!'

def test_max_bounds():
    data = pkgutil.get_data(__name__, 'data/gentests/maxcols.csv')
    data = pd.DataFrame(pd.read_csv(BytesIO(data)))
    # data = pd.read_csv('../gentests/maxcols.csv')
    loc = location_contamination()
    with pytest.raises(Exception) as excinfo:
        loc.check_data(data)
    assert 'The maximum number of columns is a 1000.' in str(excinfo.value)