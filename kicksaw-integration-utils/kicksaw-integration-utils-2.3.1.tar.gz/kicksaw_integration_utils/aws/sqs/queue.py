from __future__ import annotations

import logging
import warnings

from typing import Generic, List, Optional, Type, TypeVar

import boto3

from pydantic import BaseModel

logger = logging.getLogger(__name__)

PydanticModel = TypeVar("PydanticModel", bound=BaseModel)


class SQSQueue(Generic[PydanticModel]):
    """
    This class provides abstract interface to the boto3 SQS client.

    Attributes
    ----------
    _sqs : SQS.ServiceResource
        SQS resource.
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#service-resource
    _queue : SQS.Queue
        boto3 SQS queue instance.
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#queue
    _message_model : Type[pydantic.BaseModel]
        Pydantic model used to de/serialize messages received/sent from/to the queue.

    Methods
    -------
    from_name
    send_message
    receive_message
    delete_message
    send_messages
    receive_messages
    delete_messages

    Examples
    --------

    Enable type hints:

    >>> queue: SQSQueue[Message] = SQSQueue.from_name(name=..., message_model=Message)

    Send, receive, and delete messages

    >>> queue.send_messages(messages)
    >>> handles, messages = queue.receive_messages()
    >>> queue.delete_messages(handles)

    """

    def __init__(
        self,
        url: str,
        message_model: Type[PydanticModel],
        **kwargs,
    ) -> None:
        """
        Initialize the SQS queue.

        Parameters
        ----------
        url : str
            Queue url.
        message_model : pydantic.BaseModel
            Pydantic model used to de/serialize messages received/sent
            from/to the queue.
        **kwargs
            Additional keyword arguments passed to boto3.resource("sqs", **kwargs)
            For example, region_name.

        """
        self._sqs = boto3.resource("sqs", **kwargs)
        self._queue = self._sqs.Queue(url)
        self._message_model = message_model
        logger.debug("Successfully connected to SQS queue %s", self.url)

    @classmethod
    def from_name(
        cls,
        name: str,
        message_model: Type[PydanticModel],
        account_id: Optional[str] = None,
        **kwargs,
    ) -> SQSQueue:
        """
        Initialize queue using its name.

        Parameters
        ----------
        name : str
            Queue name.
        message_model : Type[PydanticModel]
            Pydantic model used to de/serialize messages received/sent
            from/to the queue.
        account_id : str, optional
            AWS account ID of the account that created the queue.
            If not provided, uses account ID from the local AWS credentials.
        **kwargs
            Additional keyword arguments passed to boto3.resource("sqs", **kwargs)
            For example, region_name.

        Returns
        -------
        SQSQueue
            SQSQUeue instance.

        """
        queue_kwargs = {"QueueName": name}
        if account_id is not None:
            queue_kwargs["QueueOwnerAWSAccountId"] = account_id
        sqs = boto3.resource("sqs", **kwargs)
        queue = sqs.get_queue_by_name(**queue_kwargs)
        return cls(url=queue.url, message_model=message_model, **kwargs)

    @property
    def url(self) -> str:
        return self._queue.url

    @property
    def name(self) -> str:
        return self.url.split("/")[-1]

    def __repr__(self) -> str:
        return (
            f"SQSQueue(url='{self.name}', "
            f"message_model={self._message_model.__name__})"
        )

    def send_message(self, message: PydanticModel) -> str:
        """
        Send single message to the queue.

        Parameters
        ----------
        message : pydantic.BaseModel
            Message.

        Returns
        -------
        message_id : str
            Id of the sent message. Randomly generated by SQS.
            Can be used to identify message in SQS but cannot be used to delete it.

        """
        logger.debug("Sending message %s to %s", message, self.name)
        response = self._queue.send_message(MessageBody=message.json())
        message_id: str = response.get("MessageId")
        logger.debug(
            "Successfully sent message %s to %s, SQS Id: %s",
            message,
            self.name,
            message_id,
        )
        return message_id

    def receive_message(
        self, wait_time_seconds: int = 0
    ) -> tuple[Optional[str], Optional[PydanticModel]]:
        """
        Receive a single message from the queue.

        This is a wrapper for .receive_messages method.
        If you want to receive multiple messages, don't use this method.

        Parameters
        ----------
        wait_time_seconds : int, optional
            The duration (in seconds) for which the call waits for a message to arrive
            in the queue before returning. This enables long polling.
            Read this https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.receive_messages
            By default this is 0 seconds.

        """
        handles, messages = self.receive_messages(
            max_messages=1, wait_time_seconds=wait_time_seconds
        )
        if len(messages) == 0:
            return None, None
        assert len(handles) == len(messages) == 1
        return handles[0], messages[0]

    def delete_message(self, handle: str) -> bool:
        """
        Delete a single message from the queue.

        This is a wrapper for .delete_messages method.
        If you want to delete multiple messages, don't use this method.

        Parameters
        ----------
        handle : str
            Message handle.
            See .delete_message method.

        Returns
        -------
        bool
            Deletion result (True for success, False for failure).

        """
        return self.delete_messages(handles=[handle])[0]

    def send_messages(self, messages: List[PydanticModel]) -> List[bool]:
        """
        Send multiple messages to the queue.

        Parameters
        ----------
        messages : List[pydantic.BaseModel]
            List of messages.

        Returns
        -------
        List[bool]
            List of results (True for success, False for failure).

        Raises
        ------
        AssertionError
            Number of results doesn't match number of messages sent.

        """
        logger.debug(
            "Sending %d messages to %s in batches of 10",
            len(messages),
            self.name,
        )

        results: List[bool] = []
        for i in range(0, len(messages), 10):
            batch = messages[i : i + 10]
            logger.debug(
                "Sending batch of %d messages to %s",
                len(batch),
                self.name,
            )
            response = self._queue.send_messages(
                Entries=[
                    {"Id": f"{i+j}", "MessageBody": message.json()}
                    for j, message in enumerate(batch)
                ]
            )

            # Parse response
            batch_results = sorted(
                [
                    *[
                        {"id": int(entry["Id"]), "success": True}
                        for entry in response.get("Successful", [])
                    ],
                    *[
                        {"id": int(entry["Id"]), "success": False}
                        for entry in response.get("Failed", [])
                    ],
                ],
                key=lambda x: x["id"],
            )
            assert len(batch_results) == len(batch), (
                f"this is a bug, AWS returned {len(batch_results):,d} responses, "
                f"{len(batch):,d} messages were sent"
            )
            results.extend([value["success"] for value in batch_results])

        for message, result in zip(messages, results):
            if not result:
                logger.warning(
                    "Failed to send message %s to %s",
                    message,
                    self.name,
                )

        return results

    def receive_messages(
        self,
        max_messages: int = 10_000,
        wait_time_seconds: int = 0,
        max_poll_attempts: int = 0,
    ) -> tuple[List[str], List[PydanticModel]]:
        """
        Receive messages from the queue.

        Messages are fetched from the queue until either max_messages are received
        or the queue is empty.

        Parameters
        ----------
        max_messages : int, optional
            Maximum number of messages to receive.
            By default 10,000.
        wait_time_seconds : int, optional
            The duration (in seconds) for which the call waits for a message to arrive
            in the queue before returning. This enables long polling.
            Read this https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue.receive_messages
            By default this is 0 seconds.
        max_poll_attempts : int, optional
            Maximum number of attempts to fetch messages from the queue if returned
            number of messages is less than 10 (maximum per batch).
            AWS is not guaranteed to return 10 messages even if actual number of
            messages is larger due to data being distributed over multiple servers and
            AWS using random sampling. This parameter allows sampling the queue until
            it's truly depleted.
            !!! CAUTION !!! this may dramatically increase number of SQS calls
            (up to several hundred additional calls), which may impact service cost.

        Returns
        -------
        handles : List[str]
            List of message handles. Used later to remove the messages from the queue.
        messages : List[pydantic.BaseModel]
            List of messages serialized to the provided pydantic model.

        """
        if max_poll_attempts > max_messages:
            warnings.warn(
                " ".join(
                    [
                        f"max_poll_attempts={max_poll_attempts:,d} shouldn't exceed",
                        f"max_messages={max_messages:,d} and was automatically fixed",
                    ]
                ),
                UserWarning,
            )
            max_poll_attempts = max_messages

        max_messages_in_batch = min(10, max_messages)

        poll_attempts: int = 0
        handles: List[str] = []
        messages: List[PydanticModel] = []
        while len(messages) < max_messages:
            # TODO- handle SQS.Client.exceptions.OverLimit
            # i.e., more than 120,000 in-flight messages (don't forget to delete them)
            response = self._queue.receive_messages(
                MaxNumberOfMessages=max_messages_in_batch,
                WaitTimeSeconds=wait_time_seconds,
            )
            logger.debug("Received %d messages from the queue", len(response))
            for message in response:
                handles.append(message.receipt_handle)
                messages.append(self._message_model.parse_raw(message.body))

            if len(response) == 0:
                logger.debug("%s has no messages left", self.name)
                break

            if len(response) < max_messages_in_batch:
                poll_attempts += 1
                if poll_attempts >= max_poll_attempts:
                    logger.debug(
                        (
                            "%s may still have messages, "
                            "but max_poll_attempts were exceeded"
                        ),
                        self.name,
                    )
                    break

        return handles, messages

    def delete_messages(self, handles: List[str]) -> List[bool]:
        """
        Delete messages from the queue using their handles.

        Parameters
        ----------
        handles : List[str]
            Message handles.
            See .receive_messages method.

        Returns
        -------
        List[bool]
            List of deletion results (True for success, False for failure).

        Raises
        ------
        AssertionError
            Number of messages reported to be deleted doesn't match number of messages
            requested to be deleted.

        """
        logger.debug(
            "Deleting %d messages from %s in batches of 10",
            len(handles),
            self.name,
        )

        results: List[bool] = []
        for i in range(0, len(handles), 10):
            batch = handles[i : i + 10]
            logger.debug(
                "Deleting batch of %d messages from %s",
                len(batch),
                self.name,
            )
            response = self._queue.delete_messages(
                Entries=[
                    {"Id": f"{i+j}", "ReceiptHandle": handle}
                    for j, handle in enumerate(batch)
                ]
            )

            # Parse response
            batch_results = sorted(
                [
                    *[
                        {"id": int(entry["Id"]), "success": True}
                        for entry in response.get("Successful", [])
                    ],
                    *[
                        {"id": int(entry["Id"]), "success": False}
                        for entry in response.get("Failed", [])
                    ],
                ],
                key=lambda x: x["id"],
            )
            assert len(batch_results) == len(batch), (
                f"this is a bug, AWS returned {len(batch_results):,d} responses, "
                f"{len(batch):,d} messages were requested to be deleted"
            )
            results.extend([value["success"] for value in batch_results])

        return results
