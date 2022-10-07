import gc
import os
import uuid

import numpy as np
from kdmt.ml.common import sklearn_numpy_warning_fix
from kolibri.utils.cross_validation import cross_val_predict_score,_fit_score_and_predict
import kolibri.evaluation.metrics.classification
from kolibri.core.component import Component
from kolibri.evaluation.classifier_evaluator import ClassifierEvaluator

from kolibri.visualizations.classification_plots import ClassificationPlots
from kolibri.visualizations.regression_plots import RegressionPlots
from kolibri.visualizations.advanced_viz import AdvancedCalssificationPlots

try:
    from kolibri.explainers.shap_explainer import PlotSHAP
except:
    pass
from kdmt.cloud import google
from kdmt.cloud import azure

from kolibri.config import TaskType
from kolibri.config import ParamType
from kdmt.dict import update
from sklearn.utils.multiclass import type_of_target
from sklearn.calibration import CalibratedClassifierCV
from copy import deepcopy
from kdmt.objects import class_from_module_path
from kolibri.logger import get_logger
from kolibri import default_configs as settings
import pandas as pd
import time
import datetime
from sklearn.model_selection import StratifiedKFold, KFold
from kdmt.df import color_df

logger = get_logger(__name__)
from kolibri.output import DefaultDisplay
import joblib

KOLIBRI_MODEL_FILE_NAME = "classifier_kolibri.pkl"



