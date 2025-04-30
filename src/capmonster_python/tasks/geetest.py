from typing import Optional, Any

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class GeeTestV3Task(TaskPayload, UserAgentPayload):
    """
    Represents a payload for solving GeeTest V3 captcha.

    Attributes:
        websiteURL:
            Address of the page on which the captcha is being solved.
        gt:
            The GeeTest identifier key 'gt' corresponding to the domain.
        challenge:
            A dynamic key that must be fresh on each request. Reusing a non-fresh challenge
            value will result in an ERROR_TOKEN_EXPIRED.
        geetestApiServerSubdomain:
            Optional API subdomain server for Geetest that must be different from
            `api.geetest.com`.
        geetestGetLib:
            Optional path to the captcha script. This must be provided as a JSON string.
        proxy:
            Optional proxy settings to be used while solving the captcha.
    """
    type: str = Field(default="GeeTestTask", frozen=True)
    websiteURL: str = Field(..., description="Address of the page on which the captcha is solved.")
    gt: str = Field(..., description="The GeeTest identifier key gt for the domain.")
    challenge: str = Field(..., description=(
        "A dynamic key. Must be fresh on each request. If the captcha is loaded on the page, "
        "then the challenge value is no longer valid and you will get ERROR_TOKEN_EXPIRED."
    ))
    geetestApiServerSubdomain: Optional[str] = Field(
        default=None, description="Geetest API subdomain server (must differ from api.geetest.com)"
    )
    geetestGetLib: Optional[str] = Field(
        default=None, description="Path to captcha script. Must be passed as JSON string."
    )
    proxy: Optional[ProxyPayload] = Field(default=None, description="Proxy settings.")

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base


class GeeTestV4Task(TaskPayload, UserAgentPayload):
    """
    Represents a GeeTest V4 task payload.

    Attributes:
        type: Indicates the type of the task, defaulted and frozen as "GeeTestTask".
        websiteURL: Address of the page on which the captcha is solved.
        gt: The GeeTest identifier key gt for the domain.
        version: Version of the GeeTest task, defaulted and frozen as 4.
        initParameters: Extra parameters for v4, used with 'riskType' or challenge details.
        geetestApiServerSubdomain: Geetest API subdomain server (must differ from api.geetest.com).
        geetestGetLib: Path to a captcha script. Must be passed as a JSON string.
        proxy: Proxy settings to be used for the task.
    """
    type: str = Field(default="GeeTestTask", frozen=True)
    websiteURL: str = Field(..., description="Address of the page on which the captcha is solved.")
    gt: str = Field(..., description="The GeeTest identifier key gt for the domain.")
    version: int = Field(default=4, frozen=True)
    initParameters: Optional[object] = Field(
        default=None,
        description="Extra parameters for v4, used with 'riskType' or challenge details."
    )
    geetestApiServerSubdomain: Optional[str] = Field(
        default=None, description="Geetest API subdomain server (must differ from api.geetest.com)"
    )
    geetestGetLib: Optional[str] = Field(
        default=None, description="Path to captcha script. Must be passed as JSON string."
    )
    proxy: Optional[ProxyPayload] = Field(default=None, description="Proxy settings.")

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
