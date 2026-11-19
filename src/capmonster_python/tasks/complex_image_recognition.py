from typing import Any, List, Literal, Optional

from pydantic import Field, model_validator

from .task import TaskPayload
from .._deprecation import warn_deprecated
from ..exceptions import CapmonsterValidationException

TASKS_WITH_ARGUMENT = ("bls_3x3", "portugal_text_find_icon")


class ComplexImageRecognitionTask(TaskPayload):
    """
    Represents a complex image recognition task payload.

    Attributes:
        imagesBase64: List of base64 encoded images. This is required and contains
            raw image data in base64 format.
        task: A string indicating one of the predefined types of recognition
            task: "oocl_rotate_new", "oocl_rotate_double_new", "betpunch_3x3_rotate",
            "baidu", "bls_3x3", "shein", "bills_audio", "dli", "MathSum" or
            "portugal_text_find_icon". "bls" is deprecated: it is still sent as "bls", with a warning.
        taskArgument: Extra task input sent as metadata "TaskArgument"; required for
            "bls_3x3" (the number to find) and "portugal_text_find_icon" (the instruction text).
    """
    type: str = Field(default="ComplexImageTask", frozen=True)
    class_: str = Field(default="recognition", alias="class", frozen=True)
    imagesBase64: List[str] = Field(..., description="List of base64 encoded images.")
    task: Literal["oocl_rotate_new", "oocl_rotate_double_new", "betpunch_3x3_rotate", "baidu", "bls_3x3", "bls",
                  "shein", "bills_audio", "dli", "MathSum", "portugal_text_find_icon"] = Field(...,
                                                                                               description="Type of task.")
    taskArgument: Optional[str] = Field(default=None, description="Extra task input, sent as TaskArgument.")

    @model_validator(mode="after")
    def check_task(self) -> "ComplexImageRecognitionTask":
        if self.task == "bls":
            warn_deprecated("ComplexImageRecognitionTask(task='bls') is deprecated and will be removed in 6.0; "
                            "use task='bls_3x3' with taskArgument.", stacklevel=4)
        elif self.task in TASKS_WITH_ARGUMENT and self.taskArgument is None:
            raise CapmonsterValidationException(f"taskArgument is required for task '{self.task}'",
                                                field="taskArgument", task="ComplexImageRecognitionTask")
        return self

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        task = base.pop("task")
        task_argument = base.pop("taskArgument", None)

        if "metadata" not in base:
            base["metadata"] = {}

        base["metadata"]["Task"] = task
        if task_argument is not None:
            base["metadata"]["TaskArgument"] = task_argument
        if task == "bills_audio":
            base["metadata"]["PayloadType"] = "Audio"
        return base
