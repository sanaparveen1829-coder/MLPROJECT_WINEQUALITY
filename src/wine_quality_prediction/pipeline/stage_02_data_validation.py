from wine_quality_prediction import logger
from wine_quality_prediction.config.configuration import ConfigurationManager
from wine_quality_prediction.entity.config_entity import DatavalidationConfig
from wine_quality_prediction.components.data_validation import Datavalidation


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=Datavalidation(config=data_validation_config)
        data_validation.validate_all_columns()
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

