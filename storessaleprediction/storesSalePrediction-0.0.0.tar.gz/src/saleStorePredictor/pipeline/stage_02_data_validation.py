from saleStorePredictor.config import ConfigurationManager
from saleStorePredictor.components import DataValidation
from saleStorePredictor import logger

STAGE_NAME = "Data Validation stage"

def main():
    config_manager = ConfigurationManager()
    config = config_manager.get_data_validation_config()
    ingestion_artifact = config_manager.get_data_ingestion_artifact()
    data_validation = DataValidation(config,ingestion_artifact)
    data_validation.validate_schema()
    data_validation.remove_duplicates()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e