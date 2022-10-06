from .auto_install.health_checks.report import check_health, list_remote_licenses, list_local_licenses
from .utils.sparksession_utils import start
from .auto_install.install_flow import install
# get helpers into global space
from johnsnowlabs import medical, nlp, ocr, settings, viz, finance, legal
import johnsnowlabs as jsl

# databricks
from johnsnowlabs.auto_install.databricks.work_utils import run_local_py_script_as_task

# from johnsnowlabs.auto_install.databricks.install_utils import create_cluster, get_db_client_for_token, \
#     install_jsl_suite_to_cluster
#
# from .py_models import jsl_secrets
# from .py_models.install_info import InstallFolder
# from .py_models.jsl_secrets import LicenseInfos, JslSecrets

# Input validation enums for typing the functions
# from johnsnowlabs.utils.enums import ProductName, PyInstallTypes, JvmHardwareTarget

from johnsnowlabs.nlp import *


# from johnsnowlabs.medical import *
# from johnsnowlabs.ocr import *
# from johnsnowlabs.finance import *


def new_version_online():
    from .utils.pip_utils import get_latest_lib_version_on_pypi
    # we are outdated, if current version does not match the latest on PypPi
    return settings.raw_version_jsl_lib != get_latest_lib_version_on_pypi('jsl_tmp')


from typing import Dict, Optional, Union,Callable

from types import ModuleType


def run_in_databricks(
        py_script_path: Union[str,ModuleType, Callable],
        databricks_cluster_id: Optional[str] = None,
        databricks_token: Optional[str] = None,
        databricks_host: Optional[str] = None,
        run_name: str = None,
        databricks_password: Optional[str] = None,
        databricks_email: Optional[str] = None,
):
    from johnsnowlabs.auto_install.databricks.install_utils import create_cluster, get_db_client_for_token
    db_client = get_db_client_for_token(databricks_host, databricks_token)
    return run_local_py_script_as_task(db_client, py_script_path, cluster_id=databricks_cluster_id, run_name=run_name)




