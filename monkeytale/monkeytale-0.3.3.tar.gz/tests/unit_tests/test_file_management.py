import monkeytale.file_management as mt_fm
import pytest
from hypothesis import example, given, settings
from hypothesis import strategies as st

je = mt_fm.MonkeytaleJSONEncoder()


class MyClass:
    pass


c = MyClass()

print(je.encode(c))
