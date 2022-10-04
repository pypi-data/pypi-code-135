import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENVIRONMENT = os.environ.get("ENVIRONMENT")
DB_USERNAME = os.environ.get(f"DB_USERNAME")
DB_PASSWORD = os.environ.get(f"DB_PASSWORD")
DB_HOSTNAME = os.environ.get(f"DB_HOSTNAME").replace("env", ENVIRONMENT)


class ExampleModel():
    """Example business logic that can be wrapped into a model.
       The class _must_ contain a 'predict' method.
    """
    def business_logic(self, record: dict) -> bool:
        if record.get("sales") > 5:
            return True
        else:
            return False

    def predict(self, model_input: dict) -> bool:
        return self.business_logic()


if __name__ == "__main__":
    """
    Saves the model to MLflow in an experiment run
    The model can be registered as a new version within the MLflow UI
    """
    from umlaut.core import Umlaut

    model = Umlaut(model_name="example model")
    model.track_model(ExampleModel())
