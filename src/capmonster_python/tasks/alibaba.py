from typing import Any, Optional

from pydantic import Field, BaseModel, model_validator

from .task import TaskPayload, ProxyPayload, UserAgentPayload
from ..exceptions import CapmonsterValidationException


class AlibabaMetadata(BaseModel):
    """
    Metadata for Alibaba task.

    `sceneId` and `prefix` are required unless `punishUrl` is given. Pass the other
    fields only if the website uses them.

    Attributes:
        sceneId: The captcha scenario identifier.
        prefix: Captcha initialization parameter (the subdomain of the captcha-open URL).
        userId: Unique identifier of the user or session on the website side.
        userUserId: Additional (secondary) user identifier.
        verifyType: Version or type of the verification mechanism, e.g. "1.0".
        region: Region that processes the captcha, e.g. "cn" or "sgp".
        UserCertifyId: Verification ID of the current captcha session.
        apiGetLib: Link to the captcha JS library used by the website.
        punishUrl: Full URL of the /punish verification page, including its query string.
        cookieRequired: Return cookies with the solution (for Alibaba WAF).
    """
    sceneId: Optional[str] = Field(default=None, description="The captcha scenario identifier.")
    prefix: Optional[str] = Field(default=None, description="Captcha initialization parameter.")
    userId: Optional[str] = Field(default=None, description="User or session identifier.")
    userUserId: Optional[str] = Field(default=None, description="Secondary user identifier.")
    verifyType: Optional[str] = Field(default=None, description="Verification mechanism version.")
    region: Optional[str] = Field(default=None, description="Region that processes the captcha.")
    UserCertifyId: Optional[str] = Field(default=None, description="Verification ID of the captcha session.")
    apiGetLib: Optional[str] = Field(default=None, description="Link to the captcha JS library.")
    punishUrl: Optional[str] = Field(default=None, description="Full URL of the /punish verification page.")
    cookieRequired: Optional[bool] = Field(default=None, description="Return cookies with the solution.")

    @model_validator(mode="after")
    def check_required(self) -> "AlibabaMetadata":
        if self.punishUrl is None and (self.sceneId is None or self.prefix is None):
            raise CapmonsterValidationException("sceneId and prefix are required unless punishUrl is set",
                                                task="AlibabaTask")
        return self


class AlibabaTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Alibaba captcha challenges.

    Uses CustomTask type with class "alibaba".

    Attributes:
        websiteURL: Full URL of the page with the captcha.
        metadata: Alibaba-specific metadata.
        proxy: Optional proxy settings.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="alibaba", alias="class", frozen=True)
    websiteURL: str = Field(..., description='Full URL of the page with the captcha.')
    metadata: AlibabaMetadata = Field(..., description='Alibaba-specific metadata.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
