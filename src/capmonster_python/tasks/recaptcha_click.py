from typing import Optional, Any

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class RecaptchaClickTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving click-based reCAPTCHA challenges.

    Attributes:
        websiteURL: The URL of the webpage containing the reCAPTCHA challenge.
        websiteKey: The site key associated with the reCAPTCHA on the webpage.
        isInvisible: When set to True, specifies that the challenge
            being solved is an invisible reCAPTCHA.
        proxy: Optional proxy settings.
    """
    type: str = Field(default="RecaptchaClickTask", frozen=True)
    websiteURL: str = Field(..., description='Address of a webpage with captcha.')
    websiteKey: str = Field(..., description='reCAPTCHA website key.')
    isInvisible: Optional[bool] = Field(default=None,
                                        description='Set to true if you want to solve invisible reCAPTCHA.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
