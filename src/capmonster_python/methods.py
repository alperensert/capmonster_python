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


class ReportIncorrectCaptchaPayload(BaseModel):
    clientKey: str = Field(..., description="Client key")
    taskId: int = Field(..., description="ID of the task to report as incorrect.")


class CreateTaskPayload(BaseModel):
    clientKey: str = Field(..., description="Client key")
    task: TaskPayload = Field(..., description="Task data")
    callbackUrl: Optional[str] = Field(default=None,
                                       description="Web address for sending the captcha task result. Data is sent by POST request.")

    @field_serializer("task")
    def serialize_task(self, task: TaskPayload, _info) -> dict:
        return task.to_request()


class TaskResult(BaseModel):
    """
    Represents the full result of a task returned by getTaskResult.

    Attributes:
        status (str): "processing" while the task is being solved, "ready" when it is done.
        solution (dict): The solution of the task; empty while the task is processing.
        cost (Optional[float]): Cost of the task in USD; only returned when the task is ready.
    """
    status: str = Field(default="processing", description="Task status: processing or ready.")
    solution: dict = Field(default_factory=dict, description="Task solution.")
    cost: Optional[float] = Field(default=None, description="Cost of the task in USD.")

    @classmethod
    def from_response(cls, response: dict) -> "TaskResult":
        return cls(status=response.get("status") or "processing",
                   solution=response.get("solution") or {},
                   cost=response.get("cost"))