class BaseEstimator(Component):
    """
    This is an abstract class.
    All estimators inherit from BaseEstimator.
    The notion of Estimator represents any mathematical model_type that estimate a response function. In machine learning it can represent either
    a supervised or unsupervised classification algorithm.

    Estimators have the following paramters that can be modified using the configuration object.

    Fixed Hyperparameters
    ---------------------
    base-estimator: a defined kolibri or sklearn.BaseEstimator (default=LogisticRegression)
        This is used by kolibri.bakend.meta estimators as a base estimator for each member of the ensemble is an instance of the base estimator

    explain : boolean (default=False)
        used to output an explanation file in the output folder.

    sampler: str (default=None), A sampler such as SMOTE can be used to balance the data in case the dataset is heavily unbalanced.
    see kolibri.samplers for various options that can be used.

    "priors-thresolding":boolean (default=False), a strategy to handle unbalanced dataset, by class prior probability.

    evaluate-performance: boolean (default=False), use this config to generate performance data before training the model_type.

    optimize-estimator: boolean (default=False), use this config to optimise the parameters of the estimtors. the optimisation stategy optimised the tunable parameters.

    Tunable Hyperparameters
    ---------------------

    These hyper parameters are used in optimization strategies to optimize the performances.
    one obvious parameter to optimise is the base model_type used to train the data.

    """

    short_name = "Unknown"

    component_type = "estimator"

    provides = ["classification", "target_ranking"]

    requires = ["text_features"]

    defaults = {
            "fixed": {
                "target": None,
                "auto-ml": False,
                "base-estimator": None,
                "explain": False,
                "sampler": None,
                "priors-thresolding": False,
                'evaluate-performance': False,
                'calibrate-model':False,
                'calibration-method': "isotonic",
                'task-type': None,
                'optimize-estimator': False,
                'features-names': None,
                'max-nb-models': 5,
                'fold_strategy': 'stratifiedkfold',
                'resampling-strategy': 'holdout', #'cv'
                'data-split-shuffle': True,
                "data-split-stratify": False,
                'imputer': 'none',
                'fold-shuffle': True,
                "n-folds": 5,
                "round": 4,
                "display": "default"
            },

            "tunable": {
                "model-param": {
                    "description": "This is just an example of a tuneable variable",
                    "value": "logreg",
                    "type": ParamType.CATEGORICAL,
                }

            }
        }

    def __init__(self, params, model=None, indexer=None):
        super().__init__(parameters=params)
        self.params = params
        self.library_version = None
        self.model = model
        self.all_plots={}
        self.uid = params.get("uid", str(uuid.uuid4()))
        self.model_file_path = None
        self.data=None
        self.indexer=None

        sklearn_numpy_warning_fix()

        self.sampler=None

        self.performace_scores="Not Computed"

        if self.get_parameter('sampler'):
            from kolibri.samplers import get_sampler
            self.sampler = get_sampler(self.get_parameter('sampler'))

        self.class_priors = None

        # CV params
        fold_param = self.get_parameter("n-folds")


        fold_shuffle_param = self.get_parameter("fold-shuffle")

        from sklearn.model_selection import (
            StratifiedKFold,
            KFold,
            GroupKFold,
            TimeSeriesSplit
        )

        fold_seed = self.get_parameter("random-state") if fold_shuffle_param else None
        if fold_param is not None and fold_param>0:
            if self.get_parameter("fold_strategy") == "kfold":
                self.fold_generator = KFold(
                    fold_param, random_state=fold_seed, shuffle=fold_shuffle_param
                )
            elif self.get_parameter("fold_strategy") == "stratifiedkfold":
                self.fold_generator = StratifiedKFold(
                    fold_param, random_state=fold_seed, shuffle=fold_shuffle_param
                )
            elif self.get_parameter("fold_strategy") == "groupkfold":
                self.fold_generator = GroupKFold(fold_param)
            elif self.get_parameter("fold_strategy") == "timeseries":
                self.fold_generator = TimeSeriesSplit(fold_param)
            else:
                self.fold_generator = self.get_parameter("fold_strategy")
        else:
            self.fold_generator=None

    @property
    def task_type(self):
        return self.get_parameter("task-type")

    def update_default_hyper_parameters(self):
        self.defaults=update( BaseEstimator.defaults, self.defaults,)
        super().update_default_hyper_parameters()

    def load_model_from_parameters(self, model_params):
        model_params=deepcopy(model_params)
        model=class_from_module_path(model_params["class"])
        if model is None:
            raise ValueError('Could not fint '+model_params["class"]+". Please make the name is correct and/or install any missing libraries")

        default_params={p:model_params["parameters"][p]["value"] for p in model_params["parameters"]}
        for param, param_val in default_params.items():
            if isinstance(param_val, list):
                for i, p in enumerate(param_val):
                    if isinstance(p, dict):
                        default_params[param][i]=self.load_model_from_parameters(p)
            elif isinstance(param, dict):
                default_params[param] = self.load_model_from_parameters(param_val)

        return (model_params["name"], model(**default_params))

    def update_model_parameters(self):
        if "fixed" in self.hyperparameters:
            for c in self.hyperparameters["fixed"]:

                if c in self.hyperparameters["tunable"]["model"]["parameters"]:
                    self.hyperparameters["tunable"]["model"]["parameters"][c]["value"]=self.hyperparameters["fixed"][c]

    def fit(self, data_X = None, data_y = None, X_val=None, y_val=None):

        """
        Internal version of ``create_model`` with private arguments.
        """
        self._is_multi_class=len(set(data_y))>2 and self.task_type==TaskType.CLASSIFICATION

        function_params_str = ", ".join(
            [
                f"{k}={v}"
                for k, v in locals().items()
                if k not in ("data_X", "data_y")
            ]
        )

        logger.info("Initializing create_model()")
        logger.info(f"create_model({function_params_str})")

        logger.info("Checking exceptions")

        target_type = type_of_target(data_y)
        supported_types = ['binary', 'multiclass', 'multilabel-indicator', 'continuous']
        if target_type not in supported_types:
            raise ValueError("Classification with data of type {} is "
                             "not supported. Supported types are {}. "
                             "".format(
                                    target_type,
                                    supported_types
                                )
                             )
        # run_time
        runtime_start = time.time()

        """

        ERROR HANDLING ENDS HERE

        """

        self.display=False
        verbose=True
        if not self.display:
            progress_args = {"max": 4}
            timestampStr = datetime.datetime.now().strftime("%H:%M:%S")
            monitor_rows = [
                ["Initiated", ". . . . . . . . . . . . . . . . . .", timestampStr],
                [
                    "Status",
                    ". . . . . . . . . . . . . . . . . .",
                    "Loading Dependencies",
                ],
                [
                    "Estimator",
                    ". . . . . . . . . . . . . . . . . .",
                    "Compiling Library",
                ],
            ]
            self.display = DefaultDisplay(
                verbose=verbose,
                html_param=True,
                progress_args=progress_args,
                monitor_rows=monitor_rows,
            )

        logger.info("Importing libraries")

        # general dependencies

        np.random.seed(self.get_parameter("seed"))

        logger.info("Copying training dataset")



        metrics=kolibri.evaluation.metrics.get_all_metrics(self.task_type)
        metrics_dict = dict([(k, v.scorer) for k, v in metrics.items()])

        self.display.move_progress()

        logger.info("Defining folds")


        logger.info("Declaring metric variables")

        """
        MONITOR UPDATE STARTS
        """
        self.display.update_monitor(1, "Selecting Estimator")
        """
        MONITOR UPDATE ENDS
        """

        logger.info("Importing untrained model")


        full_name = type(self.model).__name__

        self.display.update_monitor(2, full_name)

        if self.get_parameter("probability-threshold") and not self._is_multi_class:
            self.model.set_params(probability_threshold=self.get_parameter("probability-threshold"))
        logger.info(f"{full_name} Imported successfully")

        self.display.move_progress()

        """
        MONITOR UPDATE STARTS
        """

        if not self.get_parameter("evaluate-performance"):
            self.display.update_monitor(1, f"Fitting {str(full_name)}")
            evaluate_first=False
        else:
            self.display.update_monitor(1, "Initializing CV")
            evaluate_first=True


        model_fit_time, model_results, avg_results, predictions = self._create_and_evaluate_model(data_X, data_y, evaluate_first)

        if predictions != []:
            if len(predictions.shape)>1 and predictions.shape[1] > 1:
                predictions = np.column_stack((self.indexer.inverse_transform(np.argmax(predictions, axis=1)) ,predictions))
