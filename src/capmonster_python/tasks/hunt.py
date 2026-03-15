from typing import Optional, Any

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class HuntTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Hunt captcha challenges.

    Attributes:
        websiteURL: The URL of the webpage containing the captcha.
        websiteKey: The Hunt captcha site key.
        proxy: Optional proxy settings.
    """
    type: str = Field(default="HuntTask", frozen=True)
    websiteURL: str = Field(..., description='Address of a webpage with captcha.')
    websiteKey: str = Field(..., description='Hunt captcha site key.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
