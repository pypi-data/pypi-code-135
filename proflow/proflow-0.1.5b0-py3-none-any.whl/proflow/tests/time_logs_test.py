import pytest
import numpy as np

from proflow.helpers import rgetattr
from proflow.tests.mocks import Mock_Config_Shape, Mock_External_State_Shape, \
    Mock_Model_State_Shape, Mock_Nested_State, Mock_Parameters_Shape
from proflow.ProcessRunnerCls import ProcessRunner
from unittest.mock import MagicMock, patch
from vendor.helpers.list_helpers import flatten_list, filter_none

from ..ProcessRunner import Process, I


def process_add(x, y):
    return x + y


def process_add_complex(x, y):
    total = 0
    for i in range(10000):
        total += x + y + i
    return total


process_runner = ProcessRunner(
    Mock_Config_Shape(),
    Mock_External_State_Shape(),
    Mock_Parameters_Shape(),
    True,
)


@pytest.fixture(scope="module", autouse=True)
def _():
    with patch('proflow.ProcessRunner.Model_State_Shape', side_effect=Mock_Model_State_Shape) \
            as Mocked_State_Shape:
        Mocked_State_Shape.__annotations__ = Mock_Model_State_Shape.__annotations__
        yield Mocked_State_Shape


@pytest.fixture(scope="module", autouse=True)
def __():
    with patch('proflow.ProcessRunner.Config_Shape', return_value=Mock_Config_Shape) as _fixture:
        yield _fixture


@pytest.fixture(scope="module", autouse=True)
def ____():
    with patch('proflow.ProcessRunner.Parameters_Shape', return_value=Mock_Parameters_Shape) \
            as _fixture:
        yield _fixture


@pytest.fixture(scope="module", autouse=True)
def ______():
    with patch('proflow.ProcessRunner.External_State_Shape',
               return_value=Mock_External_State_Shape) \
            as _fixture:
        yield _fixture


def test_that_processRunnerCls_logs_time_for_each_process():
    state = Mock_Model_State_Shape(a=2.1, b=4.1)
    processes = flatten_list([
        Process(
            func=process_add,
            config_inputs=lambda config: [
                I(config.foo, as_='x'),
                I(config.bar, as_='y'),
            ],
            state_outputs=[
                I('result', as_='c'),
            ],
        ),
        Process(
            func=process_add_complex,
            config_inputs=lambda config: [
                I(config.foo, as_='x'),
            ],
            state_inputs=lambda state: [
                I(state.a, as_='y'),
            ],
            state_outputs=[
                I('result', as_='d'),
            ],
        ),
    ])
    run_processes = process_runner.initialize_processes(processes)
    state_2 = run_processes(initial_state=state)
    print(process_runner.time_logs)
    assert state_2.c == 4
    assert state_2.d == 50026000.00000531
    time_logs = dict(process_runner.time_logs)
    assert time_logs['process_add'] < time_logs['process_add_complex']
