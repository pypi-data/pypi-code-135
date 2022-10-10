import argparse
import logging
import marshal
import shutil
import subprocess as sp
from collections import defaultdict, namedtuple
from dataclasses import dataclass
from pathlib import Path

Call = namedtuple(
    "Call",
    ["filename", "lineno", "name", "status", "elapsed"],
    defaults=[0],
)

ALLCALLS = {}


@dataclass
class FunctionCall:
    """only one per function name"""

    filename: str
    name: str
    lineno: int
    ncalls: int = 0
    cumtime: float = 0.0
    tottime: float = 0.0

    def __post_init__(self):
        self._key = self.name
        ALLCALLS[self._key] = self
        self._parents = []
        self._open_parents = []
        self._children = []  # which functions we called from it
        self._profile = {}  # built by self.finalize()

    def __eq__(self, other):
        return self._key == other._key

    def __repr__(self):
        return f"<{self._key}: ncalls={self.ncalls}  cumtime={self.cumtime:.3f}>"

    def __hash__(self):
        return hash(self.name)

    def startcall(self, caller_key, ref_cumtime):
        self.ncalls += 1
        self._open_parents.append((caller_key, ref_cumtime))
        if caller_key:
            ALLCALLS[caller_key]._children.append(self)

    def endcall(self, cumtime):
        caller_key, ref_cumtime = self._open_parents.pop(-1)
        # cumtime is the total time spent in a single function call
        # **including** subfunctions
        cumtime -= ref_cumtime
        self._parents.append((caller_key, cumtime))
        self.cumtime += cumtime
        # remove time spent in this function from caller.tottime
        if caller_key:
            ALLCALLS[caller_key].tottime -= cumtime

    def finalize(self):
        # `self.tottime` is a negative number
        self.tottime = self.cumtime + self.tottime
        # investigate callers
        assert len(self._open_parents) == 0
        _parents = {}
        _data = [self.ncalls, self.ncalls, self.tottime, self.cumtime, _parents]
        for i, (caller_key, call_time) in enumerate(self._parents):
            # call_time is the time spent in self due to caller call
            # when self is a subroutine of call
            if not caller_key:
                continue
            caller = ALLCALLS[caller_key]
            # calculate portion of time spent in caller due to self
            _key = (caller.filename, caller.lineno, caller.name)
            if _key in _parents:
                count_callers = list(_parents[_key])
            else:
                count_callers = [0, 0, 0.0, 0.0]
            count_callers[0] += 1
            count_callers[1] += 1
            count_callers[2] += 0
            count_callers[3] += call_time
            _parents[(caller.filename, caller.lineno, caller.name)] = tuple(
                count_callers
            )
        self.data = tuple(_data)


def count():
    counter = defaultdict(list)
    callers = [None]
    while True:
        call = yield counter
        call_key = call.name
        if call_key not in ALLCALLS:
            _ = FunctionCall(call.filename, call.name, call.lineno)
        fcall = ALLCALLS[call_key]
        if call.status == "begin":
            fcall.startcall(callers[-1], call.elapsed)
            callers.append(ALLCALLS[call_key]._key)
        else:
            callers.pop(-1)
            fcall.endcall(call.elapsed)


def finalize():
    """close all functions"""
    for callkey, function in ALLCALLS.items():
        function.finalize()


def process_allcounts():
    """return data ready to be marshalled"""
    finalize()
    data = {(f.filename, f.lineno, f.name): f.data for f in ALLCALLS.values()}
    return data


def _processf04_ltd(filename, values):
    keys = ("lineno", "name", "status", "elapsed")
    d = dict(zip(keys, values))
    d["filename"] = filename
    d["elapsed"] = float(d["elapsed"])
    return d


def _processf04(filename):
    """
    return an ordered list of fucntion call and ends
    filename: pathlib.Path to F04 file
    """
    _filename = Path(filename).expanduser()
    filename = _filename.name
    with open(_filename, "r") as fh:
        lines = fh.readlines()  # if (sl := l.strip()) != ""]
    # print("\n".join(lines[135:150]))
    timing = []
    current_link = None
    lcid = None
    call_stack = []
    cumulated = 0
    link_offset = 0
    for lineno, line in enumerate(lines, 1):
        line = line.strip()
        if line == "":
            continue
        if line.startswith(">>"):
            link_offset = cumulated
            current_link = line.strip(">>").split(":")[0]
            status = current_link.split()[-1]
            current_link = " ".join(current_link.split()[:-1])
            function = current_link
            if status == "END":
                status = "end"
                current_link = None
                call_stack.pop(-1)
                cumulated = cumulated
            else:
                status = "begin"
                cumulated = cumulated
                call_stack.append(current_link)
            # register LINK timing
            timing.append(
                _processf04_ltd(
                    filename,
                    (
                        lineno,
                        function,
                        status,
                        cumulated,
                    ),
                )
            )
            continue
        # =====================================================================
        # some special lines
        # =====================================================================
        if line.startswith("****"):
            lcid = int(line.split()[3])
            continue
        # skip first lines
        if not current_link:
            continue
        # =====================================================================
        # inner LINKS functions
        # =====================================================================
        func, status, _cumulated, *comment = line.split()
        cumulated = link_offset + float(_cumulated)
        if status == "END":
            status = "end"
            call_stack.pop(-1)
        else:
            status = "begin"
            call_stack.append(func)
        # if lcid:
        #     func += f"({lcid=})"
        timing.append(
            _processf04_ltd(
                filename,
                (
                    lineno,
                    func,
                    status,
                    cumulated,
                ),
            )
        )
    return timing


def processf04(filename):
    """process a f04 file and generate a cProfile .prof file"""
    filename = Path(filename).expanduser()
    schedule = _processf04(filename)
    counter = count()
    next(counter)
    for row in schedule:
        call = Call(**row)
        counter.send(call)
    data = process_allcounts()
    data_bytes = marshal.dumps(data)
    target = filename.parent / (filename.stem + ".prof")
    with open(target, "wb") as fh:
        fh.write(data_bytes)
    return target


def main():
    parser = argparse.ArgumentParser(description="description")
    parser.add_argument("source", type=str, help="path to F04")
    parser.add_argument("-s", "--snakeviz", action="store_true", help="starts snakeviz")
    args = parser.parse_args()
    prof_file = processf04(args.source)
    print(f"wrote {prof_file}")
    if args.snakeviz:
        snakeviz_bin = shutil.which("snakeviz")
        if snakeviz_bin:
            pid = sp.Popen([snakeviz_bin, prof_file])
            print(f"run snakeviz {pid=}")
        else:
            logging.error("snakeviz not found!")


if __name__ == "__main__":
    main()
