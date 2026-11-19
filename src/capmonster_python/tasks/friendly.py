from typing import Any, Optional

from pydantic import Field, BaseModel

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class FriendlyMetadata(BaseModel):
    """
    Metadata for Friendly Captcha task.

    Attributes:
        apiGetLib: URL of the widget JS file: for V1 the friendly-challenge widget.module.min.js,
            for V2 the site.min.js loaded on the page.
    """
    apiGetLib: str = Field(..., description='URL of the Friendly Captcha widget JS file.')


class FriendlyTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Friendly Captcha challenges.

    Uses CustomTask type with class "friendly".

    Attributes:
        websiteURL: Full URL of the page with the captcha.
        websiteKey: Friendly Captcha site key.
        metadata: Friendly-specific metadata (apiGetLib).
        proxy: Optional proxy settings.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="friendly", alias="class", frozen=True)
    websiteURL: str = Field(..., description='Full URL of the page with the captcha.')
    websiteKey: str = Field(..., description='Friendly Captcha site key.')
    metadata: FriendlyMetadata = Field(..., description='Friendly-specific metadata.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
