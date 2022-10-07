import copy

import joblib
import pandas as pd

from kolibri.backend.base.estimator import BaseEstimator
from kdmt.dict import update

try:
    from kolibri.optimizers.optuna.objective import EstimatorObjective
except:
    pass

from kolibri.logger import get_logger

logger = get_logger(__name__)
from kolibri.config import TaskType

class RegSklearnEstimator(BaseEstimator):
    defaults = {"fixed": {
        "default-params": None,
        "task-type": TaskType.REGRESSION
    },

        "tunable": {
        }
    }

    def __init__(self, hyperparameters=None, model=None, indexer=None):
        """Construct a new class classifier using the sklearn framework."""
        from kolibri.backend.models import get_model
        super(RegSklearnEstimator, self).__init__(params=hyperparameters, model=model, indexer=indexer)
        self.hyperparameters["tunable"]["model"] = get_model(hyperparameters["model"], task_type=TaskType.REGRESSION)
        self.update_model_parameters()
        self.model = self.load_model_from_parameters(self.get_parameter("model"))[1]
        self.logger = logger
        self._dask_client = None
        self.all_plots = {
            "pipeline": "Pipeline Plot",
            "parameter": "Hyperparameters",
            "residuals": "Residuals",
            "errors": "Prediction Error",
            "cooks": "Cooks Distance",
            "rfe": "Feature Selection",
            "learning": "Learning Curve",
            "tsne": "Manifold Learning",
            "validation": "Validation Curve",
            "feature": "Feature Importance",
            "feature_all": "Feature Importance (All)",
            "tree": "Decision Tree"
        }
    def update_default_hyper_parameters(self):
        self.defaults = update(self.defaults, RegSklearnEstimator.defaults)
        super().update_default_hyper_parameters()

    def fit(self, X, y, X_val=None, y_val=None):

        if isinstance(X,pd.DataFrame):
            if self.get_parameter("target") in X.columns:
                X=X.drop(self.get_parameter("target"), axis=1)

            self.feature_names=X.columns

            X=X.to_numpy()

        model_results = super(RegSklearnEstimator, self).fit(X, y)
        #            self.model.fit(X, y)

        if not self.get_parameter('evaluate-performance') and X_val is not None and y_val is not None:
            self.evaluate(X_val, y_val)

        return model_results

    def copy(self):
        return copy.deepcopy(self)

    def save(self, model_file_path):
        logger.debug("SklearnAlgorithm save to {0}".format(model_file_path))
        joblib.dump(self.model, model_file_path, compress=True)
        self.model_file_path = model_file_path

    def load_model(self, model_file_path):
        logger.debug("SklearnAlgorithm loading model from {0}".format(model_file_path))
        self.model = joblib.load(model_file_path)
        self.model_file_path = model_file_path

    def is_fitted(self):
        return (
                hasattr(self.model, "n_features_")
                and self.model.n_features_ is not None
                and self.model.n_features_ > 0
        )

    def objective(self, X, y):
        objective = EstimatorObjective(X, y, self, None, eval_metric=self.get_parameter('opt-metric-name'), n_jobs=-1,
                                       random_state=42)
        return objective


from kolibri.registry import ModulesRegistry

ModulesRegistry.add_module(RegSklearnEstimator.name, RegSklearnEstimator)
