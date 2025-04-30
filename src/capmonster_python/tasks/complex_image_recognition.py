from typing import List, Literal, Any

from pydantic import Field

from .task import TaskPayload


class ComplexImageRecognitionTask(TaskPayload):
    """
    Represents a complex image recognition task payload.

    Attributes:
        imagesBase64: List of base64 encoded images. This is required and contains
            raw image data in base64 format.
        task: A string indicating one of the predefined types of recognition
            task. This must be one of "oocl_rotate_new", "oocl_rotate_double_new",
            "betpunch_3x3_rotate", "bls", "shein".
    """
    type: str = Field(default="ComplexImageTask", frozen=True)
    class_: str = Field(default="recognition", alias="class", frozen=True)
    imagesBase64: List[str] = Field(..., description="List of base64 encoded images.")
    task: Literal["oocl_rotate_new", "oocl_rotate_double_new", "betpunch_3x3_rotate", "bls", "shein"] = Field(...,
                                                                                                              description="Type of task.")

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        task = base.pop("task")

        if "metadata" not in base:
            base["metadata"] = {}

        base["metadata"]["Task"] = task
        return base
