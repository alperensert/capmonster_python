from typing import Optional, Literal, Any

from pydantic import Field

from .task import TaskPayload


class ImageToTextTask(TaskPayload):
    """
    Represents a task for solving image-based captcha using certain recognition parameters.

    Attributes:
        body (str): File body encoded in base64. Ensure it is passed without any line breaks.
        capMonsterModule (Optional[str]): The name of the recognition module (e.g., "yandex").
        recognizingThreshold (Optional[int]): The threshold for captcha recognition confidence
            with a range of 0 to 100. Ensures that you are charged only if recognition confidence
            meets or exceeds this value.
        case (Optional[bool]): Indicates whether the captcha is case-sensitive.
        numeric (Optional[Literal[0, 1]]): Set to 1 if the captcha consists only of numbers.
        math (Optional[bool]): Set to true if the captcha involves solving a mathematical operation.
    """
    type: str = Field(default="ImageToTextTask", frozen=True)
    body: str = Field(..., description="File body encoded in base64*. Make sure to pass it without line breaks.")
    capMonsterModule: Optional[str] = Field(default=None,
                                            description="The name of recognizing module, for example, “yandex“.")
    recognizingThreshold: Optional[int] = Field(default=None,
                                                description="Captcha recognition threshold with a possible value from "
                                                            "0 to 100. For example, if recognizingThreshold was set to "
                                                            "90 and the task was solved with a confidence of 80, "
                                                            "you won't be charged.",
                                                ge=0, le=100)
    case: Optional[bool] = Field(default=None, description="Set to true if captcha is case sensitive.")
    numeric: Optional[Literal[0, 1]] = Field(default=None, description="Set to 1 if captcha contains numbers only.")
    math: Optional[bool] = Field(default=None, description="Set to true if captcha requires a mathematical operation.")

    def to_request(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
