from datetime import datetime
from functools import partial, reduce
from typing import Callable, List, NamedTuple

from vendor.helpers.named_tuple_helpers import _replace_recursive

from .helpers import rgetattr
from .parameters import Parameters_Shape
from .external_state import External_State_Shape
from .config import Config_Shape
from .ProcessRunner import Process, format_with_variables, get_result, run_process
from .errors import Run_Process_Error


class ProcessRunner():
    """A class for initializing the process runner"""

    def __init__(self,
                 config_in: Config_Shape = Config_Shape(),
                 external_state_in: External_State_Shape = External_State_Shape(),
                 parameters_in: Parameters_Shape = Parameters_Shape(),
                 DEBUG_MODE: bool = False):
        self.config = config_in
        self.parameters = parameters_in
        self.external_state = external_state_in
        self.DEBUG_MODE = DEBUG_MODE
        self.time_logs = []

    # Define the process runner
    def run_processes(
            self,
            processes: List[Process] = None,
            initial_state: NamedTuple = None,  # initial state or parameters
    ) -> NamedTuple:
        """ Takes the initial state and a list of processes
        returns the new state as modified by the processes

        new state is the state after we have run all the processes
        the reduce function allows us to iterate through each function
        passing the state to the next
        """
        run_process_loaded = partial(self.run_process, config=self.config,
                                     parameters=self.parameters,
                                     external_state=self.external_state,
                                     DEBUG_MODE=self.DEBUG_MODE)
        new_state = reduce(run_process_loaded, processes, initial_state)
        return new_state

    def initialize_processes(
        self,
        processes: List[Process]
    ) -> Callable[[NamedTuple], NamedTuple]:
        """HOC component to assign processes to the run_processes function
        which can then be ran later with the state"""
        return partial(self.run_processes, processes)

    def run_process(
        self,
        prev_state: NamedTuple,  # Can be state or parameter
        process: Process,
        config: Config_Shape,
        parameters: Parameters_Shape,
        external_state: External_State_Shape,
        DEBUG_MODE: bool = False,
    ) -> NamedTuple:
        """Run a single process and output the updated state.
            The process object contains the function along with all the input
            and output targets.


            note: args from process are not garuanteed to be in the correct order

        Parameters
        ----------
        prev_state : NamedTuple
            Model state prior to this process being ran
        config : Config_Shape
            Model configuration
        parameters : Parameters_Shape
            Model derived parameters
        external_state : External_State_Shape
            External data
        DEBUG_MODE : bool, optional
            Debug processes when True, by default False

        Returns
        -------
        Model State
            Model State after process

        Raises
        ------
        Run_Process_Error
            Catches error that occur when running the process
        """
        if not process.gate:
            return prev_state
        try:
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


            # RUN PROCESS FUNC
            result = None
            if DEBUG_MODE:
                start_time = datetime.now()
                result = process.func(*args, **kwargs)
                end_time = datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000

                process_id = process.comment or process.func.__name__
                self.time_logs.append((process_id, execution_time))
            else:
                result = process.func(*args, **kwargs)



            # TODO: Implement new state out map
            # state_out = process.map_outputs(result, prev_state)
            # return state_out

            # kwrds, args = get_process_inputs(
            #     process,
            #     prev_state,
            #     config,
            #     parameters,
            #     external_state,
            #     DEBUG_MODE=DEBUG_MODE
            # )

            # # RUN PROCESS
            # result = process.func(*args, **kwrds)

            # CREATE NEW STATE
            output_map = process.state_outputs
            f = format_with_variables(config, prev_state, external_state, parameters, {})

            # iterate over output map and replace all values in state
            def update_state(prev_state, out):
                result_val = get_result(result, f(out.from_))
                # if process.debug >= 1:
                #     print(f'result_val: {result_val}')
                #     print(f'f(out.as_): {f(out.as_)}')
                return _replace_recursive(prev_state, f(out.as_), result_val)
            new_state = reduce(update_state, output_map, prev_state)
            return new_state

        except Exception as e:
            raise Run_Process_Error(process, e, prev_state) from e
