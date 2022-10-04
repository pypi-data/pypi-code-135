import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post198"
version_tuple = (0, 5, 0, 198)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post198")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post56"
data_version_tuple = (0, 5, 0, 56)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post56")
except ImportError:
    pass
data_git_hash = "c87e2a97cd55d269bf99d65c7c84ab866729bfc7"
data_git_describe = "0.5.0-56-gc87e2a97"
data_git_msg = """\
commit c87e2a97cd55d269bf99d65c7c84ab866729bfc7
Merge: 789a0c13 2d0afd88
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Oct 4 10:13:51 2022 +0200

    Merge pull request #683 from silabs-oysteink/silabs-oysteink_rvfi-assert-fix
    
    Added missing clock and reset to rvfi assertion/property.

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
