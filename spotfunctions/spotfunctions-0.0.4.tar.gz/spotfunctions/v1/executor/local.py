from spotfunctions.v1.executor.executor import Executor
from spotfunctions.v1.executor.configs import AppConfig
import logging

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Local SpotFunction starting")
    app_config = AppConfig("function.json")
    logger.info("Function configuration has been read successfully.")
    executor = Executor(app_config)
    logger.info("Starting executor.")
    executor.run()
