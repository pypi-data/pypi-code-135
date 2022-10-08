import copy
from dataclasses import dataclass, fields
from typing import Callable, Tuple

import numpy as np
from scipy.optimize import Bounds, OptimizeResult, minimize
from scipy.spatial.distance import cdist


@dataclass
class PotentialEnergyFunction:
    exponent: float

    def __call__(self, points: np.ndarray) -> Tuple[float, np.ndarray]:
        n_point, n_dim = points.shape

        dist_matrix = cdist(points, points)

        modified_dist_matrix = copy.deepcopy(dist_matrix)
        if self.exponent >= 0:
            for i in range(n_point):
                modified_dist_matrix[i, i] = np.inf
        energy = float(
            0.5 * np.sum(1.0 / (modified_dist_matrix**self.exponent))
        )  # 0.5 becaue double count

        part_grad_list = []
        for i, p in enumerate(points):
            diff = points - p
            r = modified_dist_matrix[:, i]
            tmp = 1.0 / r ** (self.exponent + 2)
            part_grad = np.sum(self.exponent * np.tile(tmp, (n_dim, 1)).T * diff, axis=0)
            part_grad_list.append(part_grad)
        grad = np.hstack(part_grad_list)
        return energy, grad


def scipinize(fun: Callable) -> Tuple[Callable, Callable]:
    closure_member = {"jac_cache": None}

    def fun_scipinized(x):
        f, jac = fun(x)
        closure_member["jac_cache"] = jac
        return f

    def fun_scipinized_jac(x):
        return closure_member["jac_cache"]

    return fun_scipinized, fun_scipinized_jac


@dataclass(frozen=True)
class ScatterResult:
    points: np.ndarray
    success: bool
    status: int
    message: str
    fun: np.ndarray
    jac: np.ndarray
    nit: int

    @classmethod
    def from_optimize_result(cls, res: OptimizeResult, n_dim) -> "ScatterResult":
        kwargs = {}
        for field in fields(cls):
            key = field.name
            if key == "points":
                value = res.x.reshape(-1, n_dim)
            else:
                value = res[key]
            kwargs[key] = value
        return cls(**kwargs)  # type: ignore


def scatter_points(
    n_point: int, n_dim: int, fun: Callable[[np.ndarray], Tuple[float, np.ndarray]]
) -> ScatterResult:
    points = np.random.rand(n_point, n_dim)
    f, jac = scipinize(lambda x: fun(x.reshape(-1, n_dim)))
    x_init = points.flatten()

    bounds = Bounds(lb=np.zeros(n_dim * n_point), ub=np.ones(n_dim * n_point))  # type: ignore
    slsqp_option = {"maxiter": 1000}

    res = minimize(f, x_init, method="SLSQP", jac=jac, bounds=bounds, options=slsqp_option)
    return ScatterResult.from_optimize_result(res, n_dim)


def create_replusive_attractive_potential(
    exp_repulsive: float = 1.0,
    exp_attractive: float = -2.0,
    coef_repulsive: float = 1.0,
    coef_attractive: float = 2.5,
) -> Callable[[np.ndarray], Tuple[float, np.ndarray]]:
    assert exp_repulsive > 0
    assert exp_attractive < 0

    def fun(points: np.ndarray) -> Tuple[float, np.ndarray]:
        F1 = PotentialEnergyFunction(exp_repulsive)
        F2 = PotentialEnergyFunction(exp_attractive)
        f1, grad1 = F1(points)
        f2, grad2 = F2(points)
        return (
            coef_repulsive * f1 + coef_attractive * f2,
            coef_repulsive * grad1 + coef_attractive * grad2,
        )

    return fun
