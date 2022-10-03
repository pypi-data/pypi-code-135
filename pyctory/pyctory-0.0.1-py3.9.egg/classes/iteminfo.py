from typing import Dict, List, Tuple, Union

UNDO = 0
PROC = 1
DONE = 2


class ItemInfo:
    def __init__(self,
                 process_list: List[str],
                 arrival: int = -1,
                 process_time: Dict[str, int] = {},
                 typ: Union[str, int, None] = None
                 ) -> None:
        self.arrival: int = arrival
        """ process name: state """
        self.states: Dict[str, int] = {}
        """ process name: (arrival time, finished time, real processing time) """
        self.times: Dict[str, Tuple[int, int, int]] = {}
        """ process name: (processor, prescribed processing time, position) """
        self.processor: Dict[str, Tuple[str, int, int]] = {}
        """ process in processing """
        self.curr_process: str = None
        """ type """
        self.typ = typ
        """ time entering Sink """
        self.done_time: int = -1

        for process in process_list:
            self.states[process] = UNDO
            self.times[process] = (-1, -1, -1)
            self.processor[process] = (None, -1, -1)

        if len(process_time) != 0:
            for k, v in process_time.items():
                self.processor[k] = (None, v, -1)

    def start_process(self, process: str, _time: int,
                      processor: str, pos: int) -> None:
        assert self.states[process] == UNDO
        assert self.times[process] == (-1, -1, -1)
        assert self.processor[process][0] is None
        assert self.processor[process][2] == -1
        assert self.curr_process is None

        self.states[process] = PROC
        self.times[process] = (_time, self.times[process]
                               [1], self.times[process][2])
        self.processor[process] = (processor, self.processor[process][1], pos)
        self.curr_process = process

    def done_process(self, _time: int) -> None:
        assert self.curr_process is not None
        assert self.states[self.curr_process] == PROC
        assert self.times[self.curr_process][0] != -1
        assert self.processor[self.curr_process][0] is not None

        self.states[self.curr_process] = DONE
        self.times[self.curr_process] = (
            self.times[self.curr_process][0],
            _time,
            _time - self.times[self.curr_process][0]
        )
        self.curr_process = None
