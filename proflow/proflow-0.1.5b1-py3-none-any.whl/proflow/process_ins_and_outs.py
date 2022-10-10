from dataclasses import is_dataclass, replace
from functools import reduce
from typing import Any, Callable, List
from copy import deepcopy

from .helpers import rgetattr, rsetattr
from .ProcessRunner import Process, format_with_variables, get_result
from .internal_state import Model_State_Shape
from .config import Config_Shape
from .external_state import External_State_Shape
from .parameters import Parameters_Shape


def get_inputs_from_process(
    process: Process,
    prev_state: Model_State_Shape,
    config: Config_Shape,
    parameters: Parameters_Shape,
    external_state: External_State_Shape,
) -> List[Any]:
    row_index = rgetattr(prev_state, 'temporal.row_index', 0)
    config_args = process.config_inputs(config)
    # parameters_args = process.parameters_inputs(parameters)
    # TODO: we need a better way of accessing current row index
    external_state_args = process.external_state_inputs(
        external_state, row_index,
    )
    additional_args = process.additional_inputs()
    state_args = process.state_inputs(prev_state)
    # additional_inputs_tuples = [astuple(a)[0:2] for a in additional_inputs]
    args = process.args
    # kwargs = {**config_args, **state_args} # fastest method
    kwargs = {i.as_: i.from_ for i in config_args +
              state_args + additional_args + external_state_args if i.as_ is not None}
    args = process.args + [i.from_ for i in config_args +
                           state_args + additional_args + external_state_args
                           if i.as_ is None]
    return args, kwargs


def get_new_val(attr, acc):
    if is_dataclass(attr):
        return replace(attr, **acc)
    if isinstance(attr, list):
        list_copy = deepcopy(attr)
        for k, v in acc.items():
            list_copy[int(k)] = v
        return list_copy


def replace_state_val(initial_state, target, val):
    target_split = target.split('.')
    target_indexed = reversed(list(enumerate(target_split[0:-1])))

    def build_up_args(acc, tar):
        [i, t] = tar
        t_2_h = '.'.join(target_split[0:i+1])
        new_args = {t: f'replace(foo.{t_2_h}, {acc})'}
        attr = rgetattr(initial_state, t_2_h)
        new_val = get_new_val(attr, acc)
        new_args = {t: new_val}
        # new_obj = replace(obj, )
        return new_args

    out = reduce(build_up_args, target_indexed, {target_split[-1]: val})
    final_state = replace(initial_state, **out)
    return final_state


def map_result_to_state(
    prev_state: Model_State_Shape,
    output_map: Callable[[any, object], object],
    result,
) -> Model_State_Shape:
    """Update the state based on an output mapping.

    Parameters
    ----------
    output_map : Callable[[any, object], object]
        [description]
    prev_state : Model_State_Shape
        [description]
    result : [type]
        [description]

    Returns
    -------
    Model_State_Shape
        [description]
    """
    # active_state = deepcopy(prev_state)
    active_state = prev_state
    # !!!WARNING MUTATING STATE HERE!!!
    for o in output_map:
        result_item = rgetattr(result, o.from_) if o.from_ != '_result' else result
        active_state = replace_state_val(active_state, o.as_, result_item)
    return active_state
