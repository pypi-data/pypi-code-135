import importlib
from random import randint
import logging
from logging.config import dictConfig
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import neptune.new as neptune
from neptune.new.types import File
from neptune.new.integrations.python_logger import NeptuneHandler
import mlflow
from  mlflow.tracking import MlflowClient
import pickle, warnings, toml
from dynaconf import settings
import site
path = site.getsitepackages()[0]

class SPDLogger(object):
    def __init__(self, *args, **kwargs):
        settings.load_file(path="{}/spdlogger/config/settings.toml".format(path))
        settings.load_file(path="{}/spdlogger/config/.secrets.toml".format(path))
        if kwargs=={}: pass  
        elif list(kwargs)[0]=="config": 
            settings.load_file(path=kwargs.get("config"))     
        # elif list(kwargs)[0]=="config":
        #     data = toml.load(kwargs.get("config"))
        #     settings.update(data)
        else:
            for i in list(kwargs):
                if i not in list(settings.as_dict(env=settings.ENV_FOR_DYNACONF).keys()):
                    del kwargs[i]
            settings.update(kwargs)
        self.metric_system = settings.METRIC_SYSTEM
        if self.metric_system == 'NEPTUNE.AI':
            self.run = neptune.init(project = settings.NEPTUNE_PROJECT,api_token = settings.NEPTUNE_API_TOKEN, tags= [settings.ENV_FOR_DYNACONF])
        if self.metric_system == "MLFLOW":
            self.EXPERIMENT_NAME = settings.MLFLOW_EXPERIMENT_NAME
            try:
                self.client = MlflowClient()
                self.exp_id = self.client.get_experiment_by_name(self.EXPERIMENT_NAME).experiment_id     
            except:
                self.exp_id = mlflow.create_experiment(self.EXPERIMENT_NAME)
                
            mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
            self.parent_run = mlflow.start_run(experiment_id=self.exp_id)
            mlflow.set_tags({"env": settings.ENV_FOR_DYNACONF})

        self.logger = self._get_logger()
      

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self.logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        self.logger.critical(*args, **kwargs)

    def fatal(self, *args, **kwargs):
        self.logger.fatal(*args, **kwargs)

    def exception(self, *args, **kwargs):
        self.logger.exception(*args, **kwargs)


    def metrics(self, key, value, *args, **kwargs):
        if self.metric_system == "NA" :
            warnings.warn("No metric system is specified, default logger is used")
            self.info("Metrics: "+ str(key)+ ":" + str(value))
            
        if self.metric_system == 'MLFLOW':
            if type(value) == dict:
                mlflow.log_metrics(value)
            else:
                mlflow.log_metric(key,value)

        if self.metric_system == 'NEPTUNE.AI':
            self.run[key].log(value)

    def params(self, key, value, *args, **kwargs):
        if self.metric_system == "NA" :
            warnings.warn("No metric system is specified, default logger is used")
            self.info("Params: "+ str(key)+ ":" + str(value))

        if self.metric_system == 'MLFLOW':
            if type(value) == dict:
                mlflow.log_params(value)
            else:
                mlflow.log_param(key,value)

        if self.metric_system == 'NEPTUNE.AI':
            self.run[key] = value
            
    def model(self, model_name, model, model_type=None, **kwargs):
        if self.metric_system == "NA" :
            warnings.warn("No metric system is specified, model is stored at current directory as pickle format")
            pickle.dump(model, open("./{}.pkl".format(model_name),'wb'))

        if self.metric_system == 'MLFLOW':
            if model_type is not None:
                return self._mlflow_model(model_type, model_name, model)
            else:
                pickle.dump(model, open("./{}.pkl".format(model_name),'wb'))
                mlflow.log_artifact("./{}.pkl".format(model_name))

        if self.metric_system == 'NEPTUNE.AI':
            try:
                pickle.dump(model, open("./{}.pkl".format(model_name),'wb'))
                self.run["train/model"].track_files("./{}.pkl".format(model_name))
            except:
                self.run[model_name].upload(File.as_pickle(model))
            # except: 
            #     torch.save(model, model_name)
            #     self.run[model_name].upload(model_name)

    def _mlflow_model(self, model_type, model_name, model):
        name_to_import = "mlflow.{}".format(model_type)
        variable_module = importlib.import_module(name_to_import)
        return variable_module.log_model(model, model_name)

    def register_model(self, model_name, model, stage=None):
        if self.metric_system == "NA" :
            warnings.warn("No metric system is specified, could not perform model registry")

        if self.metric_system == 'MLFLOW':
            model_uri = "runs:/{}/model".format(self.parent_run.info.run_id)
            mv = mlflow.register_model(model_uri, model_name)
            if stage is not None:
                try:
                    stage=stage.capitalize()
                    self.client.transition_model_version_stage(name=model_name, stage=stage, version=mv.version)
                except:
                    pass
            
        if self.metric_system == 'NEPTUNE.AI':
            mdl = neptune.init_model(
                name=model_name,
                key=(settings.NEPTUNE_PROJECT[0:3]).upper()+str(randint(0, 9999)),
                project=settings.NEPTUNE_PROJECT, 
                api_token=settings.NEPTUNE_API_TOKEN
                                    )
            model_version = neptune.init_model_version(
                model=mdl._sys_id,
                project=settings.NEPTUNE_PROJECT, 
                api_token=settings.NEPTUNE_API_TOKEN, # your credentials
                                                        )
            if stage is not None:
                stage=stage.lower()
                model_version.change_stage(stage)            
            model_version[model_name].upload(File.as_pickle(model))

    def file(self, file_name, file):
        if self.metric_system == "NA" :
            warnings.warn("No metric system is specified, could not perform log artifacts")
        if self.metric_system == 'MLFLOW':
            mlflow.log_artifact(file)

        if self.metric_system == 'NEPTUNE.AI':
            try:
                self.run[file_name].track_files(file)
            except:
                self.run[file_name].upload(file)

    def _get_logger(self):
        logconfig = toml.load("{}/spdlogger/config/settings.toml".format(path))
        logconfig.pop('development')

        logger_name = "root"

        if settings.LOGGING_FILE:
            logger_name = "file"
            logconfig['handlers']['fileHandler']['filename'] = settings.LOGGING_FILENAME

        dictConfig(logconfig)

        logger = logging.getLogger(logger_name)
        logger.setLevel(settings.LOGGING_LEVEL) # default level "INFO"


        if settings.SENTRY:
            sentry_logging = LoggingIntegration(
                                level = eval("logging.{}".format(settings.SENTRY_LOG_LEVEL)),        # INFO: Capture info and above as breadcrumbs
                                event_level= eval("logging.{}".format(settings.SENTRY_EVENT_LEVEL))  # ERROR: Send errors as events 
                                            )
            sentry_sdk.init(
                    dsn = settings.SENTRY_DSN,
                    integrations = [sentry_logging,],
                    environment = settings.ENV_FOR_DYNACONF,
                    traces_sample_rate=1.0,
                            )   

        if settings.METRIC_SYSTEM == "NEPTUNE.AI":
            logger.addHandler(NeptuneHandler(run=self.run))
            
        return logger
