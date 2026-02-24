from typing import Any, Optional

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class MTCaptchaTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving MTCaptcha challenges.

    Attributes:
        websiteURL: URL of the page where the captcha is solved.
        websiteKey: The MTCaptcha site key (passed as sk in network requests).
        pageAction: The action parameter (passed as act in requests).
            Only needed if it differs from the default "$".
        isInvisible: Set to true if the captcha is invisible.
        proxy: Optional proxy settings.
    """
    type: str = Field(default="MTCaptchaTask", frozen=True)
    websiteURL: str = Field(..., description='URL of the page where the captcha is solved.')
    websiteKey: str = Field(..., description='The MTCaptcha site key (passed as sk in network requests).')
    pageAction: Optional[str] = Field(
        default=None,
        description='The action parameter (passed as act in requests). Only needed if different from default.')
    isInvisible: Optional[bool] = Field(
        default=None,
        description='Set to true if the captcha is invisible.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
