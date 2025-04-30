from typing import Any, Optional

from pydantic import Field

from .task import TaskPayload


class RecaptchaV3Task(TaskPayload):
    """
    Represents a task for solving Google reCAPTCHA v3 without using a proxy.

    Attributes:
        websiteURL: Address of the webpage that contains the reCAPTCHA to be solved.
        websiteKey: The specific site key corresponding to the reCAPTCHA on the target website.
        minScore: Defines the minimum acceptable score required for the captcha
            result, ranging between 0.1 and 0.9. Setting this helps filter the quality of
            the solution response.
        pageAction: Specifies the widget action value, typically indicating what
            the user action represents on the page. This value is set by the website owner.
    """
    type: str = Field(default="RecaptchaV3TaskProxyless", frozen=True)
    websiteURL: str = Field(..., description='Address of a webpage with captcha.')
    websiteKey: str = Field(..., description='reCAPTCHA website key.')
    minScore: Optional[float] = Field(default=None, description='Minimum score of a captcha.', ge=0.1, le=0.9)
    pageAction: Optional[str] = Field(default=None,
                                      description='Widget action value. Website owner defines what user is doing on '
                                                  'the page through this parameter. Default value: verify')

    def to_request(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
