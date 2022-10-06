import asyncio
import concurrent.futures._base
import traceback
from contextlib import suppress
from random import randint


def get_or_create_event_loop():
    try:
        loop = asyncio.get_event_loop()
    except Exception as e:
        loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop


persistent_tasks = {}

LOGGING = False

class AsyncioSafeTasks():

    def __init__(self, *args, parent_task_manager=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._tasks = {}
        self._parent_manager = parent_task_manager
        self._discarded = False


    def create_id(self):
        return randint(0, 100000)


    def create_task(self, awaitable, id=None, persistent=False, callback=None, **kwargs):
        # if getattr(self, 'id', None) == 'binanceusdm':
        #     print('wow')
        if self._discarded:
            LOGGING and print(f'{self} is already discarded')
            return
        if self._parent_manager:
            return self._parent_manager(awaitable, id=id, persistent=persistent, callback=callback, **kwargs)
        id = id or self.create_id()
        task = asyncio.create_task(awaitable)
        if persistent:
            persistent_tasks[id] = task
        else:
            self._tasks[id] = task

        def on_done(task):
            self.discard_task(task)

        task._id = id
        task.add_done_callback(on_done)
        return task


    def discard_task(self, task):
        v = self._discard_task(task)
        LOGGING and print(f'discarded task {task._id}: {v}')
        return v

    def _discard_task(self, task):
        id = task._id
        if id in self._tasks:
            del self._tasks[id]
            return True
        if id in persistent_tasks:
            del persistent_tasks[id]
            return True
        if self._parent_manager:
            return self._parent_manager.discard_task(id)
        return False


    def cleanup_tasks(self, **kwargs):
        self._discarded = True
        if self._parent_manager:
            self._parent_manager.cleanup_tasks(**kwargs)
        for id, task in dict(self._tasks).items():
            task.cancel()
            del self._tasks[id]
        self._tasks = {}


    def cancel_task(self, task):
        v = self._cancel_task(task)
        LOGGING and print(f'cancelled task {task._id}: {v}')
        return v

    def _cancel_task(self, task, **kwargs):
        id = task._id
        if id in self._tasks:
            self._tasks[id].cancel()
            del self._tasks[id]
            return True
        if id in persistent_tasks:
            persistent_tasks[id].cancel()
            del persistent_tasks[id]
            return True
        if self._parent_manager:
            return self._parent_manager.discard_task(id)
        return False

    async def timeout_tasks(self, tasks, timeout, on_error=None):
        return

    def __del__(self):
        LOGGING and print('asyncio manager being deleted')
        self.cleanup_tasks()



def asyncio_safe(cleanup=None):
    def async_safe_warpper(function):
        async def decorated(*args, **kwargs):
            try:
                return await function(*args, **kwargs)
            except concurrent.futures._base.CancelledError as e:
                cleanup and cleanup(*args, **kwargs)
                return
            except Exception as e:
                traceback.print_exc()
                cleanup and cleanup(*args, **kwargs)
                return
        return decorated
    return async_safe_warpper


