import sys
import uuid
import json
from dataclasses import dataclass, field
import logging
from typing import Any, Callable, Dict, List, Optional, Union, cast, Tuple

import lattice.elastic.rendezvous.registry as rdzv_registry
from lattice.elastic.agent.server.api import WorkerSpec
from lattice.elastic.agent.server.lattice_agent import LatticeAgent
from lattice.elastic.multiprocessing import Std
from lattice.elastic.rendezvous import RendezvousParameters
from lattice.elastic.rendezvous.utils import parse_rendezvous_endpoint


stream_handler = logging.StreamHandler()
logging.basicConfig(level=logging.INFO, handlers=[stream_handler])




@dataclass
class LaunchConfig:
    """
    Creates a rendezvous config.

    Args:
        min_nodes: Minimum amount of nodes that the user function will
                        be launched on. Elastic agent ensures that the user
                        function start only when the min_nodes amount enters
                        the rendezvous.
        max_nodes: Maximum amount of nodes that the user function
                        will be launched on.
        nproc_per_node: On each node the elastic agent will launch
                            this amount of workers that will execute user
                            defined function.
        rdzv_backend: rdzv_backend to use in the rendezvous (zeus-adapter, etcd).
        rdzv_endpoint: The endpoint of the rdzv sync. storage.
        rdzv_configs: Key, value pair that specifies rendezvous specific configuration.
        rdzv_timeout: Legacy argument that specifies timeout for the rendezvous. It is going
            to be removed in future versions, see the note below. The default timeout is 900 seconds.
        rdzv_id: The unique run id of the job (if not passed a unique one will be
                deduced from run environment - flow workflow id in flow - or auto generated).
        role: User defined role of the worker (defaults to "trainer").
        max_restarts: The maximum amount of restarts that elastic agent will conduct
                    on workers before failure.
        monitor_interval: The interval in seconds that is used by the elastic_agent
                        as a period of monitoring workers.
        start_method: The method is used by the elastic agent to start the
                    workers (spawn, fork, forkserver).
        log_dir: base log directory where log files are written. If not set,
                one is created in a tmp dir but NOT removed on exit.
        redirects: configuration to redirect stdout/stderr to log files.
                Pass a single ``Std`` enum to redirect all workers,
                or a mapping keyed by local_rank to selectively redirect.
        tee: configuration to "tee" stdout/stderr to console + log file.
        metrics_cfg: configuration to initialize metrics.

    ..note:
        `rdzv_timeout` is a legacy argument that will be removed in future.
        Set the timeout via `rdzv_configs['timeout']`

    """

    min_nodes: int
    max_nodes: int
    nproc_per_node: int
    run_id: str = ""
    role: str = "default_role"
    rdzv_endpoint: str = ""
    rdzv_port: str = ""
    rdzv_backend: str = "etcd"
    rdzv_configs: Dict[str, Any] = field(default_factory=dict)
    rdzv_timeout: int = -1
    max_restarts: int = 3
    checkpoint_endpoint: str = None
    steps_per_checkpoint: int = 20
    monitor_interval: float = 5
    start_method: str = "spawn"
    log_dir: Optional[str] = None
    redirects: Union[Std, Dict[int, Std]] = Std.NONE
    tee: Union[Std, Dict[int, Std]] = Std.NONE
 
    def __post_init__(self):
        default_timeout = 900
        if self.rdzv_timeout != -1:
            self.rdzv_configs["timeout"] = self.rdzv_timeout
        elif "timeout" not in self.rdzv_configs:
            self.rdzv_configs["timeout"] = default_timeout


class elastic_launch:
    """
    Launches an torchelastic agent on the container that invoked the entrypoint.

        1. Pass the ``entrypoint`` arguments as non ``kwargs`` (e.g. no named parameters)/
           ``entrypoint`` can be a function or a command.
        2. The return value is a map of each worker's output mapped
           by their respective global rank.

    Usage

    ::

    def worker_fn(foo):
        # ...

    def main():
        # entrypoint is a function.
        outputs = elastic_launch(LaunchConfig, worker_fn)(foo)
        # return rank 0's output
        return outputs[0]

        # entrypoint is a command and ``script.py`` is the python module.
        ouptuts = elestic_launch(LaunchConfig, "script.py")(args)
        ouptuts = elestic_launch(LaunchConfig, "python")("script.py")
    """

    def __init__(
        self,
        config: LaunchConfig,
        entrypoint: Union[Callable, str, None],
    ):
        self._config = config
        self._entrypoint = entrypoint

    def __call__(self, *args):
        return launch_agent(self._config, self._entrypoint, list(args))


