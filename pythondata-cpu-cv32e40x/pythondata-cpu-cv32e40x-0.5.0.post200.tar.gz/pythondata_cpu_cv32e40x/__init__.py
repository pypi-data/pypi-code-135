import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post200"
version_tuple = (0, 5, 0, 200)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post200")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post58"
data_version_tuple = (0, 5, 0, 58)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post58")
except ImportError:
    pass
data_git_hash = "025c987917022f82b302f748586ab03324648c46"
data_git_describe = "0.5.0-58-g025c9879"
data_git_msg = """\
commit 025c987917022f82b302f748586ab03324648c46
Merge: c87e2a97 9f6e4daf
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Fri Oct 7 08:07:20 2022 +0200

    Merge pull request #684 from Silabs-ArjanB/ArjanB_pcs
    
    Simplified meaning of debug_pc_* interface

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
