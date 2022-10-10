from dataclasses import dataclass, field, replace
from functools import reduce
from timeit import repeat
from copy import copy
from typing import NamedTuple
from proflow.internal_state import Model_State_Shape
from proflow.helpers import rgetattr, rsetattr
from proflow.process_ins_and_outs import get_inputs_from_process, map_result_to_state
from proflow.Objects import I, Process
from proflow.tests.mocks import Mock_Config_Shape, Mock_External_State_Shape, \
    Mock_Model_State_Shape, Mock_Parameters_Shape


def test_get_inputs_from_process():
    process = Process(
        func=lambda: [1, 2, 3],
        config_inputs=lambda config: [
            I(config.foo, as_='x'),
        ],
        state_inputs=lambda state: [
            I(state.b),
            I(state.a, as_='y'),
        ],
        state_outputs=lambda prev_state, result: [
            rsetattr(prev_state, 'nested.na', result[0]),
        ],
        args=[1, 2, 3]
    )

    args, kwargs = get_inputs_from_process(
        process,
        Mock_Model_State_Shape(a=2.1, b=4.1),
        Mock_Config_Shape(),
        Mock_Parameters_Shape(),
        Mock_External_State_Shape(),
    )

    assert args == [1, 2, 3, 4.1]
    assert kwargs == {'x': 1, 'y': 2.1}


def test_map_result_to_state():
    process = Process(
        func=lambda: {'out': 'zzz'},
        config_inputs=lambda config: [
            I(config.foo, as_='x'),
        ],
        state_inputs=lambda state: [
            I(state.b),
            I(state.a, as_='y'),
        ],
        state_outputs=[
            I('out', as_='nested.na'),
        ],
    )

    result = {'out': 'zzz'}

    prev_state = Mock_Model_State_Shape(a=2.1, b=4.1)
    state_out = map_result_to_state(
        prev_state,
        process.state_outputs,
        result,
    )

    assert state_out.nested.na == 'zzz'


def test_map_result_to_state_timeit():
    process = Process(
        func=lambda: {'out': 'zzz'},
        config_inputs=lambda config: [
            I(config.foo, as_='x'),
        ],
        state_inputs=lambda state: [
            I(state.b),
            I(state.a, as_='y'),
        ],
        state_outputs=[
            I('out', as_='nested.na'),
        ],
    )

    result = {'out': 'zzz'}

    prev_state = Mock_Model_State_Shape(a=2.1, b=4.1)
    t1 = min(repeat(lambda: map_result_to_state(
        prev_state,
        process.state_outputs,
        result,
    ), number=1000, repeat=20))

    assert 0.00159 < t1 < 0.008


def test_namedtuple_version():
    class Child(NamedTuple):
        bar: str = 'bar'

    class Foo(NamedTuple):
        a: int = 1
        b: int = 3
        c: Child = Child()

    foo = Foo()
    foob = foo._replace(c=foo.c._replace(bar='hello'))
    assert foob.c.bar == 'hello'
    assert foo.c.bar == 'bar'


def test_dataclass_version():
    @dataclass(frozen=True)
    class Child():
        bar: str = 'bar'

    @dataclass(frozen=True)
    class Foo():
        a: int = 1
        b: int = 3
        c: Child = field(default_factory=lambda: Child())

    foo = Foo()
    foob = replace(foo, c=replace(foo.c, bar="hello"))
    assert foob.c.bar == 'hello'
    assert foo.c.bar == 'bar'


def test_dataclass_version_mapping():
    @dataclass(frozen=True)
    class SubChild:
        low: str = 'hi'

    @dataclass(frozen=True)
    class Child:
        bar: str = 'bar'
        subbar: SubChild = field(default_factory=lambda: SubChild())

    @dataclass(frozen=True)
    class Foo:
        a: int = 1
        b: int = 3
        c: Child = field(default_factory=lambda: Child())

    foo = Foo()
    target = 'c.subbar.low'

    target_split = target.split('.')
    target_indexed = reversed(list(enumerate(target_split[0:-1])))

    def build_up_args(acc, tar):
        [i, t] = tar
        # [obj, args] = acc
        print(acc, i, t)
        t_2_h = '.'.join(target_split[0:i+1])
        new_args = {t: f'replace(foo.{t_2_h}, {acc})'}
        attr = rgetattr(foo, t_2_h)
        new_args = {t: replace(attr, **acc)}
        # new_obj = replace(obj, )
        return new_args

    val = "zzz"
    out = reduce(build_up_args, target_indexed, {target_split[-1]: val})
    final_state = replace(foo, **out)
    print(final_state)
    # foob = replace(foo, c=replace(foo.c, bar="hello"))
    assert final_state.c.subbar.low == val
    assert foo.c.subbar.low == 'hi'


def test_dataclass_version_mapping_func():
    @dataclass(frozen=True)
    class SubChild:
        low: str = 'hi'

    @dataclass(frozen=True)
    class Child:
        bar: str = 'bar'
        subbar: SubChild = field(default_factory=lambda: SubChild())

    @dataclass(frozen=True)
    class Foo:
        a: int = 1
        b: int = 3
        c: Child = field(default_factory=lambda: Child())

    def replace_state_val(initial_state, target, val):
        target_split = target.split('.')
        target_indexed = reversed(list(enumerate(target_split[0:-1])))

        def build_up_args(acc, tar):
            [i, t] = tar
            t_2_h = '.'.join(target_split[0:i+1])
            new_args = {t: f'replace(foo.{t_2_h}, {acc})'}
            attr = rgetattr(initial_state, t_2_h)
            new_args = {t: replace(attr, **acc)}
            # new_obj = replace(obj, )
            return new_args

        out = reduce(build_up_args, target_indexed, {target_split[-1]: val})
        final_state = replace(initial_state, **out)
        return final_state

    foo = Foo()
    val = 'zzz'
    foo_updated = replace_state_val(foo, 'c.subbar.low', val)
    # foob = replace(foo, c=replace(foo.c, bar="hello"))
    assert foo_updated.c.subbar.low == val
    assert foo.c.subbar.low == 'hi'

    t1 = min(repeat(lambda: replace_state_val(foo, 'c.subbar.low', val), number=1000, repeat=20))
    assert 0.002 < t1 < 0.01
