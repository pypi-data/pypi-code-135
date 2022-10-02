# /usr/bin/python3
from cicd import config
from cicd.util import node_util
from cicd.util import docker_util
from cicd.util import aws_util
from cicd.archetype import IArchetype
from cicd.util import terraform_util
from cicd.util import helm_util


class StoreBackend(IArchetype):

    def deps(self):
        aws_util.deps()
        terraform_util.deps()
        helm_util.deps()

    def build(self):
        version = node_util.get_version()
        docker_util.build(
            [],
            '.',
            [f"{self.application_name}:{version}", f"{self.application_name}:latest"],
            'Dockerfile'
        )

    def publish(self, lifecycle: str):
        version = node_util.get_version()
        repository = aws_util.ensure_repository(self.application_name, lifecycle)

        aws_util.ecr_login(self.application_name, lifecycle)
        repository_uri = repository['repositoryUri']
        source_image = f"{self.application_name}:{version}"
        docker_util.tag(source_image, f"{repository_uri}:{version}")
        docker_util.tag(source_image, f"{repository_uri}:latest")

        docker_util.push([
            f"{repository_uri}:{version}",
            f"{repository_uri}:latest",
        ])

    def deploy(self, resource: str, lifecycle: str):
        version = node_util.get_version()
        if 'application' == resource:
            if config.EKS_CLUSTER_NAME:
                aws_util.update_kubeconfig(config.EKS_CLUSTER_NAME)
            common_opts = [
                '--set', f"deployment.env.DYNAMODB_TABLE_NAME=store-backend-{lifecycle}",
                '--set', f"deployment.env.SQS_QUEUE_NAME=store-backend-{lifecycle}",
                '--set', f"deployment.env.SERVER_URL=https://store-backend.{lifecycle}.pago.dev",
                '--set-string', f"deployment.env.AWS_ACCOUNT_ID={aws_util.get_aws_account_id()}",
                '--set', 'deployment.env.SQS_ENDPOINT=https://sqs.us-east-2.amazonaws.com',
                '--set', 'deployment.env.AWS_REGION=us-east-2',
            ]
            helm_util.update_repo()
            helm_util.deploy(
                f"{self.application_name}-api",
                lifecycle,
                version,
                'pago/dropwizard',
                opts=[
                    '--set', 'deployment.env.SERVICE=api',
                    '--set', f"application_name={self.application_name}-api",
                    *common_opts
                ],
                image=self.application_name
            )
            helm_util.deploy(
                f"{self.application_name}-payments",
                lifecycle,
                version,
                'pago/dropwizard',
                opts=[
                    '--set', 'deployment.env.SERVICE=payments',
                    '--set', 'ingress=null',
                    *common_opts
                ],
                image=self.application_name
            )
            helm_util.deploy(
                f"{self.application_name}-batch",
                lifecycle,
                version,
                'pago/cronjob',
                opts=[
                    '--set', 'deployment.env.SERVICE=batch',
                    '--set', 'deployment.schedule="0/10 * * * *"',
                    *common_opts
                ],
                image=self.application_name
            )
        else:
            terraform_util.init(self.application_name, lifecycle, resource)
            terraform_util.apply(self.application_name, lifecycle, resource)

    def undeploy(self, resource: str, lifecycle: str):
        if 'application' == resource:
            if config.EKS_CLUSTER_NAME:
                aws_util.update_kubeconfig(config.EKS_CLUSTER_NAME)
            helm_util.update_repo()
            helm_util.delete(f"{self.application_name}-api", lifecycle)
            helm_util.delete(f"{self.application_name}-payments", lifecycle)
            helm_util.delete(f"{self.application_name}-batch", lifecycle)
        else:
            terraform_util.init(self.application_name, lifecycle, resource)
            terraform_util.destroy(self.application_name, lifecycle, resource)
