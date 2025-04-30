from typing import List, Literal, Optional, Any

from pydantic import Field, BaseModel, model_validator

from .task import TaskPayload
from ..exceptions import CapmonsterValidationException


class ComplexImageRecaptchaMetadata(BaseModel):
    """
    Represents metadata for a complex image-based CAPTCHA task.

    Attributes:
        task: Optional. Represents the textual description of the CAPTCHA task
            (e.g., "Click on traffic lights"). Only one of `task` or `taskDefinition`
            must be set.
        taskDefinition: Optional. Represents the technical value defining the CAPTCHA
            task type. Only one of `task` or `taskDefinition` must be set.
        grid: Required. Specifies the grid size of the CAPTCHA. It must be one of
            the possible values: "4x4", "3x3", or "1x1".
    """
    task: Optional[str] = Field(default=None, alias="Task",
                                description="Possible values: \"Click on traffic lights\" and others.")
    taskDefinition: Optional[str] = Field(default=None, alias="TaskDefinition",
                                          description="Technical value that defines the task type.")
    grid: Literal["4x4", "3x3", "1x1"] = Field(..., alias="Grid",
                                               description="Grid size of the captcha part.")

    @model_validator(mode="after")
    def check_fields_match_type(self) -> "ComplexImageRecaptchaMetadata":
        if self.task is None and self.taskDefinition is None:
            raise ValueError("task or taskDefinition must be set")
        if self.task is not None and self.taskDefinition is not None:
            raise ValueError("only one of task or taskDefinition must be set")
        return self


class ComplexImageRecaptchaTask(TaskPayload):
    """
    Represents a task payload for solving complex image-based recaptcha challenges.

    Attributes:
        imageUrls: Optional list of image URLs associated with the captcha. These may
            correspond to a single image captcha of formats 4x4, 3x3, or other new
            configurations.
        imagesBase64: Optional list of base64-encoded images. Similar to imageUrls,
            these represent segments of the captcha in various formats such as 4x4,
            3x3, or others.
        metadata: Metadata describing additional details required for solving the recaptcha
            challenge. This attribute must be provided.

    Raises:
        CapmonsterValidationException: If neither `imageUrls` nor `imagesBase64` is provided,
            or if both are provided at the same time.
    """
    type: str = Field(default="ComplexImageTask", frozen=True)
    class_: str = Field(default="recaptcha", alias="class", frozen=True)
    imageUrls: Optional[List[str]] = Field(default=None,
                                           description="Single image 4x4, 3x3 or a new 1x1 captcha part (in an array).")
    imagesBase64: Optional[List[str]] = Field(default=None,
                                              description="Single image 4x4, 3x3 or a new 1x1 captcha part in base64 format (in an array).")
    metadata: ComplexImageRecaptchaMetadata = Field(..., description="Metadata for the task.")

    @model_validator(mode="after")
    def check_fields_match_type(self) -> "ComplexImageRecaptchaTask":
        if self.imageUrls is None and self.imagesBase64 is None:
            raise CapmonsterValidationException("imageUrls or imagesBase64 must be set")
        if self.imageUrls is not None and self.imagesBase64 is not None:
            raise CapmonsterValidationException("only one of imageUrls or imagesBase64 must be set")
        return self

    def to_request(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)
