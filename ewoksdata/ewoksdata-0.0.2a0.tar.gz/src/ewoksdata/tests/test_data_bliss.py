import os
from ..data import bliss


def test_find_lima_files(bliss_scan):
    expected = [
        os.path.join(bliss_scan.dirname, "scan0002", f"p3_{i}.h5") for i in range(11)
    ]
    found = bliss._find_lima_files(bliss_scan, 2, "p3")
    assert expected == found
    assert not bliss._find_lima_files(bliss_scan, 1, "p3")
    assert not bliss._find_lima_files(bliss_scan, 2, "p")


def test_iter_lima_files(bliss_scan):
    filenames = bliss._find_lima_files(bliss_scan, 2, "p3")
    file_fmt = os.path.join(bliss_scan.dirname, "scan0002", "p3_{}.h5")
    dset_path = "/entry_0000/measurement/data"

    expected = [(file_fmt.format(i), dset_path, 0, 3) for i in range(11)]
    found = list(bliss._iter_lima_images(filenames))
    assert expected == found

    expected = [(file_fmt.format(0), dset_path, 0, 1)]
    found = list(bliss._iter_lima_images(filenames, start_index=0, end_index=1))
    assert expected == found

    expected = [
        (file_fmt.format(0), dset_path, 2, 3),
        (file_fmt.format(1), dset_path, 0, 1),
    ]
    found = list(bliss._iter_lima_images(filenames, start_index=2, end_index=4))
    assert expected == found

    expected = [
        (file_fmt.format(2), dset_path, 2, 3),
        (file_fmt.format(3), dset_path, 0, 1),
    ]
    found = list(
        bliss._iter_lima_images(filenames, start_index=2 + 2 * 3, end_index=4 + 2 * 3)
    )
    assert expected == found

    expected = [(file_fmt.format(i), dset_path, 0, 3) for i in range(2, 11)]
    found = list(bliss._iter_lima_images(filenames, start_index=2 * 3))
    assert expected == found


def test_iter_bliss_data(bliss_scan):
    for (
        index,
        data,
    ) in bliss.iter_bliss_data(bliss_scan, 2, "p3", ["diode1", "diode2"]):
        assert len(data) == 3
        assert data["diode1"] == index
        assert data["diode2"] == index
        assert (data["p3"] == index).all()
    assert index == 30
