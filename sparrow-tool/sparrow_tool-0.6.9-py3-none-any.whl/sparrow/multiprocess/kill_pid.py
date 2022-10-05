from typing import Tuple, List, NamedTuple
import psutil


class ProcessInfo(NamedTuple):
    port: int
    process: psutil.Process


def get_processes(ports: List[int]) -> List[ProcessInfo]:
    processes = set()
    for process in psutil.process_iter():
        try:
            conns = process.connections(kind="inet")
        except (psutil.AccessDenied, psutil.ZombieProcess):
            continue

        for conn in conns:
            port = conn.laddr.port
            if port in ports:
                processes.add(ProcessInfo(port=port, process=process))

    return sorted(processes, key=lambda p: p.port)


def kill_ports(ports: Tuple[int], just_view: bool = False) -> int:
    processes = get_processes(ports)
    if not processes:
        print("🙃 Do not find process by the given ports")
        return False

    for pinfo in processes:
        emoji = "👁️" if just_view else "☠️🔪"
        process = pinfo.process
        if not just_view:
            process.kill()
        print(
            f"{emoji}: {process.name()} (pid {process.pid}) "
            f"on port {pinfo.port}",
        )
    return True if processes else False
