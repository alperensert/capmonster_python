from typing import Any

from pydantic import Field, BaseModel

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class TSPDMetadata(BaseModel):
    """
    Metadata for TSPD task.

    Attributes:
        tspdCookie: Cookies obtained on the TSPD challenge page.
        htmlPageBase64: Entire TSPD page encoded in base64.
    """
    tspdCookie: str = Field(..., description='Cookies obtained on the TSPD challenge page.')
    htmlPageBase64: str = Field(..., description='Entire TSPD page encoded in base64.')


class TSPDTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving TSPD challenges.

    Uses CustomTask type with class "tspd". Proxy is required for this task type.

    Attributes:
        websiteURL: URL of the page where the TSPD challenge is located.
        metadata: TSPD-specific metadata (tspdCookie, htmlPageBase64).
        userAgent: Browser User-Agent string (required, must be from Windows OS).
        proxy: Proxy settings (required).
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="tspd", alias="class", frozen=True)
    websiteURL: str = Field(..., description='URL of the page where the TSPD challenge is located.')
    metadata: TSPDMetadata = Field(..., description='TSPD-specific metadata.')
    userAgent: str = Field(..., description='Browser User-Agent string (required, must be from Windows OS).')
    proxy: ProxyPayload = Field(..., description='Proxy settings (required).')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
