from dataclasses import dataclass
from typing import Dict, List

from beam.base import BaseDataClass
from beam.types import OutputType, PythonVersion, Types


@dataclass()
class AppSpecConfiguration(BaseDataClass):
    name: str
    cpu: str
    gpu: int
    memory: str
    apt_install: PythonVersion
    python_version: List[str]
    python_packages: List[str]
    workspace: str


@dataclass
class WebhookConfiguration(BaseDataClass):
    inputs: Dict[str, Types]
    handler: str
    trigger_type: str = "webhook"


@dataclass
class CronJobConfiguration(BaseDataClass):
    inputs: Dict[str, Types]
    cron_schedule: str
    handler: str
    trigger_type: str = "cron_job"


@dataclass
class RestAPIConfiguration(BaseDataClass):
    inputs: Dict[str, Types]
    outputs: Dict[str, Types]
    handler: str
    trigger_type: str = "rest_api"


@dataclass
class FileConfiguration(BaseDataClass):
    path: str
    name: str
    output_type: OutputType
