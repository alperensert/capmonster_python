from typing import Any, Optional

from pydantic import Field

from .task import TaskPayload


class RecaptchaV3EnterpriseTask(TaskPayload):
    """
    Represents a task for solving Google reCAPTCHA v3 Enterprise.

    Attributes:
        websiteURL: Address of the webpage that contains the reCAPTCHA to be solved.
        websiteKey: The specific site key corresponding to the reCAPTCHA on the target website.
        minScore: Defines the minimum acceptable score required for the captcha
            result, ranging between 0.1 and 0.9.
        pageAction: Specifies the widget action value. Default value: verify.
    """
    type: str = Field(default="RecaptchaV3EnterpriseTask", frozen=True)
    websiteURL: str = Field(..., description='Address of a webpage with Google ReCaptcha Enterprise.')
    websiteKey: str = Field(..., description='reCAPTCHA website key.')
    minScore: Optional[float] = Field(default=None, description='Minimum score of a captcha.', ge=0.1, le=0.9)
    pageAction: Optional[str] = Field(default=None,
                                      description='Widget action value. Website owner defines what user is doing on '
                                                  'the page through this parameter. Default value: verify')
    nocache: Optional[bool] = Field(default=None,
                                    description='Set to true to force fresh token generation (prevents reuse of cached tokens).')

    def to_request(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True)