#               predictions=np.column_stack((self.indexer.inverse_transform(predictions[:,0]), predictions[:,1]))
            elif len(predictions.shape)==1 or predictions.shape[1] == 1:
                if self.indexer is not None:
                    predictions = self.indexer.inverse_transform(predictions)
        # dashboard logging
        indices = "Mean"

        self.display.move_progress()

        logger.info("Uploading results into container")


        if model_results is not None:
            # yellow the mean
            model_results_ = color_df(model_results, "yellow", indices, axis=1)
            model_results_ = model_results_.format(precision=self.get_parameter("round"))
            self.display.display(model_results_)

        # end runtime
        runtime_end = time.time()
        runtime = np.array(runtime_end - runtime_start).round(self.get_parameter("round"))




        logger.info(str(self.model))
        logger.info(
            "create_model() successfully completed......................................"
        )
        gc.collect()
        self.display.close()
        self.display=None

        self.y_true=data_y
        self.X=data_X
        if predictions!=[] and len(predictions.shape)==1:
            self.y_pred=predictions
        else:
            self.y_pred= [] if predictions==[] else predictions[:,1:,].astype(np.float16)
        return model_results, runtime, model_fit_time, predictions

    def _create_and_evaluate_model(self, data_X, data_y, evaluate_first=False):
        """
        MONITOR UPDATE STARTS
        """
        avgs_dict = {}
        predictions=[]
        model_fit_start = time.time()
        model_results=None
        if evaluate_first:
            if self.task_type==TaskType.CLASSIFICATION:
                cv= StratifiedKFold(n_splits=self.get_parameter('n-folds'), shuffle=False, random_state=None)
            else:
                cv=KFold(n_splits=self.get_parameter('n-folds'), shuffle=False, random_state=None)
            self.display.update_monitor(
                row_idx=1,
                message=f"Fitting {cv} Folds"
            )
            """
            MONITOR UPDATE ENDS
            """

            from sklearn.model_selection import cross_validate
            metrics=kolibri.evaluation.metrics.get_all_metrics(self.task_type)
            metrics_dict = dict([(k, v.scorer) for k, v in metrics.items()])

            logger.info("Starting cross validation")

            n_jobs = self.get_parameter("n_jobs")
            from sklearn.gaussian_process import (
                GaussianProcessClassifier,
                GaussianProcessRegressor,
            )

            # special case to prevent running out of memory
            if isinstance(self.model, (GaussianProcessClassifier, GaussianProcessRegressor)):
                n_jobs = 1


            logger.info(f"Cross validating with {cv}, n_jobs={n_jobs}")


            predictions, scores = cross_val_predict_score(
                        self.model,
                        data_X,
                        data_y,
                        method='predict_proba',
                        cv=cv,
                        scoring=metrics_dict,
                        n_jobs=n_jobs,
                        error_score=0,
                    )

            score_dict = {}
            for k, v in metrics.items():
                score_dict[v.display_name] = []
                test_score = scores[f"test_{k}"] * (1 if v.greater_is_better else -1)
                test_score = test_score.tolist()
                score_dict[v.display_name] += test_score

            logger.info("Calculating mean and std")

            avgs_dict = {}
            for k, v in metrics.items():
                    avgs_dict[v.display_name] = []
                    test_score = scores[f"test_{k}"] * (1 if v.greater_is_better else -1)
                    test_score = test_score.tolist()
                    avgs_dict[v.display_name] += [np.mean(test_score), np.std(test_score)]

            self.display.move_progress()

            logger.info("Creating metrics dataframe")

            if hasattr(cv, "n_splits"):
                    fold = cv.n_splits
            elif hasattr(cv, "get_n_splits"):
                    fold = cv.get_n_splits()
            else:
                    raise ValueError(
                        "The cross validation class should implement a n_splits "
                        f"attribute or a get_n_splits method. {cv.__class__.__name__} "
                        "has neither."
                    )

            model_results = pd.DataFrame(
                        {
                            "Fold": np.arange(fold).tolist() + ["Mean", "Std"],
                        }
                    )

            model_scores = pd.concat(
                    [pd.DataFrame(score_dict), pd.DataFrame(avgs_dict)]
                ).reset_index(drop=True)

            model_results = pd.concat([model_results, model_scores], axis=1)
            model_results.set_index(["Fold"], inplace=True)
            model_results = model_results.round(self.get_parameter("round"))

        # refitting the model on complete X_train, y_train
        self.display.update_monitor(1, "Finalizing Model")
        logger.info("Finalizing model")
        if self.get_parameter("calibrate-model"):
            self.model = CalibratedClassifierCV(self.model, cv=None, method=self.get_parameter("calibration-method"))

        self.model.fit(data_X, data_y)


        model_fit_end = time.time()

        # calculating metrics on predictions of complete train dataset


        model_fit_time = np.array(model_fit_end - model_fit_start).round(2)



        return model_fit_time, model_results, avgs_dict, predictions

    def calibrate(
        self,
            X, y,
        method: str = "sigmoid",
        fit_kwargs = None,
    ):

        """
        This function calibrates the probability of a given estimator using isotonic
        or logistic regression. The output of this function is a score grid with CV
        scores by fold. Metrics evaluated during CV can be accessed using the
        ``get_metrics`` function. Custom metrics can be added or removed using
        ``add_metric`` and ``remove_metric`` function. The ouput of the original estimator
        and the calibrated estimator (created using this function) might not differ much.
        In order to see the calibration differences, use 'calibration' plot in ``plot_model``
        to see the difference before and after.


        Example
        -------


        estimator: scikit-learn compatible object
            Trained model object


        method: str, default = 'sigmoid'
            The method to use for calibration. Can be 'sigmoid' which corresponds to
            Platt's method or 'isotonic' which is a non-parametric approach.


        calibrate_fold: integer or scikit-learn compatible CV generator, default = 5
            Controls internal cross-validation. Can be an integer or a scikit-learn
            CV generator. If set to an integer, will use (Stratifed)KFold CV with
            that many folds. See scikit-learn documentation on Stacking for
            more details.


        fold: int or scikit-learn compatible CV generator, default = None
            Controls cross-validation. If None, the CV generator in the ``fold_strategy``
            parameter of the ``setup`` function is used. When an integer is passed,
            it is interpreted as the 'n_splits' parameter of the CV generator in the
            ``setup`` function.


        round: int, default = 4
            Number of decimal places the metrics in the score grid will be rounded to.


        fit_kwargs: dict, default = {} (empty dict)
            Dictionary of arguments passed to the fit method of the model.


        groups: str or array-like, with shape (n_samples,), default = None
            Optional group labels when GroupKFold is used for the cross validation.
            It takes an array with shape (n_samples, ) where n_samples is the number
            of rows in training dataset. When string is passed, it is interpreted as
            the column name in the dataset containing group labels.


        verbose: bool, default = True
            Score grid is not printed when verbose is set to False.


        return_train_score: bool, default = False
            If False, returns the CV Validation scores only.
            If True, returns the CV training scores along with the CV validation scores.
            This is useful when the user wants to do bias-variance tradeoff. A high CV
            training score with a low corresponding CV validation score indicates overfitting.


        Returns:
            Trained Model


        Warnings
        --------
        - Avoid isotonic calibration with too few calibration samples (< 1000) since it
        tends to overfit.

        """

        function_params_str = ", ".join([f"{k}={v}" for k, v in locals().items()])

        logger.info("Initializing calibrate_model()")
        logger.info(f"calibrate_model({function_params_str})")

        logger.info("Checking exceptions")

        # run_time
        runtime_start = time.time()

        if not fit_kwargs:
            fit_kwargs = {}

        # checking round parameter
        if type(round) is not int:
            raise TypeError("Round parameter only accepts integer value.")

        """

        ERROR HANDLING ENDS HERE

        """

        fold = StratifiedKFold(self.get_parameter("n-folds"))


        logger.info("Preloading libraries")

        # pre-load libraries

        logger.info("Preparing display monitor")

        progress_args = {"max": 2 + 4}
        timestampStr = datetime.datetime.now().strftime("%H:%M:%S")
        monitor_rows = [
            ["Initiated", ". . . . . . . . . . . . . . . . . .", timestampStr],
            [
                "Status",
                ". . . . . . . . . . . . . . . . . .",
                "Loading Dependencies",
            ],
            [
                "Estimator",
                ". . . . . . . . . . . . . . . . . .",
                "Compiling Library",
            ],
        ]
        display = DefaultDisplay(
            verbose=True,
            html_param=True,
            progress_args=progress_args,
            monitor_rows=monitor_rows,
        )

        np.random.seed(self.get_parameter("seed"))

        probability_threshold = None


        logger.info("Getting model name")

        full_name = str(self.model)

        logger.info(f"Base model : {full_name}")

        display.update_monitor(2, full_name)

        """
        MONITOR UPDATE STARTS
        """

        display.update_monitor(1, "Selecting Estimator")

        """
        MONITOR UPDATE ENDS
        """

        # calibrating estimator

        logger.info("Importing untrained CalibratedClassifierCV")

        calibrated_model=CalibratedClassifierCV(self.model, cv=fold, method=method)

        display.move_progress()

        logger.info(
            "SubProcess create_model() called =================================="
        )
        self._create_and_evaluate_model()
        self.model= calibrated_model.fit(X, y)


    def load_model(self, model_file_path):
        pass

    def explain(
        self,
        X_train,
        y_train,
        X_validation,
        y_validation,
        model_file_path,
        learner_name,
        target_name=None,
        class_names=None,
        ml_task=None,
    ):
        # do not produce feature importance for Baseline
        if self.algorithm_short_name == "Baseline":
            return
        PlotSHAP.compute(
                self,
                X_train,
                y_train,
                X_validation,
                y_validation,
                model_file_path,
                learner_name,
                class_names,
                ml_task,
            )

    def get_params(self):
        params = {
            "library_version": self.library_version,
            "algorithm_name": self.algorithm_name,
            "algorithm_short_name": self.algorithm_short_name,
            "uid": self.uid,
            "params": self.params,
            "name": self.name,
        }
        if hasattr(self, "best_ntree_limit") and self.best_ntree_limit is not None:
            params["best_ntree_limit"] = self.best_ntree_limit
        return params

    def set_params(self, json_desc, learner_path):
        self.library_version = json_desc.get("library_version", self.library_version)
        self.algorithm_name = json_desc.get("algorithm_name", self.algorithm_name)
        self.algorithm_short_name = json_desc.get(
            "algorithm_short_name", self.algorithm_short_name
        )
        self.uid = json_desc.get("uid", self.uid)
        self.params = json_desc.get("params", self.params)
        self.name = json_desc.get("name", self.name)
        self.model_file_path = learner_path

        if hasattr(self, "best_ntree_limit"):
            self.best_ntree_limit = json_desc.get(
                "best_ntree_limit", self.best_ntree_limit
            )

    @classmethod
    def required_packages(cls):
        return ["sklearn"]

    def evaluate(self, X_val=None, y_val=None):

        if X_val is not None and y_val is not None:
            pred = self.predict(X_val)

            self.performace_scores = ClassifierEvaluator().get_performance_report(y_true=y_val, y_pred=pred)

    def compute_priors(self, y):
        unique, counts = np.unique(y, return_counts=True)
        self.class_priors = dict(zip(unique, counts))

        total = sum(self.class_priors.values(), 0.0)
        self.class_priors = {k: v / total for k, v in self.class_priors.items()}

    def predict_proba(self, X):
        """Given a bow vector of an input text, predict the class label.

        Return probabilities for all y_values.

        :param X: bow of input text
        :return: vector of probabilities containing one entry for each label"""
        raw_predictions=None
        try:
            if self.get_parameter('task-type') == TaskType.BINARY_CLASSIFICATION:
                raw_predictions=self.model.predict_proba(X)[:, 1]
            elif self.get_parameter('task-type') == TaskType.CLASSIFICATION:
                raw_predictions=self.model.predict_proba(X)
        except:
            raise Exception('Predict_proba raised an error in Estimator')


        if self.get_parameter("priors-thresolding"):
            if not raw_predictions is None:
                try:
                    priors = np.array([v for v in self.class_priors.values()])
                    raw_predictions = (raw_predictions.T - priors[:, None]) / priors[:, None]
                    raw_predictions = np.argmax(raw_predictions.T, axis=1)
                except Exception as e:
                    print(e)

        # sort the probabilities retrieving the indices of
        # the elements in sorted order
        sorted_indices = np.fliplr(np.argsort(raw_predictions, axis=1))

        return raw_predictions, sorted_indices, [p[sorted_indices[i]] for i, p in enumerate(raw_predictions)]

    def predict(self, X):
        """Given a bow vector of an input text, predict most probable label.

        Return only the most likely label.

        :param X: bow of input text
        :return: tuple of first, the most probable label and second,
                 its probability."""
        probabilities=[]
        try:
            raw_predictions, class_ids, probabilities=self.predict_proba(X)
        except:
            class_ids=self.model.predict(X)

        classes = [self.indexer.inverse_transform(np.ravel(class_id)) for class_id in class_ids]

        return self.process([list(zip(classe, probability)) for classe, probability in zip(classes, probabilities)])

    def process(self, results):

        if results is not None:
            ranking= [result[:settings.TARGET_RANKING_LENGTH] for result in results]

            target = [{"name": result[0][0], "confidence": result[0][1]} for result in results]

            target_ranking = [[{"name":r[0], "confidence":r[1]} for r in rank] for rank in ranking]
        else:
            target = {"name": None, "confidence": 0.0}
            target_ranking = []


        response={
            "label": target,
            "ranking": target_ranking
        }
        return response

    @classmethod
    def load(cls, model_dir=None, model_metadata=None, cached_component=None, platform = None, authentication = None, **kwargs):
        """
        This generic function loads a previously saved transformation pipeline and model
        from the current active directory into the current python environment.
        Load object must be a pickle file.

        Parameters
        ----------


        Returns
        -------
        Model Object

        """

        function_params_str = ", ".join([f"{k}={v}" for k, v in locals().items()])

        logger = get_logger()

        logger.info("Initializing load_model()")
        logger.info(f"load_model({function_params_str})")

        # exception checking
        file_name = model_metadata.get("classifier_file", KOLIBRI_MODEL_FILE_NAME)
        if platform:
            if not authentication:
                raise ValueError("Authentication is missing.")

        if not platform:

            classifier_file = os.path.join(model_dir, file_name)

            if os.path.exists(classifier_file):
                model = joblib.load(classifier_file)
            else:
                return cls(model_metadata)
            return model

        # cloud providers
        elif platform == "aws":

            import boto3

            bucketname = authentication.get("bucket")

            if bucketname is None:
                logger.error(
                    "S3 bucket name missing. Provide `bucket` as part of authentication parameter"
                )
                raise ValueError(
                    "S3 bucket name missing. Provide `bucket` name as part of authentication parameter"
                )

            filename = f"{file_name}.pkl"

            if "path" in authentication:
                key = os.path.join(authentication.get("path"), filename)
            else:
                key = filename

            index = filename.rfind("/")
            s3 = boto3.resource("s3")

            if index == -1:
                s3.Bucket(bucketname).download_file(key, filename)
            else:
                path, key = filename[: index + 1], filename[index + 1:]
                if not os.path.exists(path):
                    os.makedirs(path)
                s3.Bucket(bucketname).download_file(key, filename)

            model = cls.load_model(filename, verbose=False)

            logger.info("Transformation Pipeline and Model Successfully Loaded")

            return model

        elif platform == "gcp":

            bucket_name = authentication.get("bucket")
            project_name = authentication.get("project")

            if bucket_name is None or project_name is None:
                logger.error(
                    "Project and Bucket name missing. Provide `bucket` and `project` as part of "
                    "authentication parameter"
                )
                raise ValueError(
                    "Project and Bucket name missing. Provide `bucket` and `project` as part of "
                    "authentication parameter"
                )

            filename = f"{file_name}.pkl"

            _download_blob_gcp(project_name, bucket_name, filename, filename)

            model = cls.load_model(filename, verbose=False)

            logger.info("Transformation Pipeline and Model Successfully Loaded")
            return model

        elif platform == "azure":

            container_name = authentication.get("container")

            if container_name is None:
                logger.error(
                    "Storage Container name missing. Provide `container` as part of authentication parameter"
                )
                raise ValueError(
                    "Storage Container name missing. Provide `container` as part of authentication parameter"
                )

            filename = f"{file_name}.pkl"

            _download_blob_azure(container_name, filename, filename)

            model = cls.load_model(filename, verbose=False)

            logger.info("Transformation Pipeline and Model Successfully Loaded")
            return model
        else:
            print(f"Platform {platform} is not supported by pycaret or illegal option")
        gc.collect()

    def persist(self, model_dir):
        """Persist this model_type into the passed directory."""

        classifier_file = os.path.join(model_dir, KOLIBRI_MODEL_FILE_NAME)
        joblib.dump(self, classifier_file)

        logger.info(f"{self.name} saved in current working directory")
        logger.info(str(self))
        logger.info(
            "save_model() successfully completed......................................"
        )

        gc.collect()
        return {
            "classifier_file": KOLIBRI_MODEL_FILE_NAME,
            "performace_scores": self.performace_scores,
        }

    def plot(
        self,
        plot,
        scale: float = 1,
        fit_kwargs = None,
        plot_kwargs= None,
        groups = None,
        feature_name = None,
        label = False,
        use_train_data = False,
        verbose = True,
        system = True,
        display= None,  
        display_format = None,
    ):


        function_params_str = ", ".join([f"{k}={v}" for k, v in locals().items()])

        logger.info("Initializing plot_model()")
        logger.info(f"plot_model({function_params_str})")

        logger.info("Checking exceptions")
        print("plotting "+plot)
        if not fit_kwargs:
            fit_kwargs = {}

        if plot not in self.all_plots:
            raise ValueError(
                f"Plot {plot} is not Available. Please see docstring for list of available Plots."
            )

        # Import required libraries ----
        if display_format == "streamlit":
            try:
                import streamlit as st
            except:
                raise Exception("did you install streamlit. use 'pip install streamlit'")

        # multiclass plot exceptions:
        multiclass_not_available = ["threshold", "manifold", "rfe"]
        if self._is_multi_class and self.task_type==TaskType.CLASSIFICATION:
            if plot in multiclass_not_available:
                logger.warning(
                    "Plot Not Available for multiclass problems. Please see docstring for list of available Plots."
                )
                return None

        # exception for CatBoost
        # if "CatBoostClassifier" in str(type(estimator)):
        #    raise ValueError(
        #    "CatBoost estimator is not compatible with plot_model function, try using Catboost with interpret_model instead."
        # )

        # checking for auc plot
        if not hasattr(self.model, "predict_proba") and plot == "auc":
            raise TypeError(
                "AUC plot not available for estimators with no predict_proba attribute."
            )

        # checking for calibration plot
        if not hasattr(self.model, "predict_proba") and plot == "calibration":
            raise TypeError(
                "Calibration plot not available for estimators with no predict_proba attribute."
            )

        def is_tree(e):
            from sklearn.ensemble._forest import BaseForest
            from sklearn.tree import BaseDecisionTree

            if "final_estimator" in e.get_params():
                e = e.final_estimator
            if "base_estimator" in e.get_params():
                e = e.base_estimator
            if isinstance(e, BaseForest) or isinstance(e, BaseDecisionTree):
                return True

        # checking for calibration plot
        if plot == "tree" and not is_tree(self.model) and self.task_type==TaskType.CLASSIFICATION:
            raise TypeError(
                "Decision Tree plot is only available for scikit-learn Decision Trees and Forests, Ensemble models using those or Stacked models using those as meta (final) estimators."
            )

        # checking for feature plot
        if not (
            hasattr(self.model, "coef_") or hasattr(self.model, "feature_importances_")
        ) and (plot == "feature" or plot == "feature_all" or plot == "rfe"):
            raise TypeError(
                "Feature Importance and RFE plots not available for estimators that doesnt support coef_ or feature_importances_ attribute."
            )


        if type(label) is not bool:
            raise TypeError("Label parameter only accepts True or False.")

        if type(use_train_data) is not bool:
            raise TypeError("use_train_data parameter only accepts True or False.")

        if feature_name is not None and type(feature_name) is not str:
            raise TypeError(
                "feature parameter must be string containing column name of dataset."
            )

        """

        ERROR HANDLING ENDS HERE

        """


        if not display:
            display = DefaultDisplay(verbose=verbose, html_param=True)

        plot_kwargs = plot_kwargs or {}

        logger.info("Preloading libraries")
        # pre-load libraries
        import matplotlib.pyplot as plt

        np.random.seed(self.get_parameter("seed"))


        estimator = deepcopy(self.model)
        model = estimator

        # plots used for logging (controlled through plots_log_param)
        # AUC, #Confusion Matrix and #Feature Importance

        logger.info("Copying training dataset")

        logger.info(f"Plot type: {plot}")


        
        _base_dpi = 100
        all_plots=None
        all_plots_adv=None
        if self.task_type==TaskType.CLASSIFICATION:
            all_plots=ClassificationPlots(y_true=self.y_true, y_pred=self.y_pred, labels_dict=self.indexer.idx2token)
            all_plots_adv=AdvancedCalssificationPlots(X=self.X, y=self.y_true, classifier=self.model, labels_dict=self.indexer.idx2token)
        elif self.task_type==TaskType.REGRESSION:
            all_plots = RegressionPlots(y_true=self.y_true, y_pred=self.y_pred, model_name=str(self.model),X=self.X, y=self.y_true, estimator=self.model, features_names=self.get_parameter("features-names"))

        try:
            if all_plots:
                function = getattr(all_plots, plot)
        except:
            try:
                if all_plots_adv:
                    function=getattr(all_plots_adv, plot)
            except:
                logger.warning(plot+" Does not exist. Please check the spelling")
                return None
        # execute the plot method
        plt = function()

        gc.collect()

        logger.info(
            "plot_model() successfully completed......................................"
        )

        return plt

    def deploy(self, model_dir: str, authentication: dict, platform: str = "azure", prep_pipe_=None
    ):

        function_params_str = ", ".join([f"{k}={v}" for k, v in locals().items()])

        logger = get_logger()

        logger.info("Initializing deploy_model()")
        logger.info(f"deploy_model({function_params_str})")

        allowed_platforms = ["aws", "gcp", "azure"]

        if platform not in allowed_platforms:
            logger.error(
                f"(Value Error): Platform {platform} is not supported by pycaret or illegal option"
            )
            raise ValueError(
                f"Platform {platform} is not supported by pycaret or illegal option"
            )

        if platform:
            if not authentication:
                raise ValueError("Authentication is missing.")

        # general dependencies
        import os

        logger.info("Saving model in active working directory")
        logger.info("SubProcess save_model() called ==================================")
        self.persist(model_dir)
        logger.info("SubProcess save_model() end ==================================")

        if platform == "aws":

            logger.info("Platform : AWS S3")
            import boto3

            # initialize s3
            logger.info("Initializing S3 client")
            s3 = boto3.client("s3")
            filename = f"{KOLIBRI_MODEL_FILE_NAME}.pkl"
            if "path" in authentication:
                key = os.path.join(authentication.get("path"), f"{KOLIBRI_MODEL_FILE_NAME}.pkl")
            else:
                key = f"{KOLIBRI_MODEL_FILE_NAME}.pkl"
            bucket_name = authentication.get("bucket")

            if bucket_name is None:
                logger.error(
                    "S3 bucket name missing. Provide `bucket` as part of authentication parameter."
                )
                raise ValueError(
                    "S3 bucket name missing. Provide `bucket` name as part of authentication parameter."
                )

            import botocore.exceptions

            try:
                s3.upload_file(filename, bucket_name, key)
            except botocore.exceptions.NoCredentialsError:
                logger.error(
                    "Boto3 credentials not configured. Refer boto3 documentation "
                    "(https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)"
                )
                logger.error("Model deployment to AWS S3 failed.")
                raise ValueError(
                    "Boto3 credentials not configured. Refer boto3 documentation "
                    "(https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)"
                )
            os.remove(filename)
            print("Model Successfully Deployed on AWS S3")
            logger.info("Model Successfully Deployed on AWS S3")
            logger.info(str(self.model))

        elif platform == "gcp":

            logger.info("Platform : GCP")

            # initialize deployment
            filename = f"{KOLIBRI_MODEL_FILE_NAME}.pkl"
            key = f"{KOLIBRI_MODEL_FILE_NAME}.pkl"
            bucket_name = authentication.get("bucket")
            project_name = authentication.get("project")

            if bucket_name is None or project_name is None:
                logger.error(
                    "Project and Bucket name missing. Provide `bucket` and `project` as part of "
                    "authentication parameter"
                )
                raise ValueError(
                    "Project and Bucket name missing. Provide `bucket` and `project` as part of "
                    "authentication parameter"
                )

            try:
                google.create_bucket(project_name, bucket_name)
                google.upload_blob(project_name, bucket_name, filename, key)
            except Exception:
                google.upload_blob(project_name, bucket_name, filename, key)
            os.remove(filename)
            print("Model Successfully Deployed on GCP")
            logger.info("Model Successfully Deployed on GCP")
            logger.info(str(self.model))

        elif platform == "azure":

            logger.info("Platform : Azure Blob Storage")

            # initialize deployment
            filename = f"{KOLIBRI_MODEL_FILE_NAME}.pkl"
            key = f"{KOLIBRI_MODEL_FILE_NAME}.pkl"
            container_name = authentication.get("container")

            if container_name is None:
                logger.error(
                    "Storage Container name missing. Provide `container` as part of authentication parameter"
                )
                raise ValueError(
                    "Storage Container name missing. Provide `container` as part of authentication parameter"
                )

            try:
                azure.get_container(authentication, container_name)
                azure.upload_file_object(authentication, container_name, filename, key)
            except Exception:
                azure.upload_file_object(authentication, container_name, filename, key)

            os.remove(filename)

            print("Model Successfully Deployed on Azure Storage Blob")
            logger.info("Model Successfully Deployed on Azure Storage Blob")
            logger.info(str(self.model))

        logger.info(
            "deploy_model() successfully completed......................................"
        )
        gc.collect()