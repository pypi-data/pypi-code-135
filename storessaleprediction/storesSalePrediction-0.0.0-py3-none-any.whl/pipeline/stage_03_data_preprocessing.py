from saleStorePredictor.config import ConfigurationManager
from saleStorePredictor.components import DataTransformation
from saleStorePredictor import logger

STAGE_NAME = "Data preprocessing stage"

def main():
    config = ConfigurationManager()
    config = config.get_data_transformation_config()
    trans = DataTransformation(config)
    trans.initiate_data_transformation()





if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e