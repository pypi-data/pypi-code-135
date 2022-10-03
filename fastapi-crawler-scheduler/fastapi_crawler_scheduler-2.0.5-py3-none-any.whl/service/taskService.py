from typing import Callable, Dict
import os

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import ConflictingIdError, JobLookupError
from apscheduler.util import datetime_to_utc_timestamp
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from apscheduler.util import obj_to_ref

try:
    import cPickle as pickle
except ImportError:  # pragma: nocover
    import pickle

try:
    from redis import Redis
except ImportError:  # pragma: nocover
    raise ImportError('RedisJobStore requires redis installed')

from fastapi_crawler_scheduler.utils.exception import SchedulerError
from fastapi_crawler_scheduler.service.dbRedisHelper import DbRedisHelper
from fastapi_crawler_scheduler.service.baseScheduler import BaseScheduler


class TaskScheduler(object):

    def __init__(self,
                 app: FastAPI,
                 project_name: str,
                 uuid_number: str,
                 ssl: bool,
                 thread_pool_size: int = 10,
                 job_coalesce: bool = True,
                 job_max_instance: int = 1,
                 job_misfire_grace_time: int = 10,
                 redis_host: str = "127.0.0.1",
                 redis_port: int = 6379,
                 redis_username: str = None,
                 redis_password: str = None,
                 ):
        self.app = app
        self.ssl = ssl
        self.project_name = project_name
        self.uuid_number = uuid_number
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.username = redis_username
        self.password = redis_password
        self.jobs_key = self.project_name + ':apscheduler:jobs:' + uuid_number + ":" + str(os.getpid())
        self.run_times_key = self.project_name + ':apscheduler:run_times:' + uuid_number + ":" + str(os.getpid())
        self.thread_pool_size = thread_pool_size
        self.job_coalesce = job_coalesce
        self.job_max_instance = job_max_instance
        self.job_misfire_grace_time = job_misfire_grace_time
        self.redis = Redis(
            host=self.redis_host,
            port=self.redis_port,
            username=self.username,
            password=self.password,
            decode_responses=True,
            ssl=ssl,
        )
        self.pickle_protocol = pickle.HIGHEST_PROTOCOL

        # 实现 scheduler 注册
        self.register_scheduler()
        self.register_redis_db = DbRedisHelper(
            project_name=self.project_name,
            redis_host=self.redis_host,
            redis_port=self.redis_port,
            username=self.username,
            password=self.password,
            ssl=self.ssl,
        )
        self.register_base_scheduler = BaseScheduler(
            project_name=self.project_name,
            redis_db=self.register_redis_db,
            scheduler=self.scheduler,
            uuid_number=self.uuid_number,
            redis_job_store=self.redis_job_store
        )
        self.register_async_task()

    def register_async_task(self) -> None:
        @repeat_every(seconds=5)
        def check_process() -> None:
            self.register_base_scheduler.check_process()

        @repeat_every(seconds=8)
        def check_scheduler_run() -> None:
            self.register_base_scheduler.run()

        @repeat_every(seconds=10)
        def check_redis_jobstores() -> None:
            self.register_base_scheduler.check_redis_jobstores()

        def scheduler_start():
            self.scheduler.start()

        def scheduler_shutdown():
            self.scheduler.shutdown()

        self.app.on_event("startup")(check_process)
        self.app.on_event("startup")(check_scheduler_run)
        self.app.on_event("startup")(check_redis_jobstores)
        self.app.on_event("startup")(scheduler_start)
        self.app.on_event("shutdown")(scheduler_shutdown)

    def add_job(self, job):
        if self.redis.hexists(self.jobs_key, job.id):
            raise ConflictingIdError(job.id)
        self.redis.hset(self.jobs_key, job.id, pickle.dumps(job.__getstate__(), self.pickle_protocol))
        if job.next_run_time:
            self.redis.zadd(self.run_times_key, {job.id: datetime_to_utc_timestamp(job.next_run_time)})

    def update_job(self, job):
        if not self.redis.hexists(self.jobs_key, job.id):
            raise JobLookupError(job.id)
        self.redis.hset(self.jobs_key, job.id, pickle.dumps(job.__getstate__(), self.pickle_protocol))
        if job.next_run_time:
            self.redis.zadd(self.run_times_key,
                            {job.id: datetime_to_utc_timestamp(job.next_run_time)})
        else:
            self.redis.zrem(self.run_times_key, job.id)

    def remove_job(self, job_id):
        if not self.redis.hexists(self.jobs_key, job_id):
            raise JobLookupError(job_id)
        self.redis.hdel(self.jobs_key, job_id)
        self.redis.zrem(self.run_times_key, job_id)

    def remove_all_jobs(self):
        self.redis.delete(self.jobs_key)
        self.redis.delete(self.run_times_key)

    def register_scheduler(self) -> None:
        redis_job_store = getattr(self.app, "redis_job_store", None)
        if redis_job_store is None:
            redis_job_store = RedisJobStore(
                host=self.redis_host,
                port=self.redis_port,
                username=self.username,
                password=self.password,
                jobs_key=self.jobs_key,
                run_times_key=self.run_times_key,
                ssl=self.ssl,
            )
            redis_job_store.add_job = self.add_job
            redis_job_store.update_job = self.update_job
            redis_job_store.remove_job = self.remove_job
            redis_job_store.remove_all_jobs = self.remove_all_jobs

        self.redis_job_store = redis_job_store
        setattr(self.app, "redis_job_store", self.redis_job_store)
        scheduler = getattr(self.app, "scheduler", None)
        if scheduler is None:
            scheduler = BackgroundScheduler()
            scheduler.configure(
                jobstores={
                    "default": self.redis_job_store
                },
                executors={
                    "default": ThreadPoolExecutor(
                        max_workers=self.thread_pool_size,
                    )
                },
                job_defaults={
                    "coalesce": self.job_coalesce,
                    "max_instance": self.job_max_instance,
                    "misfire_grace_time": self.job_misfire_grace_time,
                }
            )
        elif isinstance(scheduler, BackgroundScheduler):
            pass
        else:
            raise SchedulerError("FastAPI应用已经包含scheduler对象，但是该对象并非BackgroundScheduler")
        self.scheduler = scheduler
        setattr(self.app, "scheduler", self.scheduler)

    def add_task(
            self,
            func: Callable,
            job_id: str,
            trigger: str,
            crawler_info: Dict = None,
            **trigger_args
    ) -> None:
        '''
        :param trigger: interval 、 date or cron
        '''
        task_info = dict()
        task_info['func'] = obj_to_ref(func)
        task_info['job_id'] = job_id
        task_info['trigger'] = trigger
        task_info['crawler_info'] = crawler_info
        task_info['trigger_args'] = trigger_args
        self.register_base_scheduler.insert_task(task_info=task_info)

    # def update_task(
    #         self,
    #         func: Callable,
    #         job_id: str,
    #         trigger: str,
    #         crawler_info: Dict = None,
    #         **trigger_args
    # ) -> None:
    #     task_info = dict()
    #     task_info['func'] = obj_to_ref(func)
    #     task_info['job_id'] = job_id
    #     task_info['trigger'] = trigger
    #     task_info['crawler_info'] = crawler_info
    #     task_info['trigger_args'] = trigger_args
    #     self.register_base_scheduler.update_task(task_info=task_info)

    def delete_task(
            self,
            job_id: str,
    ) -> None:
        self.register_base_scheduler.delete_task(job_id=job_id)
