from typing import Any, Optional

from pydantic import Field, BaseModel

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class AltchaMetadata(BaseModel):
    """
    Metadata for Altcha task.

    Attributes:
        challenge: Unique task identifier obtained from the website.
        iterations: Number of iterations (corresponds to maxnumber value).
        salt: Salt obtained from the site, used for hash generation.
        signature: Digital signature of the request.
    """
    challenge: str = Field(..., description='Unique task identifier obtained from the website.')
    iterations: str = Field(..., description='Number of iterations (corresponds to maxnumber value).')
    salt: str = Field(..., description='Salt obtained from the site, used for hash generation.')
    signature: str = Field(..., description='Digital signature of the request.')


class AltchaTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Altcha challenges.

    Uses CustomTask type with class "altcha".

    Attributes:
        websiteURL: Main page URL where Altcha is located.
        websiteKey: For this task, sending an empty string is allowed.
        metadata: Altcha-specific metadata (challenge, iterations, salt, signature).
        proxy: Optional proxy settings.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="altcha", alias="class", frozen=True)
    websiteURL: str = Field(..., description='Main page URL where Altcha is located.')
    websiteKey: str = Field(default="", description='For this task, sending an empty string is allowed.')
    metadata: AltchaMetadata = Field(..., description='Altcha-specific metadata.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
