import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb

from ..utils import Utils


class ScheduledTask:
    def __init__(self, stub, scheduled_task):
        st = pb.ScheduledTask()
        st.CopyFrom(scheduled_task)
        self._scheduled_task = st
        self._stub = stub

    @property
    def id(self):
        return self._scheduled_task.id

    @property
    def name(self):
        return self._scheduled_task.name

    @property
    def description(self):
        return self._scheduled_task.description

    @description.setter
    def description(self, value: str):
        update_request = pb.ScheduledTaskUpdateRequest(
            scheduled_task_id=self._scheduled_task.id,
            description=value,
            updated_fields=["description"],
        )
        self._stub.UpdateScheduledTask(update_request)
        self._refresh()

    @property
    def schedule(self):
        return self._scheduled_task.schedule

    @schedule.setter
    def schedule(self, value: str):
        update_request = pb.ScheduledTaskUpdateRequest(
            scheduled_task_id=self._scheduled_task.id,
            schedule=value,
            updated_fields=["schedule"],
        )
        self._stub.UpdateScheduledTask(update_request)
        self._refresh()

    def delete(self):
        request = pb.ScheduledTaskId(scheduled_task_id=self._scheduled_task.id)
        self._stub.DeleteScheduledTask(request)

    def _refresh(self):
        request = pb.ScheduledTaskId(scheduled_task_id=self._scheduled_task.id)
        response = self._stub.GetScheduledTask(request)
        self._scheduled_task = response.task

    def __repr__(self):
        return Utils.pretty_print_proto(self._scheduled_task)
