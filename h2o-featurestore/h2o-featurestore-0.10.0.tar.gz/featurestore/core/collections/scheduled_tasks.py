import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb
from ai.h2o.featurestore.api.v1.CoreService_pb2_grpc import CoreServiceStub

from ..entities.scheduled_task import ScheduledTask


class ScheduledTasks:
    def __init__(self, stub: CoreServiceStub, feature_set):
        self._stub = stub
        self._feature_set = feature_set

    def create_ingest_task(self, request: pb.ScheduleTaskRequest):
        response = self._stub.ScheduleIngestJob(request)
        return ScheduledTask(self._stub, response.task)

    def tasks(self):
        request = pb.ListScheduledTasksRequest()
        request.feature_set_id = self._feature_set.id
        while request:
            response = self._stub.ListScheduledTasks(request)
            if response.next_page_token:
                request.page_token = response.next_page_token
            else:
                request = None
            for task in response.tasks:
                yield ScheduledTask(self._stub, task)

    def get(self, task_id: str):
        request = pb.ScheduledTaskId(scheduled_task_id=task_id)
        response = self._stub.GetScheduledTask(request)
        return ScheduledTask(self._stub, response.task)
