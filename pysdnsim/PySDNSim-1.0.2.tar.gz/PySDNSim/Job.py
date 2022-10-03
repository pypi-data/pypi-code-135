class Job:
    """
    Represents a single job.
    """
    _ms: int
    _length: int
    _file_size: int
    _schedule: int

    def __init__(self, ms: int, length: int, file_size: int, schedule: int):
        """
        Create a new Job with the given ms, length, file_size, schedule specified.

        :param ms: id of microservice.
        :param length: length of the job in MIPS.
        :param file_size: input/output size of the job in bytes.
        :param schedule: schedule of the job.
        """
        self._ms = ms
        self._length = length
        self._file_size = file_size
        self._schedule = schedule

    @property
    def ms(self):
        return self._ms

    @property
    def length(self):
        return self._length

    @property
    def file_size(self):
        return self._file_size

    @property
    def schedule(self):
        return self._schedule
