import asyncio
from machine_learning.training.abstractions.batch_training_plugin import *
from machine_learning.evaluation.abstractions.evaluation_service import *
from typing import *

class PostValidationPlugin(Generic[TInput, TTarget, TModel]):
    @abstractmethod
    def post_validation(self, logger: Logger, training_context: TrainingContext[TInput, TTarget, TModel], validation_result: EVALUATION_RESULT):
        pass

class PreValidationPlugin(Generic[TInput, TTarget, TModel]):
    @abstractmethod
    def pre_validation(self, logger: Logger, training_context: TrainingContext[TInput, TTarget, TModel]):
        pass

VALIDATION_PLUGINS = Union[PreValidationPlugin, PostValidationPlugin]

class ValidationPlugin(PostEpoch[TInput, TTarget, TModel]):
    def __init__(self, evaluation_service: EvaluationService[TInput, TTarget, TModel], validation_datasets: EVALUATION_DATASET, validation_metrics: EVALUATION_METRICS, event_loop: asyncio.AbstractEventLoop = None, plugins: Dict[str, VALIDATION_PLUGINS] = {}):
        if evaluation_service == None:
            raise ValueError('evaluaiton_service')

        if validation_datasets == None:
            raise ValueError('validation_datasets')

        self.__evaluation_service: EvaluationService[TInput, TTarget, TModel] = evaluation_service
        self.__validation_datasets: EVALUATION_DATASET = validation_datasets
        self.__validation_metrics: EVALUATION_METRICS = validation_metrics
        self.__event_loop: asyncio.AbstractEventLoop = event_loop if event_loop != None else asyncio.get_event_loop()

        self.__pre_validation_plugins: Dict[str, PreValidationPlugin[TInput, TTarget, TModel]] = dict(filter(lambda plugin: isinstance(plugin[1], PreValidationPlugin), plugins.items()))
        self.__post_validation_plugins: Dict[str, PostValidationPlugin[TInput, TTarget, TModel]] = dict(filter(lambda plugin: isinstance(plugin[1], PostValidationPlugin), plugins.items()))

    def __execute_pre_validation_plugins(self, logger: Logger, context: TrainingContext[TInput, TTarget, TModel]):
        logger.debug("Executing pre validation plugins...")
        for name, plugin in self.__pre_validation_plugins.items():
            logger.debug(f"Executing plugin with name {name}...")
            plugin.pre_validation(logger, context)

    def __execute_post_validation_plugins(self, logger: Logger, context: TrainingContext[TInput, TTarget, TModel], validation_result: EVALUATION_RESULT):
        logger.debug("Executing post validation plugins...")
        for name, plugin in self.__post_validation_plugins.items():
            logger.debug(f"Executing plugin with name {name}...")
            plugin.post_validation(logger, context, validation_result)

    def post_epoch(self, logger: Logger, trainingContext: TrainingContext[TInput, TTarget, TModel]):
        logger.info("Validating current model.")
        self.__execute_pre_validation_plugins(logger, trainingContext)
        validation_result: EVALUATION_RESULT = self.__event_loop.run_until_complete(self.__evaluation_service.evaluate(model=trainingContext.model, evaluation_dataset=self.__validation_datasets, evaluation_metrics=self.__validation_metrics, logger=logger))
        self.__execute_post_validation_plugins(logger, trainingContext, validation_result)
        logger.info("finished validation of current model.")

