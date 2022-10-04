import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post196"
version_tuple = (0, 5, 0, 196)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post196")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post54"
data_version_tuple = (0, 5, 0, 54)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post54")
except ImportError:
    pass
data_git_hash = "789a0c13941bb747bb13789e9be583daa635ece2"
data_git_describe = "0.5.0-54-g789a0c13"
data_git_msg = """\
commit 789a0c13941bb747bb13789e9be583daa635ece2
Merge: ac236895 3bd95e88
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Oct 4 09:12:05 2022 +0200

    Merge pull request #682 from silabs-oysteink/silabs-oysteink_clic-ptr-wb_valid
    
    Fix for issue #497

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
