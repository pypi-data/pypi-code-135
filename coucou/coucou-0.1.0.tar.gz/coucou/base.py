import abc


class Solver(abc.ABC):
    @abc.abstractmethod
    def solve(self, problem):
        ...

    @abc.abstractmethod
    def check_problem(self, problem):
        ...
