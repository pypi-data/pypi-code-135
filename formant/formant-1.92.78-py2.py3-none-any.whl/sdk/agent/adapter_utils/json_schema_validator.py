from typing import Callable, Dict, Optional
import json
import jsonschema
import logging
from formant.sdk.agent.v1.client import Client as AgentClient

logging.basicConfig()


class JsonSchemaValidator:
    def __init__(
        self,
        client,  # type: AgentClient
        adapter_name,  # type: str
        update_adapter_config_callback,  # type: Callable[[Dict], None]
        logger=None,  # type: Optional[logging.Logger]
        logger_level=logging.INFO,  # type: int
    ):
        self._client = client
        self._adapter_name = adapter_name
        self._update_adapter_config_callback = update_adapter_config_callback
        if logger is None:
            logger = logging.getLogger(adapter_name)
            logger.setLevel(logger_level)
        self.logger = logger
        self._client.register_config_update_callback(self._update_adapter_config)
        self._update_adapter_config()

    def _update_adapter_config(self):
        # Load config from either the agent's json blob or the config.json file
        try:
            try:
                config_blob = json.loads(self._client.get_config_blob_data())
                self.logger.info("Loaded config from agent")
            except (json.decoder.JSONDecodeError, TypeError):
                # Otherwise, load from the config.json file shipped with the adapter
                with open("config.json") as f:
                    config_blob = json.loads(f.read())
                self.logger.info("Loaded config from config.json file")

            # Validate configuration based on schema
            with open("config_schema.json") as f:
                try:
                    self.config_schema = json.load(f)
                    self.logger.info(
                        "Loaded config schema from config_schema.json file"
                    )
                except json.decoder.JSONDecodeError:
                    self.logger.warn(
                        "Could not load config schema. Is the file valid json?"
                    )
                    raise Exception("config schema error")

            self.logger.info("Validating config...")

            try:
                adapter_config = config_blob.get(self._adapter_name, None)
                if adapter_config is None:
                    raise Exception("no key: %s in configuration" % self._adapter_name)
                jsonschema.validate(adapter_config, self.config_schema)
                self.logger.info("Validation succeeded")
                self._update_adapter_config_callback(adapter_config)
            except (
                jsonschema.ValidationError,
                jsonschema.SchemaError,
                jsonschema.FormatError,
                jsonschema.RefResolutionError,
            ) as e:
                self.logger.warn("Validation failed %s: %s", type(e).__name__, str(e))

        except Exception as e:
            self.logger.warn("Failed to load config: %s" % str(e))
            self._client.create_event(
                "%s configuration loading failed: %s." % (self._adapter_name, str(e)),
                notify=False,
                severity="warning",
            )