def _get_entrypoint_name(
    entrypoint: Union[Callable, str, None], args: List[Any]
) -> str:
    """Retrive entrypoint name with the rule:
    1. If entrypoint is a function, use ``entrypont.__qualname__``.
    2. If entrypoint is a string, check its value:
        2.1 if entrypoint equals to ``sys.executable`` (like "python"), use the first element from ``args``
            which does not start with hifen letter (for example, "-u" will be skipped).
        2.2 otherwise, use ``entrypoint`` value.
    3. Otherwise, return empty string.
    """
    if isinstance(entrypoint, Callable):  # type: ignore[arg-type]
        return entrypoint.__name__  # type: ignore[union-attr]
    elif isinstance(entrypoint, str):
        if entrypoint == sys.executable:
            return next((arg for arg in args if arg[0] != "-"), "")
        else:
            return entrypoint
    else:
        return ""


def _get_addr_and_port(
    rdzv_parameters: RendezvousParameters,
) -> Tuple[Optional[str], Optional[int]]:
    if rdzv_parameters.backend != "static":
        return (None, None)
    endpoint = rdzv_parameters.endpoint
    endpoint = endpoint.strip()
    if not endpoint:
        raise ValueError(
            "Endpoint is missing in endpoint. Try to add --master_addr and --master_port"
        )
    master_addr, master_port = parse_rendezvous_endpoint(endpoint, default_port=-1)
    if master_port == -1:
        raise ValueError(
            f"port is missing in endpoint: {endpoint}. Try to specify --master_port"
        )
    return (master_addr, master_port)


# pyre-fixme[56]: Pyre was not able to infer the type of the decorator
# torch.distributed.elastic.multiprocessing.errors.record.
def launch_agent(
    config: LaunchConfig,
    entrypoint: Union[Callable, str, None],
    args: List[Any],
) -> Dict[int, Any]:
    if not config.run_id:
        run_id = str(uuid.uuid4().int)
        logging.warning(f"config has no run_id, generate a new one: {run_id}")
        config.run_id = run_id

    entrypoint_name = _get_entrypoint_name(entrypoint, args)

    logging.info(
        f"Starting elastic_operator with launch configs:\n"
        f"  entrypoint       : {entrypoint_name}\n"
        f"  min_nodes        : {config.min_nodes}\n"
        f"  max_nodes        : {config.max_nodes}\n"
        f"  nproc_per_node   : {config.nproc_per_node}\n"
        f"  run_id           : {config.run_id}\n"
        f"  rdzv_backend     : {config.rdzv_backend}\n"
        f"  rdzv_endpoint    : {config.rdzv_endpoint}\n"
        f"  rdzv_port        : {config.rdzv_port}\n"
        f"  rdzv_configs     : {config.rdzv_configs}\n"
        f"  max_restarts     : {config.max_restarts}\n"
        f"  monitor_interval : {config.monitor_interval}\n"
    )

    rdzv_parameters = RendezvousParameters(
        backend=config.rdzv_backend,
        endpoint=config.rdzv_endpoint,
        port=config.rdzv_port,
        run_id=config.run_id,
        min_nodes=config.min_nodes,
        max_nodes=config.max_nodes,
        **config.rdzv_configs,
    )

    agent = None
    rdzv_handler = rdzv_registry.get_rendezvous_handler(rdzv_parameters)
    master_addr, master_port = _get_addr_and_port(rdzv_parameters)
    try:
        spec = WorkerSpec(
            role=config.role,
            local_world_size=config.nproc_per_node,
            entrypoint=entrypoint,
            args=tuple(args),
            rdzv_handler=rdzv_handler,
            max_restarts=config.max_restarts,
            monitor_interval=config.monitor_interval,
            master_addr=master_addr,
            master_port=master_port,
        )

        extra_env = {
            'RDZV_BACKEND': config.rdzv_backend,
            'RDZV_ENDPOINT': config.rdzv_endpoint,
            'MIN_NODES': str(config.min_nodes),
            'MAX_NODES': str(config.max_nodes),
            'RDZV_CONFIG': json.dumps(config.rdzv_configs),
            'NUM_LOCAL_DEVICES': str(config.nproc_per_node),
            'LATTICE_CHECKPOINT_ENDPOINT': config.checkpoint_endpoint,
            'LATTICE_STEPS_PER_CHECKPOINT': str(config.steps_per_checkpoint),
        }
        agent = LatticeAgent(
            spec=spec, start_method=config.start_method, log_dir=config.log_dir,
            extra_env=extra_env
        )

        agent.run()
    except Exception:
        raise
# Disabling since this closes the rendezvous no matter what
#    finally:
#        rdzv_handler.shutdown()
