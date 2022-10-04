import typing_extensions

from data_repo_client.apis.tags import TagValues
from data_repo_client.apis.tags.data_repository_service_api import DataRepositoryServiceApi
from data_repo_client.apis.tags.configs_api import ConfigsApi
from data_repo_client.apis.tags.repository_api import RepositoryApi
from data_repo_client.apis.tags.datasets_api import DatasetsApi
from data_repo_client.apis.tags.jobs_api import JobsApi
from data_repo_client.apis.tags.profiles_api import ProfilesApi
from data_repo_client.apis.tags.resources_api import ResourcesApi
from data_repo_client.apis.tags.register_api import RegisterApi
from data_repo_client.apis.tags.snapshots_api import SnapshotsApi
from data_repo_client.apis.tags.search_api import SearchApi
from data_repo_client.apis.tags.upgrade_api import UpgradeApi
from data_repo_client.apis.tags.unauthenticated_api import UnauthenticatedApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DATA_REPOSITORY_SERVICE: DataRepositoryServiceApi,
        TagValues.CONFIGS: ConfigsApi,
        TagValues.REPOSITORY: RepositoryApi,
        TagValues.DATASETS: DatasetsApi,
        TagValues.JOBS: JobsApi,
        TagValues.PROFILES: ProfilesApi,
        TagValues.RESOURCES: ResourcesApi,
        TagValues.REGISTER: RegisterApi,
        TagValues.SNAPSHOTS: SnapshotsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.UPGRADE: UpgradeApi,
        TagValues.UNAUTHENTICATED: UnauthenticatedApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DATA_REPOSITORY_SERVICE: DataRepositoryServiceApi,
        TagValues.CONFIGS: ConfigsApi,
        TagValues.REPOSITORY: RepositoryApi,
        TagValues.DATASETS: DatasetsApi,
        TagValues.JOBS: JobsApi,
        TagValues.PROFILES: ProfilesApi,
        TagValues.RESOURCES: ResourcesApi,
        TagValues.REGISTER: RegisterApi,
        TagValues.SNAPSHOTS: SnapshotsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.UPGRADE: UpgradeApi,
        TagValues.UNAUTHENTICATED: UnauthenticatedApi,
    }
)
