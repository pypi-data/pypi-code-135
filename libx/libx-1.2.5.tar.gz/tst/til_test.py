import os
from pathlib import PosixPath
from libx.til import glue, lmap  # , spawn


from randomname import get_name


def test_glue():
    folder_name = get_name()
    _base_path = os.getcwd()
    try:
        resulting_path = glue(folder_name)
        assert resulting_path == PosixPath(f"{_base_path}/{folder_name}")
        print("test_glue passed")
    except Exception as e:
        print("test_glue failed with:")
        print(e)


def test_lmap():
    actual_res = [1, 4, 9, 16, 25, 36]

    sample_list = [1, 2, 3, 4, 5, 6]
    sample_func = lambda x: x * x

    try:
        res = lmap(sample_func, sample_list)
        assert res == actual_res
        print("test_lmap passed")
    except Exception as e:
        print("test_lmap failed with:")
        print(e)
