import typing
import threading
import time


import pymem


class Script:
    def __init__(self, callback: typing.Callable, enabled=False):
        self.callback = callback
        self.enabled = enabled

    def __repr__(self):
        return f"<Script {self.callback.__name__}: enabled={self.enabled}>"

    def __call__(self):
        return self.callback()


class ScriptEngine:
    def __init__(self, delay: float = 0.05):
        self.delay = delay
        self.should_run = False
        self.thread = threading.Thread(target=self.script_loop)
        self.scripts = []

    def __repr__(self):
        return (
            "<ScriptEngine"
            f" delay={self.delay}"
            f" should_run={self.should_run}"
            f" scripts={len(self.scripts)}"
            ">"
        )

    def start(self):
        self.should_run = True
        self.thread.start()

    def stop(self):
        self.should_run = False
        self.thread.join()

    def script_loop(self):
        while self.should_run:
            try:
                for script in self.scripts:
                    if script.enabled:
                        script()
            except (pymem.exception.MemoryReadError, pymem.exception.MemoryWriteError):
                continue
            except Exception as e:
                print(e)
                self.stop()
            time.sleep(self.delay)

    def register_script(self, callback: typing.Callable):
        script = Script(callback)
        self.scripts.append(script)
        return script
