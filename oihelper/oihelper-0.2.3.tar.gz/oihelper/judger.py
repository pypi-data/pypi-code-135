from collections import namedtuple
import difflib
import subprocess
import time
from threading import Thread
from typing import TextIO

from psutil._common import bytes2human  # type: ignore
from psutil import Process, NoSuchProcess  # type: ignore


pmem = namedtuple("pmem", ["rss", "vms"])


class Judger(object):
    def __init__(self, compiler_path: str = "g++") -> None:
        super().__init__()
        self.compiler_path = compiler_path.replace(" ", "\\ ")

    def _assert_equal(self, output: str, expected: str) -> dict[str, bool | str | int]:
        diffs = difflib.ndiff(output.rstrip(), expected.rstrip())

        position = -1
        for i, diff in enumerate(diffs):
            if diff[0] != " ":
                position = i
                break

        if position == -1:
            return {"passed": True, "position": -1}

        return {"passed": False, "position": position}

    def _monitor_memory_usage(
        self, process: subprocess.Popen[bytes], results: list[pmem]
    ) -> list[tuple]:
        psutil_process = Process(process.pid)
        while process.poll() is None:
            try:
                results.append(psutil_process.memory_info())
            except NoSuchProcess:
                break
            time.sleep(0.01)
        return results

    def compile_program(self, program_path: str, output_path: str = "./output") -> None:
        compile_process = subprocess.Popen(
            [self.compiler_path, program_path, "-o", output_path],
        )
        compile_process.wait()
        if compile_process.returncode != 0:
            raise RuntimeError(
                "Failed to compile. "
                "There should be more error messages produced by the compiler above."
            )

    def run_program(
        self,
        exec_path: str,
        stdin: TextIO,
        stdout: TextIO,
        max_timeout: float = 1,
        max_memory: int = 1024 * 1024 * 128,
    ) -> None:
        runner_process = subprocess.Popen(
            exec_path,
            stdin=stdin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        start_time = time.time()
        results: list[pmem] = []
        memory_process = Thread(
            target=self._monitor_memory_usage, args=(runner_process, results)
        )
        memory_process.start()

        try:
            program_output = (
                runner_process.communicate(timeout=max_timeout)[0]
                .decode("utf-8")
                .rstrip("\n")
            )
            time_cost = time.time() - start_time
        except subprocess.TimeoutExpired:
            runner_process.kill()
            return {
                "status": "TLE",
                "details": f"Program ran longer than the expected {max_timeout}s.",
            }

        if runner_process.returncode != 0:
            return {
                "status": "RE",
                "details": f"Program exited with non-zero code {runner_process.returncode}.",
            }

        max_memory_usage = -1
        for result in results:
            max_memory_usage = max(result.rss, max_memory_usage)
        readable_memory_usage = bytes2human(max_memory_usage)

        if max_memory_usage > max_memory:
            return {
                "status": "MLE",
                "details": f"Exceeded maximum memory usage. "
                f"Reading {readable_memory_usage}, expected under {bytes2human(max_memory)}.",
            }

        expected_output = stdout.read().rstrip("\n")
        program_output_original = program_output
        program_output = program_output.splitlines(True)
        for i, expected in enumerate(expected_output.splitlines(True)):
            if i >= len(program_output):
                return {
                    "status": "WA",
                    "details": f"Wrong answer on line {i} column 0, "
                    f"reading EOF, expected {expected[0]}.",
                    "program_output": program_output_original,
                    "expected_output": expected_output,
                }
            output = program_output[i]
            result = self._assert_equal(output, expected)
            if not result["passed"]:
                pos = result["position"]
                cur_output = output[pos] if pos < len(output) else "EOF"
                cur_expected = expected[pos] if pos < len(expected) else "EOF"
                return {
                    "status": "WA",
                    "details": f"Wrong answer on line {i} column {pos}, "
                    f"reading {cur_output}, expected {cur_expected}.",
                    "program_output": program_output_original,
                    "expected_output": expected_output,
                }

        return {
            "status": "AC",
            "details": {"time_cost": time_cost, "memory_usage": readable_memory_usage},
        }


if __name__ == "__main__":
    helper = Judger("g++-11")
    helper.compile_program("./test.cpp")
    helper_result = helper.run_program(
        "./output",
        open("./test.in", "r", encoding="utf-8"),
        open("./test.out", "r", encoding="utf-8"),
    )
    print(helper_result)
