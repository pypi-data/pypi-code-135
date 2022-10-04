from pathlib import Path

from phidata.utils.env_var import env_var_is_true

# -*- Workspace settings

# Workspace name: used for naming cloud resources
ws_name: str = "aws-dp"
# Workspace git repo url: used to git-sync DAGs and Charts
ws_repo: str = "https://github.com/phidatahq/aws-dp.git"
# Path to the workspace directory
ws_dir_path: Path = Path(__file__).parent.resolve()
# Path to the root i.e. data platform directory
data_platform_dir_path: Path = ws_dir_path.parent

# -*- AWS settings

# Availability Zone for EbsVolumes
aws_az: str = "us-east-1a"
aws_region: str = "us-east-1"

# -*- Enable apps

pg_dbs_enabled: bool = env_var_is_true("PG_DBS_ENABLED", False)
superset_enabled: bool = env_var_is_true("SUPERSET_ENABLED", False)
jupyter_enabled: bool = env_var_is_true("JUPYTER_ENABLED", False)
airflow_enabled: bool = env_var_is_true("AIRFLOW_ENABLED", False)
databox_enabled: bool = env_var_is_true("DATABOX_ENABLED", False)
traefik_enabled: bool = env_var_is_true("TRAEFIK_ENABLED", False)
whoami_enabled: bool = env_var_is_true("WHOAMI_ENABLED", False)

# -*- Settings using environment variables

# When env var CACHE=True, phi will skip the create/delete of existing resources.
# So `CACHE=f phi [command]` can be used to recreate existing resources
# Example: `CACHE=f phi ws up --env dev --name airflow --type container`
#           will restart existing airflow containers.
use_cache: bool = env_var_is_true("CACHE", True)
