import pytest
from time import time
import os
import shutil

from devpytools import Cacher, getCacher, FileCacheProvider
from devpytools.cacher.cacher import CACHER_MAP

TMP_DIR_PATH = f'./tmp{int(time())}'


@pytest.fixture()
def inmemResourceSetup(request):
    os.mkdir(TMP_DIR_PATH)

    def resource_teardown():
        c = CACHER_MAP[None]
        CACHER_MAP.clear()
        CACHER_MAP[None] = c
        shutil.rmtree(TMP_DIR_PATH)
    request.addfinalizer(resource_teardown)


@pytest.fixture()
def fileResourceSetup(request):
    os.mkdir(TMP_DIR_PATH)

    def resource_teardown():
        c = CACHER_MAP[None]
        CACHER_MAP.clear()
        CACHER_MAP[None] = c
        shutil.rmtree(TMP_DIR_PATH)
    request.addfinalizer(resource_teardown)


def countFiles(path=TMP_DIR_PATH):
    return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])



def test_base(inmemResourceSetup):
    c = Cacher(name='test')
    var = 4

    @c.cache
    def a(a):
        return var
    assert a(1) == 4
    assert a(2) == 4
    var = 7
    assert a(1) == 4
    assert a(3) == 7


def test_fileBase(fileResourceSetup):
    c = Cacher(name='test', tmpDirPath=TMP_DIR_PATH)
    var = 4

    @c.cache
    def a(a):
        return var
    assert a(1) == 4
    assert a(2) == 4
    var = 7
    assert a(1) == 4
    assert a(3) == 7
    assert countFiles() != 0


def test_getCacher(inmemResourceSetup):
    c = getCacher()
    c1 = getCacher('test')
    c2 = getCacher('test')
    var = 4

    @c.cache
    def a(a):
        return var

    @c1.cache
    def a1(a):
        return var

    @c2.cache
    def a2(a):
        return var
    assert a(1) == 4
    assert a2(1) == 4
    var = 7
    assert a(1) == 4
    assert a1(2) == 7
    assert a2(1) == 4


def test_globalCachers(inmemResourceSetup):
    c = Cacher(name='test')
    with pytest.raises(ValueError):
        c = Cacher(name='test')


def test_uniqKey(inmemResourceSetup):
    c = Cacher(name='test')
    var = 4

    @c.cache
    def a(a):
        return var

    @c.cache(uniqueKey=lambda *a, **b: 'True')
    def a1(a):
        return var
    assert a(1) == 4
    assert a1(1) == 4
    var = 7
    assert a(2) == 7
    assert a1(2) == 4


def test_uniqKeyArgs(inmemResourceSetup):
    c = Cacher(name='test')
    var = 4

    @c.cache(uniqueKey=lambda args: args["a"]+args['b'])
    def a1(a, b):
        return var
    assert a1(1, b=2) == 4
    var = 7
    assert a1(2, b=1) == 4


def test_expired(inmemResourceSetup):
    c = Cacher(name='test', isExpired=lambda x, y: True)
    var = 4

    @c.cache
    def a(a):
        return var
    assert a(1) == 4
    var = 7
    assert a(2) == 7


def test_expiredArgs(inmemResourceSetup):
    c = Cacher(name='test', isExpired=lambda x, y: time() > x and y == 4)
    var = 4

    @c.cache
    def a(a):
        return var
    assert a(1) == 4
    var = 7
    assert a(2) == 7


def test_enabled(inmemResourceSetup):
    c = Cacher(name='test', isEnable=False)
    var = 4

    @c.cache
    def a(a):
        return var
    assert a(1) == 4
    var = 7
    assert a(1) == 7


def test_cacheProvider(inmemResourceSetup):
    class Ctest:
        def getData(self, hsh, func, *args, **kwargs):
            return 5

        def setData(self, hsh, func, data, *args, **kwargs):
            return 5

    c = Cacher(name='test', cacheProvider=Ctest())  # type: ignore
    var = 4

    @c.cache
    def a(a):
        return var
    assert a(1) == 5


def test_expireExtensions(inmemResourceSetup, monkeypatch):
    import time
    tm = time.time()

    def monkeyTime():
        return tm
    from devpytools.cacher import extensions
    monkeypatch.setattr(extensions, "time", monkeyTime)
    c = Cacher(name='test', isExpired=extensions.expireAfterMinutes(1))
    var = 4

    @c.cache
    def a(a):
        return var
    assert a(1) == 4
    var = 7
    assert a(1) == 4
    tm += 61
    assert a(1) == 7


def test_version(inmemResourceSetup):
    c1 = Cacher(name='test1', tmpDirPath=TMP_DIR_PATH, version=1)
    c2 = Cacher(name='test2', tmpDirPath=TMP_DIR_PATH, version=2)
    c3 = Cacher(name='test3', tmpDirPath=TMP_DIR_PATH, version=1)
    var = 4

    @c1.cache
    def a(a):  # type: ignore
        return var
    a1 = a

    @c2.cache
    def a(a):  # type: ignore
        return var
    a2 = a

    @c3.cache
    def a(a):
        return var
    a3 = a
    assert a1(1) == 4
    var = 7
    assert a2(1) == 7

    assert a1(1) == 4
    assert a1(1) == a3(1)
    var = 4
    assert a2(1) == 7
