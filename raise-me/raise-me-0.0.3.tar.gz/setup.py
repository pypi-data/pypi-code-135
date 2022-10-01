# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raise_me',
 'raise_me.build',
 'raise_me.build.cloud',
 'raise_me.exceptions',
 'raise_me.identity',
 'raise_me.models',
 'raise_me.models.event',
 'raise_me.parser',
 'raise_me.parser.event',
 'raise_me.resources.aws.lambda.functions',
 'raise_me.util',
 'raise_me.util.gcp',
 'raise_me.wsk']

package_data = \
{'': ['*'],
 'raise_me': ['resources/aws/lambda/layers/*', 'resources/gcp/workflows/*']}

install_requires = \
['boto3>=1.24.50,<2.0.0',
 'cloudevents>=1.6.1,<2.0.0',
 'constructs>=10.1.85,<11.0.0',
 'pulumi-aws>=5.11.0,<6.0.0',
 'pulumi-gcp>=6.37.0,<7.0.0',
 'pulumi>=3.38.0,<4.0.0',
 'requests>=2.28.1,<3.0.0',
 'ruamel.yaml>=0.17.21,<0.18.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['raise = raise_me.app:app']}

setup_kwargs = {
    'name': 'raise-me',
    'version': '0.0.3',
    'description': 'Serverless event broker which allows connecting native cloud events (AWS & GCP) to targets declaratively.',
    'long_description': '\n# raise-me\nServerless event broker which allows connecting native cloud events to targets declaratively.\n- The native cloud **events** can be raised from either *AWS* or *GCP*.\n- The **targets** can be either *HTTP endpoints* or [*OpenWhisk Actions*](https://github.com/apache/openwhisk/blob/master/docs/actions.md).\n\n\n### Example\nDeclare your event defintions in `raise-events.yaml`:\n```yaml\nevents:\n\n  s3-to-cloudfunction: # Event\'s logical name.\n    source:\n      provider: aws\n      filters: # AWS EventBridge event patterns.\n        - \'source: ["aws.s3"]\'\n        - \'detail-type: ["Object Created"]\'\n        - \'detail: {"bucket": {"name": ["my-bucket-name"]}}\'\n    targets:\n      - http:\n          method: post # Sends event data in CloudEvents format.\n          url: my-cloudfunction-url\n      - action:\n          name: my-openwhisk-action-name\n\n  cloudstorage-to-lambda:\n    source:\n      provider: gcp\n      filters: # GCP Eventrac filters.\n        - \'type=google.cloud.audit.log.v1.written\'\n        - \'serviceName=storage.googleapis.com\'\n        - \'methodName=storage.objects.create\'\n    targets:\n      - http:\n          method: get\n          url: my-lambda-url\n```\n\n---\n\n## Introduction\nThis solution enables declarative native cloud event routing (e.g. AWS S3\'s "Object Created") to either HTTP endpoints or user-defined serverless functions deployed as [Apache OpenWhisk](https://openwhisk.apache.org/) Actions.\n\nAn example use case could be triggering a [GCP Cloud Function](https://cloud.google.com/functions) when a file is uploaded to an [AWS S3](https://aws.amazon.com/s3/) bucket.\nSuch process is accomplished by creating necessary cloud resources that will route the event to the OpenWhisk deployment, which will then receive the event\'s data in the [CloudEvents](https://cloudevents.io/) format and forward it to the Cloud Function through an API call.\n\n---\n\n## Table of Contents\n- [Motivation](#motivation)\n- [Requirements](#requirements)\n- [Configuration](#configuration)\n  - [Pulumi](#pulumi)\n  - [Enable Google Services](#enable-google-services)\n- [Installation](#installation)\n- [Testing](#testing)\n- [Usage](#usage)\n  - [1. Prepare Inputs](#1-prepare-inputs)\n  - [2. Create Resources](#2-create-resources)\n  - [3. Cleanup](#3-cleanup)\n- [Architecture](#architecture)\n- [Contriburing](#architecture)\n- [License](#architecture)\n- [Future Features](#future-features)\n\n---\n\n## Motivation\nThe implementation alternatives for the previous example (trigger Cloud Function from S3 event) are countless. A straightforward approach could be linking a Lambda to the event, which is fairly simple within the AWS ecosystem, and communicate with the Cloud Function from there.\n\nAlthough this alternative may seem initially as a good approach, there are several design limitations. If we were to trigger 2 Cloud functions instead of 1, we would have to deploy a new Lambda with code containing logic to reach both Cloud functions.\nWhat if we want to reach 100 endpoints from that single event? Lambdas have a 15-minute time limit on their execution, so extending this event-based communication solution would have limitations in terms of:\n- ***Extensibility** – the number of endpoints would be limited by Lambda. Perhaps, we would have to create more Lambdas to handle different endpoints.*\n- ***Maintainability** – the logic at the Lambda layer might require frequent changes.*\n- ***Complexity** – the logic at the Lambda layer will increase.*\n- ***Portability** – this schema would only work for native AWS events, but not for other clouds, such as GCP.*\n\nThe solution that **raise-me** provides addresses all of these limitations by using serverless services and an abstraction layer that simplifies the management of the required infrastrcture that makes the event routing possible.\n\n---\n\n## Requirements\n- [Apache OpenWhisk](https://openwhisk.apache.org/) deployment - *where the event processors run; OpenWhisk has several [deployment options](https://openwhisk.apache.org/documentation.html#openwhisk_deployment), including Kubernetes.*\n- [Pulumi](https://www.pulumi.com/) - *used to create cloud resources.*\n- AWS Account & [AWS CLI](https://aws.amazon.com/cli/) - *optional, if AWS events are to be listened.*\n- GCP Account - *optional, if GCP events are to be listened.*\n\n---\n\n## Configuration\n#### Pulumi\n[Configure Pulumi to access your AWS account](https://www.pulumi.com/docs/get-started/aws/begin/) and/or [Google Cloud account](https://www.pulumi.com/docs/get-started/gcp/begin/). If you are just interested in one of those event sources, you can ignore the other.\n\nCreate a Pulumi project. You can use either a Python template, AWS or GCP. For example:\n```bash\n$ mikdir your-project-name\n$ pulumi new aws-python\n```\n\nActivate your pulumi project\'s virtual environment and install `raise-me` (available on PyPi):\n```bash\n$ source ./venv/bin/activate\n$ ./venv/bin/python.exe -m pip install raise-me\n```\n\nIn `Pulumi.<stack-name>.yaml`, make sure you have the appropriate configuration for the corresponding clouds:\n```yaml\nconfig:\n  aws:region: your-target-region\n  gcp:project: your-project-id\n```\n\nIn your `__main__.py` Pulumi file, include the code that will create the cloud resources for you:\n```python\nfrom raise_me.build import CloudBuilder\n\nbuilder = CloudBuilder(config_path=\'path/to/raise-config.yaml\')\nbuilder.update_stack(events_path=\'path/to/raise-events.yaml\')\n```\n\n\n#### Enable Google Services\nEnable the following Google services:\n- [Eventrac](https://cloud.google.com/eventarc/docs/overview) - _eventrac triggers will be created._\n- [PubSub](https://cloud.google.com/pubsub) - _used internally by Eventrac._\n- [Workflows](https://cloud.google.com/workflows) - _workflows will be created._\n- [Cloud Logging](https://cloud.google.com/logging) - _provides more event options._\n\nIf you are interested in handling events from services that log into Cloud Logging, [enable the logging of those services](https://cloud.google.com/logging/docs/audit/configure-data-access#config-console). \n\n---\n\n## Installation\nRun (available on PyPi):\n```bash\n$ pip install raise-me\n```\nVerify installation:\n```bash\n$ raise --help\n```\n\n---\n\n## Testing\nInstall [Poetry](https://python-poetry.org/) if you don\'t have it already:\n```bash\n$ pip install poetry\n```\n\nClone the repository, create a virtual environment at the project level and activate it:\n```bash\n$ python3 -m venv my-venv\n$ source my-venv/bin/activate \n```\n\nInstall project dependencies using Poetry:\n```bash\n$ poetry install\n```\n\nModify the `tests/raise-config.yaml` and provide the connection details of the target OpenWhisk deployment (see [Usage](#usage) for more details). You can also modify the contents of `tests/raise-events.yaml`, but it is not necessary for these tests.\n\nAfter this, you can run the following integration tests that verify that the connection with the OpenWhisk deployment is successful:\n```bash\n$ pytest -v -m client # Tests OpenWhisk API client.\n$ pytest -v -m paginator # Tests paginator interface using the API client.\n$ pytest -v -m builder # Tests creation/destruction of raise-me OpenWhisk resources.\n```\n\n---\n\n## Usage\n\n#### 1. Prepare Inputs\nThere are 2 required inputs, namely `raise-config.yaml` and `raise-events.yaml`.\n\nThe `raise-config.yaml` file contains configuration settings that allow connecting to the OpenWhisk deployment and creating cloud resources. *(The auth field in the example contains default values for a basic unchanged OpenWhisk deployment.)*\n\n```yaml\nopenwhisk:\n  namespace: guest # Storage location of Openwhisk resources.\n  endpoint: https://my-endpoint:443 # Openwhisk deployment endpoint.\n  auth: # Authentication for REST API.\n    username: 23bc46b1-71f6-4ed5-8c54-816aa4f8c502\n    password: 123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP\n\ngcp: # Used for cloud resource creation.\n  project-id: my-project-id\n  region: my-region # Should match pulumi config.\n```\n\nThe `raise-events.yaml` will contain the event definitions. Each event definition is composed by a Source and a list of Targets.\nTo specify the desired events, we use each cloud\'s selection strategy; event patterns for AWS and Eventrac filters for GCP.\n\n```yaml\nevents:\n\n  s3-to-cloudfunction: # Your event\'s logical name.\n    source:\n      provider: aws\n      filters: # AWS EventBridge event patterns.\n        - \'source: ["aws.s3"]\'\n        - \'detail-type: ["Object Created"]\'\n        - \'detail: {"bucket": {"name": ["my-bucket-name"]}}\'\n    targets:\n      - http:\n          method: post # Sends event data in CloudEvents format.\n          url: my-cloudfunction-url\n      - action:\n          name: my-openwhisk-action-name\n\n  cloudstorage-to-lambda:\n    source:\n      provider: gcp\n      filters: # GCP Eventrac filters.\n        - \'type=google.cloud.audit.log.v1.written\'\n        - \'serviceName=storage.googleapis.com\'\n        - \'methodName=storage.objects.create\'\n    targets:\n      - http:\n          method: get\n          url: my-lambda-url\n```\n\n_Notes on the `raise-events.yaml`:_\n* _Each event definition must have only 1 `provider` and at least 1 target._\n* _The providers available are `aws` and `gcp`._\n* _Targets available include `http` and `action`._\n* _`http` targets must contain `method` and a `url`. Current available methods are `get` and `post`, where the later sends the event\'s data to the target._\n* _`action` targets must contain the `name` of the OpenWhisk action to trigger, which should be available within the namespace specified in the `raise-config.yaml`._\n* _OpenWhisk Actions are language-agnostic, so if you need more advanced event-handling logic, you can deploy your own actions and link them to the one or more events seamlessly!_\n\n\n#### 2. Create Resources\nOnce having the inputs ready, we just need to create:\n- Cloud resources that will route the events to our OpenWhisk deployment.\n- OpenWhisk resources that will handle the incoming events.\n\nCreate the OpenWhisk resources using the `raise` command:\n```bash\n$ raise up --config-path path/to/raise-config.yaml --events-path path/to/raise-events.yaml\n```\n\nCreate the cloud resources with Pulumi as you usually would:\n```bash\n~/pulumi/project/$ pulumi up \n```\n\nAnd done! You should have now the required infrastructure in place to route the specified events to their corresponding targets.\n\n\n#### 3. Cleanup\nTo delete the OpenWhisk resources created by **raise-me**, run:\n```bash\n$ raise destroy --config-path path/to/raise-config.yaml\n```\n\nDelete the cloud resources running:\n```bash\n~/pulumi/project/$ pulumi destroy\n```\n\n---\n\n### Architecture\nLet\'s consider the example given in the introduction and an OpenWhisk deployment in [AWS EKS](https://aws.amazon.com/eks/).\n\nTo forward S3 events to OpenWhisk, **raise-me** uses [AWS EventBridge](https://aws.amazon.com/eventbridge/). It creates an [EventRule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) that routes the event to a [Lambda](https://aws.amazon.com/lambda/) function that parses the event and forwards it to the OpenWhisk deployment by firing an [OpenWhisk Trigger](https://github.com/apache/openwhisk/blob/master/docs/triggers_rules.md#creating-triggers-and-rules). Such Trigger will then invoke the necessary Actions to reach the Cloud Function\'s endpoint.\n\n![Architecture](images/architecture-example-aws.PNG)\n\n_Note that:_\n- _The services used to route the events to our target, namely *EventBridge*, *Lambda* and *OpenWhisk*, are serverless and can scale seamlessly._\n- _The dotted arrows represent AWS managed communication, whereas the solid lines represent REST API calls implemented in the solution._\n- _Although OpenWhisk implements internal load balancing, a deployment in EKS will also include an Elastic Load Balancer ([docs](https://github.com/apache/openwhisk-deploy-kube/blob/master/docs/k8s-aws.md)). This component is omitted in the diagram as it is AWS-specific._\n\nConsidering the same OpenWhisk deployment, let\'s say that we would like to trigger a Lambda function when a file is uploaded to a Cloud Storage bucket. The architecture would look as follows:\n\n![Architecture](images/architecture-example-google.PNG)\n\n---\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss the change.\n\nPlease ensure tests are up to date.\n\n---\n\n## License\n[MIT](License)\n\n-----\n\n## Future Features\n- [ ] Thorough exception handling\n- [ ] Secure OpenWhisk API credentials\n  - [ ] AWS: SecretsManager\n  - [ ] GCP: SecretManager\n- [ ] Http request body/parameters\n- [ ] Internal API crendential storage (for HTTP targets)\n- [ ] Logging',
    'author': 'Fernando Ancona',
    'author_email': 'f.anconac@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ferancona/raise-me',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
