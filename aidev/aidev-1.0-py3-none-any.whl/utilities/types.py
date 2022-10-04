from abc import ABC, abstractmethod
from typing import List, Union
import matplotlib.pyplot as plt
from numpy import ndarray
from sklearn.model_selection import cross_val_score
from pymoo.optimize import minimize
from pymoo.problems.functional import FunctionalProblem
from pandas import DataFrame
from matplotlib.pyplot import savefig
from matplotlib.axes import Axes


class Target:
    """
    Class for defining a target variable.
    """

    def __init__(
        self,
        name: str,
        objective: bool = True,
        measurement: bool = False,
        weight: float = 0,
        ineq: float = 0,
    ) -> None:
        """

        Initialize class.

        :param name: name of the target (as defined in NX).
        :type name: str
        :param objective: Specify if target is to consider an optimization objective. Default True
        :type objective: bool
        :param measurement: Specify if target si coming from a NX measurement. Default False
        :type measurement: bool
        :param weight: Weight to be assigned to the objective (optimization and decision-making).
                       If None, weight is equally distributed between objectives. Default None.
        :type weight: float
        :param ineq: Value of inequality constraint. Objective should be <= then ineq. Default None.
        :type ineq: float
        :return:
        :rtype: None
        """
        self.name = name
        self.objective = objective
        self.measurement = measurement
        self.weight = weight
        self.ineq = ineq

    def __repr__(self) -> str:
        return (
            f"Target('{self.name}', '{self.objective}', {self.measurement},"
            f" {self.weight}, {self.ineq})"
        )


class Parameter:
    """
    Class for defining a parameter variable.
    """

    def __init__(self, name: str, unit: str, lb: float, ub: float) -> None:
        """

        Initialize class.

        :param name: Name of parameter.
        :type name: str
        :param unit: Physical units of parameter according to NX.
        :type unit: str
        :param lb: Lower bound of parameter.
        :type lb: float
        :param ub: Upper bound of parameter.
        :type ub: float
        :return:
        :rtype: None
        """
        self.name = name
        self.unit = unit
        self.lb = lb
        self.ub = ub

    def __repr__(self) -> str:
        return f"Parameter('{self.name}', '{self.unit}', {self.lb}, {self.ub}"


class FeatureDefinition:
    """
    Class used to combined and extract parameters and targets related information.

    """

    def __init__(self, parameters: List[Parameter], targets: List[Target]) -> None:
        """

        Initialize class.

        :param parameters: List of parameter objects.
        :type parameters: List[Parameter]
        :param targets: List of target objects.
        :type targets: List[Target]
        :return:
        :rtype: None
        """
        self.parameters = parameters
        self.targets = targets
        self._update()

    def _update(self) -> None:
        """
        Update calculated and extracted values from parameters and targets.

        """
        self.pnames = [p.name for p in self.parameters]
        self.punits = [p.unit for p in self.parameters]
        self.lbs = [p.lb for p in self.parameters]
        self.ubs = [p.ub for p in self.parameters]
        self.nvar = len(self.parameters)

        self.tnames = [t.name for t in self.targets]
        self.areobjs = [t.objective for t in self.targets]
        self.aremeas = [t.measurement for t in self.targets]
        self.weights = [t.weight for t in self.targets]
        self.ineqs = [t.ineq for t in self.targets]
        self.nobj = len(self.areobjs)
        assert sum(self.weights) == 1, "Objective weights must sum up to 1."


class Visualization(ABC):
    """
    Abstract class for results visualization.
    """

    def __init__(
        self,
        data: DataFrame,
        save: bool = True,
        figname: str = "results.html",
        **kwargs,
    ):
        """

        :param data: pandas dataframe for training surrogate model.
        :type data: DataFrame
        :param save: Whether to save the generated image.
        :type save: bool
        :param figname: name to give to generated image.
        :type figname: str
        :param kwargs: Optional arguments (see child classes)
        :type kwargs:
        :return: The visualization object (matplotlib Axes)
        :rtype: Axes
        """
        self.fig = self._method(data, **kwargs)
        if save:
            self.fig.write_html(figname)

    def getfig(self):
        return self.fig

    @abstractmethod
    def _method(self, data: DataFrame, **kwargs) -> Axes:
        """
        Method defining visualization object. To be overridden.

        :param data: pandas dataframe for training surrogate model.
        :type data: DataFrame
        :param kwargs: Optional arguments (see child classes)
        :type kwargs:
        :return: The visualization object (matplotlib Axes)
        :rtype: Axes
        """
        pass


