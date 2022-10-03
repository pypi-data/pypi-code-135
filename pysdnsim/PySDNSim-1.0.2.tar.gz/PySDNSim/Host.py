class Host:
    """
    This class represents a host.
    """
    _cpus: int
    _ram: int
    _bw: int
    _storage: int
    _static_power: float
    _max_power: float
    _vm_scheduler: str
    _replicas: int

    def __init__(self, cpus: int, ram: int, bw: int, storage: int, static_power: float, max_power: float,
                 replicas: int, vm_scheduler: str = "SpaceShared"):
        """
        Host with given id, cpus, ram, bw, storages, static_power and max_power.
        :param cpus: number of cpus.
        :param ram: size of ram.
        :param bw: capacity of bandwidth.
        :param storage: size of storages.
        :param static_power: idle power.
        :param max_power: maximum power.
        :param replicas: number of replicas.
        :param vm_scheduler: vm scheduler, default to SpaceShared.
        """
        self._cpus = cpus
        self._ram = ram
        self._bw = bw
        self._storage = storage
        self._static_power = static_power
        self._max_power = max_power
        self._replicas = replicas
        self._vm_scheduler = vm_scheduler


    @property
    def cpus(self):
        return self._cpus

    @property
    def ram(self):
        return self._ram

    @property
    def bw(self):
        return self._bw

    @property
    def storage(self):
        return self._storage

    @property
    def static_power(self):
        return self._static_power

    @property
    def max_power(self):
        return self._max_power

    @property
    def vm_scheduler(self):
        return self._vm_scheduler

    @property
    def replicas(self):
        return self._replicas
