from typing import Any, Dict, List

from beam.base import AbstractDataLoader, BaseConfiguration
from beam.dataclass import (
    CronJobConfiguration,
    RestAPIConfiguration,
    WebhookConfiguration,
)
from beam.serializer import BaseTriggerSerializer, CronJobTriggerSerializer
from beam.types import Types


class TriggerType:
    Webhook = "webhook"
    RestAPI = "rest_api"
    CronJob = "cron_job"


class Webhook(BaseConfiguration):
    def __init__(self, inputs: Dict[str, Types], handler: str) -> None:
        self.config = WebhookConfiguration(inputs=inputs, handler=handler)

        BaseTriggerSerializer().validate(self.config.to_dict(), raise_exception=True)


class CronJob(BaseConfiguration):
    def __init__(
        self, inputs: Dict[str, Types], cron_schedule: str, handler: str
    ) -> None:
        self.config = CronJobConfiguration(
            inputs=inputs, cron_schedule=cron_schedule, handler=handler
        )

        CronJobTriggerSerializer().validate(self.config.to_dict(), raise_exception=True)


class RestAPI(BaseConfiguration):
    def __init__(
        self, inputs: Dict[str, Types], outputs: Dict[str, Types], handler: str
    ) -> None:
        self.config = RestAPIConfiguration(
            inputs=inputs, outputs=outputs, handler=handler
        )

        BaseTriggerSerializer().validate(self.config.to_dict(), raise_exception=True)


class TriggerManager(AbstractDataLoader):
    def __init__(self) -> None:
        self.webhooks: List[Webhook] = []
        self.cron_jobs: List[CronJob] = []
        self.rest_apis: List[RestAPI] = []

    def _validate_trigger_groupings(self):
        """
        NOTE: For the time being, the Beam APP can only accept one trigger during the alpha
        stages. Later we will allow multiple trigger types for webhooks (Slack, Twitter, etc)
        """
        triggers = self.webhooks + self.cron_jobs + self.rest_apis

        if len(triggers) > 1:
            raise ValueError("App can only have 1 trigger at a time")

    def Webhook(self, inputs: Dict[str, Types], handler: str):
        """
        Arguments:
            inputs: dictionary specifying how to serialize/deserialize input arguments
        """
        self.webhooks.append(Webhook(inputs=inputs, handler=handler))
        self._validate_trigger_groupings()

    def CronJob(self, inputs: Dict[str, Types], cron_schedule: str, handler: str):
        """
        Arguments:
            inputs: dictionary specifying how to serialize/deserialize input arguments
            cron_schedule: CRON string to indicate the schedule in which the job is to run
                - https://en.wikipedia.org/wiki/Cron
        """
        self.cron_jobs.append(
            CronJob(inputs=inputs, cron_schedule=cron_schedule, handler=handler),
        )
        self._validate_trigger_groupings()

    def RestAPI(
        self, inputs: Dict[str, Types], outputs: Dict[str, Types], handler: str
    ):
        """
        Arguments:
            inputs: dictionary specifying how to serialize/deserialize input arguments
            outputs: dictionary specifying how to serialize/deserialize return values
        """
        self.rest_apis.append(RestAPI(inputs=inputs, outputs=outputs, handler=handler))
        self._validate_trigger_groupings()

    def dumps(self):
        # To make this backwards compatible in the future after switching back to
        # multiple triggers, we will make this a list that currently will only have 1 trigger
        self._validate_trigger_groupings()
        triggers = []

        if len(self.webhooks) != 0:
            triggers.append(self.webhooks[0].dumps())
        elif len(self.cron_jobs) != 0:
            triggers.append(self.cron_jobs[0].dumps())
        elif len(self.rest_apis) != 0:
            triggers.append(self.rest_apis[0].dumps())

        return triggers

    def from_config(self, triggers):
        if triggers is None:
            return

        for t in triggers:
            trigger_type = t.get("trigger_type", "")

            del t["trigger_type"]

            if trigger_type == TriggerType.Webhook:
                self.Webhook(**t)
            elif trigger_type == TriggerType.CronJob:
                self.CronJob(**t)
            elif trigger_type == TriggerType.RestAPI:
                self.RestAPI(**t)
            else:
                raise ValueError(
                    f"Found an unknown trigger type in config: {trigger_type}"
                )
