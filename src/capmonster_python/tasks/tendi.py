from typing import Optional, Any

from pydantic import Field, BaseModel

from .task import TaskPayload, UserAgentPayload, ProxyPayload


class TenDIMetadata(BaseModel):
    """
    Optional metadata for TenDI task.

    Attributes:
        captchaUrl: Link to the captcha script, if the site loads it from a custom domain.
        aidEncrypted: The single-use encrypted Aid value issued by the site, if it uses one.
    """
    captchaUrl: Optional[str] = Field(default=None, description="Link to the captcha script.")
    aidEncrypted: Optional[str] = Field(default=None, description="Single-use encrypted Aid value from the site.")


class TenDITask(TaskPayload, UserAgentPayload):
    """
    Represents a task configuration for solving a captcha using the TenDI service.

    Attributes:
        class_: Represents the class name of the task. Default is "TenDI".
        websiteURL: Address of the page on which the captcha is solved.
        websiteKey: A unique identifier (captchaAppId) specific to the site.
        metadata: Optional. TenDI-specific metadata (captchaUrl, aidEncrypted).
        proxy: Optional. Proxy settings for the task, if applicable.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="TenDI", alias="class", frozen=True)
    websiteURL: str = Field(..., description="Address of the page on which the captcha is solved.")
    websiteKey: str = Field(..., description="captchaAppId. For example websiteKey: 189123456 - is a "
                                             "unique parameter for your site.")
    metadata: Optional[TenDIMetadata] = Field(default=None, description="TenDI-specific metadata.")
    proxy: Optional[ProxyPayload] = Field(default=None, description="Proxy settings.")

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        if base.get("metadata") == {}:
            base.pop("metadata")
        return base
