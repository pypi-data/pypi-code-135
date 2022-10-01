from saleStorePredictor.config import ConfigurationManager
from saleStorePredictor.components import ModelTrainer
from saleStorePredictor import logger


STAGE_NAME = "Model training stage"

def main():
    config = ConfigurationManager()
    model_trainer_config = config.get_data_model_trainer_config()
    transformation_artifact = config.get_data_transformation_artifact()

    model_traner = ModelTrainer(model_trainer_config, transformation_artifact)
    model_traner.initiate_model_trainer()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e