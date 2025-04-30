from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from .tasks.task import TaskPayload


class GetBalancePayload(BaseModel):
    """
    Represents a payload for retrieving the balance.

    Attributes:
        clientKey (str): The key representing the client, used for identifying
            the client in balance-related operations.
    """
    clientKey: str = Field(..., description="Client key")


class GetTaskResultPayload(BaseModel):
    clientKey: str = Field(..., description="Client key")
    taskId: int = Field(..., description="ID which was obtained from create task method.")


class CreateTaskPayload(BaseModel):
    clientKey: str = Field(..., description="Client key")
    task: TaskPayload = Field(..., description="Task data")
    callbackUrl: Optional[str] = Field(default=None,
                                       description="Web address for sending the captcha task result. Data is sent by POST request.")

    @field_serializer("task")
    def serialize_task(self, task: TaskPayload, _info) -> dict:
        return task.to_request()
