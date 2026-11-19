from typing import Any, Optional

from pydantic import Field

from .task import TaskPayload, UserAgentPayload


class ARCaptchaTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving ARCaptcha challenges. This task does not use a proxy.

    Attributes:
        websiteURL: Address of the main page where the captcha is located.
        websiteKey: The siteKey value found on the page.
        isInvisible: Set to True if the captcha is invisible.
    """
    type: str = Field(default="ArCaptchaTask", frozen=True)
    websiteURL: str = Field(..., description='Address of the main page where the captcha is located.')
    websiteKey: str = Field(..., description='The siteKey value found on the page.')
    isInvisible: Optional[bool] = Field(default=None, description='Set to true if the captcha is invisible.')

    def to_request(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
