import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post190"
version_tuple = (0, 5, 0, 190)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post190")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post48"
data_version_tuple = (0, 5, 0, 48)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post48")
except ImportError:
    pass
data_git_hash = "b042f3b29d06735da1b60ea646c3f16cebe23a6b"
data_git_describe = "0.5.0-48-gb042f3b2"
data_git_msg = """\
commit b042f3b29d06735da1b60ea646c3f16cebe23a6b
Merge: 689a1184 74921041
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Mon Oct 3 14:17:56 2022 +0200

    Merge pull request #680 from Silabs-ArjanB/ArjanB_clic1
    
    Updates according to latest Smclic specification

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
