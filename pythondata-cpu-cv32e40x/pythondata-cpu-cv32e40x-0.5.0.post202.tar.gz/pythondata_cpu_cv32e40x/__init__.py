import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post202"
version_tuple = (0, 5, 0, 202)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post202")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post60"
data_version_tuple = (0, 5, 0, 60)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post60")
except ImportError:
    pass
data_git_hash = "f17b92ad4e5f20110f5fffa34a81dbbc9574296a"
data_git_describe = "0.5.0-60-gf17b92ad"
data_git_msg = """\
commit f17b92ad4e5f20110f5fffa34a81dbbc9574296a
Merge: 025c9879 2b364d9a
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Mon Oct 10 14:27:55 2022 +0200

    Merge pull request #685 from Silabs-ArjanB/ArjanB_etnmi
    
    Removed non-existing etrigger.nmi field

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