class Surrogate(ABC):
    """
    Abstract class for surrogate modelling.
    """

    def __call__(self, x: Union[List, ndarray], y: Union[List, ndarray]) -> tuple:
        """

        :param x: Data containing predictor values.
        :type x: Union[List, ndarray]
        :param y: Data containing target values.
        :type y: Union[List, ndarray]
        :return: Trained surrogate sklearn model and tuple containing model accuracy and standard deviation
        :rtype: tuple
        """
        pipe = self._model()
        sur = pipe.fit(x, y)
        scores = cross_val_score(sur, x, y, cv=4)
        performance = (scores.mean(), scores.std())
        return sur, performance

    @abstractmethod
    def _model(self):
        """
        Method defining the surrogate model. To be overridden.

        :return: Sklearn pipeline containing the surrogate model.
        :rtype:
        """
        pass


class Sampling(ABC):
    """
    Abstract class for DoE sampling.
    """

    def __init__(self, features: FeatureDefinition) -> None:
        """

        :param features: Collective targets and parameters information in the form of Definition class
        :type features: FeatureDefinition
        """
        self.lbs = features.lbs
        self.ubs = features.ubs
        self.nvar = features.nvar

    def __call__(self, n_samples: int = 50) -> ndarray:
        """

        :param n_samples: Number of samples to generate in the DoE.
        :type n_samples: int
        :return: The samples to be evaluated.
        :rtype: ndarray
        """
        samples = self._method(n_samples)
        return samples

    @abstractmethod
    def _method(self, n_samples: int = 50) -> ndarray:
        """

        Method defining the sampling strategy.

        :param n_samples: Number of samples to generate in the DoE.
        :type n_samples: int
        :return: The samples.
        :rtype: ndarray
        """
        pass


class Optimization(ABC):
    """
    Abstract class for surrogate optimization.
    """

    def __init__(
        self, surrogates: list, features: FeatureDefinition, popsize: int = 10
    ) -> None:
        """

        :param features: Collective targets and parameters information in the form of Definition class
        :type features: FeatureDefinition
        :param popsize: population size to use in evolutionary algorithms (global optimization)
        :type popsize: int
        """

        self.objs = []
        self.consts = []
        self.popsize = popsize
        self.nvar = features.nvar
        self.lbs = features.lbs
        self.ubs = features.ubs

        for name, surrogate, weight, ineq in zip(
            features.tnames,
            surrogates,
            features.weights,
            features.ineqs,
        ):
            if surrogate is not None:
                if weight != 0:
                    self.objs.append(
                        lambda p, surrogate=surrogate, weight=weight: weight
                        * surrogate(p)
                    )
                else:
                    raise Exception(
                        f"Objective {name} does not have an associated weight. Please define it."
                    )
                if ineq != 0:
                    self.consts.append(
                        lambda p, surrogate=surrogate, ineq=ineq: surrogate(p) - ineq
                    )
            else:
                raise Exception(f"Target {name} does not have an associated surrogate.")

    def __call__(self) -> dict:
        """

        :return: Dictionary containing the optimized parameters and target values.
        :rtype: dict
        """

        problem = self._problem()
        algorithm = self._algorithm()

        res = minimize(
            problem,
            algorithm,
            seed=1,
            return_least_infeasible=True,
        )
        if len(problem.objs) == 1:
            res.X = [res.X]
            res.F = [res.F]

        return {"x": res.X, "fmodel": res.F}

    def _problem(self):
        """
        Method defining the optimization problem.

        :return: The problem object.
        :rtype:

        See https://pymoo.org/index.html for more information.
        """
        problem = FunctionalProblem(
            self.nvar, self.objs, constr_ieq=self.consts, xl=self.lbs, xu=self.ubs
        )
        return problem

    @abstractmethod
    def _algorithm(self):
        """
        Method defining the optimization algorithm.

        :return: The algorithm object.
        :rtype:

        See https://pymoo.org/index.html for more information.
        """
        pass
