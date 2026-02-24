from typing import Any, Optional

from pydantic import Field, BaseModel

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class CastleMetadata(BaseModel):
    """
    Metadata for Castle task.

    Attributes:
        wUrl: Link to cw.js file.
        swUrl: Link to csw.js file.
        count: Number of tokens to generate (default 1, max 49).
    """
    wUrl: str = Field(..., description='Link to cw.js file.')
    swUrl: str = Field(..., description='Link to csw.js file.')
    count: Optional[int] = Field(default=None, description='Number of tokens (default 1, max 49).', ge=1, le=49)


class CastleTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Castle challenges.

    Uses CustomTask type with class "Castle".

    Attributes:
        websiteURL: URL of the page where Castle is located.
        websiteKey: Publishable Key.
        metadata: Castle-specific metadata (wUrl, swUrl, count).
        proxy: Optional proxy settings.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="Castle", alias="class", frozen=True)
    websiteURL: str = Field(..., description='URL of the page where Castle is located.')
    websiteKey: str = Field(..., description='Castle publishable key.')
    metadata: CastleMetadata = Field(..., description='Castle-specific metadata.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
