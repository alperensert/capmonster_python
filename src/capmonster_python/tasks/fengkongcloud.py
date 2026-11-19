from typing import Any, Optional

from pydantic import Field, BaseModel

from .task import TaskPayload, UserAgentPayload


class FengkongCloudMetadata(BaseModel):
    """
    Optional metadata for FengkongCloud task.

    Attributes:
        apiJsUrl: Link to smcp.min.js, e.g. "https://castatic.fengkongcloud.com/pr/vX.X.X/smcp.min.js".
    """
    apiJsUrl: Optional[str] = Field(default=None, description='Link to smcp.min.js.')


class FengkongCloudTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving FengkongCloud captcha challenges.

    Uses CustomTask type with class "fengkongcloud". This task does not use a proxy.

    Attributes:
        websiteURL: Address of the main page where the captcha is located.
        websiteKey: The siteKey value found on the page.
        metadata: Optional FengkongCloud-specific metadata (apiJsUrl).
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="fengkongcloud", alias="class", frozen=True)
    websiteURL: str = Field(..., description='Address of the main page where the captcha is located.')
    websiteKey: str = Field(..., description='The siteKey value found on the page.')
    metadata: Optional[FengkongCloudMetadata] = Field(default=None, description='FengkongCloud-specific metadata.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        if base.get("metadata") == {}:
            base.pop("metadata")
        return base
