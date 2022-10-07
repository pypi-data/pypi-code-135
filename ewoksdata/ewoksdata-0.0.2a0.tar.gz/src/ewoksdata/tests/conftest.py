import numpy
import pytest
from . import data


@pytest.fixture(scope="session")
def bliss_scan(tmpdir_factory):
    tmpdir = tmpdir_factory.mktemp("sample_dataset")
    npoints_per_file = 3
    npoints = 31
    scannr = 2
    subscannr = 1
    detector = "p3"
    image = numpy.zeros((10, 12))
    return data.save_bliss_scan(
        tmpdir,
        image,
        npoints_per_file,
        npoints,
        scannr,
        subscannr,
        detector,
        sequence="add",
    )
