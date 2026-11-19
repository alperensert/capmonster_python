from typing import Any, Literal

from pydantic import Field, BaseModel

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class ProtonMetadata(BaseModel):
    """
    Metadata for Proton Captcha task.

    Attributes:
        HumanVerificationToken: Token from the site's response.
        pageAction: Action on the site: "login" or "signup".
    """
    HumanVerificationToken: str = Field(..., description='Token from the site response.')
    pageAction: Literal["login", "signup"] = Field(..., description='Action on the site: login or signup.')


class ProtonTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Proton Captcha challenges.

    Uses CustomTask type with class "proton". Proxy is required for this task type.

    Attributes:
        websiteURL: Address of the main page where the captcha is located.
        metadata: Proton-specific metadata (HumanVerificationToken, pageAction).
        proxy: Proxy settings.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="proton", alias="class", frozen=True)
    websiteURL: str = Field(..., description='Address of the main page where the captcha is located.')
    metadata: ProtonMetadata = Field(..., description='Proton-specific metadata.')
    proxy: ProxyPayload = Field(..., description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        base.update(base.pop("proxy"))
        return base
