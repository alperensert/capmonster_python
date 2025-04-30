from typing import Optional, Any

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class GeeTestV3Task(TaskPayload, UserAgentPayload):
    """
    Represents a payload for solving GeeTest V3 captcha.

    Attributes
    ----------
    websiteURL : str
        Address of the page on which the captcha is being solved.
    gt : str
        The GeeTest identifier key 'gt' corresponding to the domain.
    challenge : str
        A dynamic key that must be fresh on each request. Reusing a non-fresh challenge
        value will result in an ERROR_TOKEN_EXPIRED.
    geetestApiServerSubdomain : Optional[str]
        Optional API subdomain server for Geetest that must be different from
        `api.geetest.com`.
    geetestGetLib : Optional[str]
        Optional path to the captcha script. This must be provided as a JSON string.
    proxy : Optional[ProxyPayload]
        Optional proxy settings to be used while solving the captcha.

    Methods
    -------
    to_request()
        Constructs a dictionary representation of the payload, including proxy settings
        if provided.
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
    Handles the creation of a GeeTest v4 task payload for solving the GeeTest CAPTCHA.

    Attributes:
        type: Specifies the type of the task. The value is fixed as "GeeTestTask".
        websiteURL: Specifies the URL of the webpage where CAPTCHA is being solved.
        gt: The GeeTest identifier key for the domain.
        version: The version of the payload, which is fixed to 4.
        initParameters: Optional. Additional parameters used for risk type identification or challenge details.
        geetestApiServerSubdomain: Optional. Subdomain for the Geetest API server, differing from "api.geetest.com".
        geetestGetLib: Optional. Path to the CAPTCHA script provided as a JSON string.
        proxy: Optional. Proxy configuration used for solving CAPTCHA.

    Methods:
        to_request:
            Prepares a dictionary representation of the task payload, including proxy configuration if provided.
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
