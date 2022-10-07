import threading


class _Context(type):
    _instances = {}
    _thread_local = threading.local()
    _thread_local.trace_id = ""

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Context, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    @property
    def trace_id(self):
        return getattr(self._thread_local, 'trace_id', None)

    @trace_id.setter
    def trace_id(self, value):
        self._thread_local.trace_id = value


class Context(_Context('SingletonMeta', (object,), {})):
    pass


ctx = Context()
