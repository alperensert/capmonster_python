from typing import Any, Optional

from pydantic import Field, BaseModel

from .task import TaskPayload, UserAgentPayload


class HeyTapMetadata(BaseModel):
    """
    Optional metadata for HeyTap task.

    Attributes:
        apiServer: HeyTap API server domain without "https://"; required if it differs
            from the default "captcha-sec.heytapmobi.com".
    """
    apiServer: Optional[str] = Field(default=None, description='HeyTap API server domain without https://.')


class HeyTapTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving HeyTap captcha challenges.

    Uses CustomTask type with class "heytap". This task does not use a proxy.

    Attributes:
        websiteURL: Address of the main page where the captcha is located.
        websiteKey: The siteKey value found on the page.
        metadata: Optional HeyTap-specific metadata (apiServer).
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="heytap", alias="class", frozen=True)
    websiteURL: str = Field(..., description='Address of the main page where the captcha is located.')
    websiteKey: str = Field(..., description='The siteKey value found on the page.')
    metadata: Optional[HeyTapMetadata] = Field(default=None, description='HeyTap-specific metadata.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        if base.get("metadata") == {}:
            base.pop("metadata")
        return base
