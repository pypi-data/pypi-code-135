from typing import Any, Optional

from phidata.constants import AWS_REGION_ENV_VAR, AWS_PROFILE_ENV_VAR
from phidata.infra.base.resource import InfraResource
from phidata.infra.aws.api_client import AwsApiClient
from phidata.utils.cli_console import print_info, print_error
from phidata.utils.log import logger


class AwsObject(InfraResource):
    """Base class for Aws Objects"""

    aws_region: Optional[str] = None
    aws_profile: Optional[str] = None

    aws_client: Optional[AwsApiClient] = None

    def get_aws_region(self) -> Optional[str]:
        # use value if provided
        if self.aws_region:
            return self.aws_region

        # get from env if not provided
        # logger.info(f"Loading {AWS_REGION_ENV_VAR} from env")
        import os

        aws_region_env = os.getenv(AWS_REGION_ENV_VAR)
        # logger.info(f"{AWS_REGION_ENV_VAR}: {aws_region_env}")
        if aws_region_env is not None:
            self.aws_region = aws_region_env
        return self.aws_region

    def get_aws_profile(self) -> Optional[str]:
        # use value if provided
        if self.aws_profile:
            return self.aws_profile

        # get from env if not provided
        # logger.info(f"Loading {AWS_PROFILE_ENV_VAR} from env")
        import os

        aws_profile_env = os.getenv(AWS_PROFILE_ENV_VAR)
        # logger.info(f"{AWS_PROFILE_ENV_VAR}: {aws_profile_env}")
        if aws_profile_env is not None:
            self.aws_profile = aws_profile_env
        return self.aws_profile

    def get_aws_client(self) -> AwsApiClient:
        if self.aws_client is not None:
            return self.aws_client
        self.aws_client = AwsApiClient(
            aws_region=self.get_aws_region(), aws_profile=self.get_aws_profile()
        )
        return self.aws_client


class AwsResource(AwsObject):
    """Base class for Aws Resources"""

    service_name: str
    service_client: Optional[Any] = None
    service_resource: Optional[Any] = None

    resource_available: bool = False
    resource_updated: bool = False
    resource_deleted: bool = False

    def is_valid(self) -> bool:
        # SubResources can use this function to add validation checks
        return True

    def get_service_client(self, aws_client: AwsApiClient):
        if self.service_client is None:
            self.service_client = aws_client.boto3_session.client(
                service_name=self.service_name, region_name=aws_client.aws_region
            )
        return self.service_client

    def get_service_resource(self, aws_client: AwsApiClient):
        if self.service_resource is None:
            self.service_resource = aws_client.boto3_session.resource(
                service_name=self.service_name, region_name=aws_client.aws_region
            )
        return self.service_resource

    def _create(self, aws_client: AwsApiClient) -> bool:
        logger.error(f"@_create method not defined for {self.__class__.__name__}")
        return False

    def create(self, aws_client: Optional[AwsApiClient] = None) -> bool:
        """Creates the resource on the Aws Cluster

        Args:
            aws_client: The AwsApiClient for the current Cluster
        """
        if not self.is_valid():
            return False
        # Skip resource creation if skip_create = True
        if self.skip_create:
            print_info(f"Skipping create: {self.get_resource_name()}")
            return True

        client: AwsApiClient = aws_client or self.get_aws_client()
        if self.use_cache and self.is_active(client):
            self.resource_available = True
            print_info(
                f"{self.get_resource_type()}: {self.get_resource_name()} already active."
            )
        else:
            self.resource_available = self._create(client)
        if self.resource_available:
            # print_info(
            #     f"Running post-create steps for {self.get_resource_type()}: {self.get_resource_name()}."
            # )
            return self.post_create(client)
        return self.resource_available

    def post_create(self, aws_client: AwsApiClient) -> bool:
        # return True because this function is not used for most resources
        return True

    def _read(self, aws_client: AwsApiClient) -> Any:
        logger.error(f"@_read method not defined for {self.__class__.__name__}")
        return False

    def read(self, aws_client: Optional[AwsApiClient] = None) -> Any:
        """Reads the resource from the Aws Cluster

        Args:
            aws_client: The AwsApiClient for the current Cluster
        """
        if not self.is_valid():
            return None
        if self.use_cache and self.active_resource is not None:
            return self.active_resource

        client: AwsApiClient = aws_client or self.get_aws_client()
        return self._read(client)

    def _update(self, aws_client: AwsApiClient) -> Any:
        logger.error(f"@_update method not defined for {self.__class__.__name__}")
        return False

    def update(self, aws_client: Optional[AwsApiClient] = None) -> bool:
        """Updates the resource on the Aws Cluster

        Args:
            aws_client: The AwsApiClient for the current Cluster
        """
        if not self.is_valid():
            return False
        # Skip resource creation if update = True
        if self.skip_update:
            print_info(f"Skipping update: {self.get_resource_name()}")
            return True

        client: AwsApiClient = aws_client or self.get_aws_client()
        if self.is_active(client):
            self.resource_updated = self._update(client)
        else:
            print_info(
                f"{self.get_resource_type()}: {self.get_resource_name()} does not exist."
            )
            return True
        if self.resource_updated:
            # print_info(
            #     f"Running post-update steps for {self.get_resource_type()}: {self.get_resource_name()}."
            # )
            return self.post_update(client)
        return self.resource_updated

    def post_update(self, aws_client: AwsApiClient) -> bool:
        # return True because this function is not used for most resources
        return True

    def _delete(self, aws_client: AwsApiClient) -> Any:
        logger.error(f"@_delete method not defined for {self.__class__.__name__}")
        return False

    def delete(self, aws_client: Optional[AwsApiClient] = None) -> bool:
        """Deletes the resource from the Aws Cluster

        Args:
            aws_client: The AwsApiClient for the current Cluster
        """
        if not self.is_valid():
            return False
        # Skip resource deletion if skip_delete = True
        if self.skip_delete:
            print_info(f"Skipping delete: {self.get_resource_name()}")
            return True

        client: AwsApiClient = aws_client or self.get_aws_client()
        if self.is_active(client):
            self.resource_deleted = self._delete(client)
        else:
            print_info(
                f"{self.get_resource_type()}: {self.get_resource_name()} does not exist."
            )
            return True
        if self.resource_deleted:
            # print_info(
            #     f"Running post-delete steps for {self.get_resource_type()}: {self.get_resource_name()}."
            # )
            return self.post_delete(client)
        return self.resource_deleted

    def post_delete(self, aws_client: AwsApiClient) -> bool:
        # return True because this function is not used for most resources
        return True

    def is_active(self, aws_client: AwsApiClient) -> bool:
        """Returns True if the resource is active on the Aws Cluster"""
        active_resource = self.read(aws_client=aws_client)
        if active_resource is not None:
            return True
        return False
