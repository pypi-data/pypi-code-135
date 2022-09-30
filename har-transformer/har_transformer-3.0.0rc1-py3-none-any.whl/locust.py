import enum
import warnings
from typing import Sequence, List, Union, Iterator

import transformer.plugins as plug
import transformer.python as py
from transformer.plugins.contracts import Plugin
from transformer.scenario import Scenario
from transformer.task import Task, Task2
from ._version import __version__

LOCUST_MAX_WAIT_DELAY = 10

LOCUST_MIN_WAIT_DELAY = 0

LOCUSTFILE_COMMENT = f"""
File automatically generated by Transformer v{__version__}:
https://github.com/zalando-incubator/Transformer
""".strip()


def _locust_task(task: Union[Task, Task2]) -> py.Function:
    """
    Transforms a Task into the Python code expected by Locust.

    This function is private because it does not return a complete Locust task
    (the @task decorator is missing) and should therefore not be used for that
    purpose by unsuspecting users.
    """
    if isinstance(task, Task):
        # TODO: remove when Task2 has replaced Task.
        #   See https://github.com/zalando-incubator/Transformer/issues/11.
        task = Task2.from_task(task)

    return py.Function(name=task.name, params=["self"], statements=task.statements)


class TaskSetType(enum.Enum):
    Set = "TaskSet"
    Sequence = "TaskSequence"


def locust_taskset(scenario: Scenario) -> py.Class:
    """
    Transforms a scenario (potentially containing other scenarios) into a Locust
    TaskSet definition.
    """
    if any(isinstance(child, (Task, Task2)) for child in scenario.children):
        ts_type = TaskSetType.Sequence
    else:
        ts_type = TaskSetType.Set

    fields: List[py.Statement] = []
    for i, child in enumerate(scenario.children, start=1):
        seq_decorator = f"seq_task({i})"
        if isinstance(child, (Task2, Task)):
            fields.append(py.Decoration(seq_decorator, _locust_task(child)))
        elif isinstance(child, Scenario):
            field = py.Decoration(f"task({child.weight})", locust_taskset(child))
            if ts_type is TaskSetType.Sequence:
                field = py.Decoration(seq_decorator, field)
            fields.append(field)
        else:
            wrong_type = child.__class__.__qualname__
            scenario_type = scenario.__class__.__qualname__
            raise TypeError(
                f"unexpected type {wrong_type} in {scenario_type}.children: {child!r}"
            )
    return py.Class(scenario.name, superclasses=[str(ts_type.value)], statements=fields)


def locust_classes(scenarios: Sequence[Scenario]) -> List[py.Class]:
    """
    Transforms scenarios into all Python classes needed by Locust (TaskSet and
    Locust classes).

    The only missing parts before a fully functional locustfile are:
    - integrating all necessary set-up/tear-down statements:
        - Python imports,
        - apply global plugins,
        - etc.
    - serializing everything via transformer.python.
    """
    classes = []
    for scenario in scenarios:
        taskset = locust_taskset(scenario)
        is_post_1 = py.BinaryOp(py.Symbol("LOCUST_MAJOR_VERSION"), ">=", py.Literal(1))
        tasks = py.IfElse(
            [
                (
                    is_post_1,
                    [py.Assignment("tasks", py.Literal([py.Symbol(taskset.name)]))],
                )
            ],
            [py.Assignment("task_set", py.Symbol(taskset.name))],
        )
        locust_class = py.Class(
            name=f"LocustFor{taskset.name}",
            superclasses=["HttpLocust"],
            statements=[
                tasks,
                py.Assignment("weight", py.Literal(scenario.weight)),
                py.Assignment("min_wait", py.Literal(LOCUST_MIN_WAIT_DELAY)),
                py.Assignment("max_wait", py.Literal(LOCUST_MAX_WAIT_DELAY)),
            ],
        )
        classes.append(taskset)
        classes.append(locust_class)
    return classes


def locust_detected_version() -> py.Program:
    return [
        py.Import(["LooseVersion"], source="distutils.version"),
        py.Import(["__version__"], source="locust"),
        py.OpaqueBlock("LOCUST_MAJOR_VERSION = LooseVersion(__version__).version[0]"),
    ]


def locust_imports() -> py.Program:
    is_post_1 = py.BinaryOp(
        py.Symbol("LOCUST_MAJOR_VERSION"),
        ">=",
        py.Literal(1),
    )
    imports_pre_1 = [
        py.Import(
            ["HttpLocust", "TaskSequence", "TaskSet", "seq_task", "task"],
            source="locust",
        )
    ]
    imports_post_1 = [
        py.Import(
            ["HttpUser", "SequentialTaskSet", "TaskSet", "task"],
            source="locust",
        ),
        py.Assignment("HttpLocust", py.Symbol("HttpUser")),
        py.Assignment("TaskSequence", py.Symbol("SequentialTaskSet")),
        py.Function("seq_task", ["_"], [py.Return(py.Symbol("task"))]),
    ]
    return [
        py.IfElse([(is_post_1, imports_post_1)], imports_pre_1),
    ]


def locust_program(scenarios: Sequence[Scenario]) -> py.Program:
    """
    Converts a ScenarioGroup into a Locust File.
    """
    global_code_blocks = {
        # TODO: Replace me with a plugin framework that accesses the full tree.
        #   See https://github.com/zalando-incubator/Transformer/issues/11.
        block_name: py.OpaqueBlock("\n".join(block), comments=[block_name])
        for scenario in scenarios
        for block_name, block in scenario.global_code_blocks.items()
    }

    return [
        py.Import(["re"], comments=[LOCUSTFILE_COMMENT]),
        *locust_detected_version(),
        *locust_imports(),
        *locust_classes(scenarios),
        *global_code_blocks.values(),
    ]


def locustfile_lines(
    scenarios: Sequence[Scenario], program_plugins: Sequence[Plugin]
) -> Iterator[str]:
    """
    Converts the provided scenarios into a stream of Python statements
    and iterate on the resulting lines.
    """
    program = plug.apply(program_plugins, locust_program(scenarios))
    for stmt in program:
        for line in stmt.lines():
            yield str(line)


def locustfile(scenarios: Sequence[Scenario]) -> str:
    """
    Simple wrapper around locustfile_lines joining all lines with "\n".

    This function is deprecated and will be removed in a future version.
    Do not rely on it.
    Reason: It does not provide significant value over locustfile_lines and has
    a less clear name and a less flexible API. It does not support new
    generation plugins contracts like OnPythonProgram.
    Deprecated since: v1.0.2.
    """
    warnings.warn(DeprecationWarning("locustfile: use locustfile_lines instead"))
    return "\n".join(locustfile_lines(scenarios, ()))
