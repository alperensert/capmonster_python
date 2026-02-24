from typing import Any, Optional

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class YidunTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Yidun (NECaptcha) challenges.

    Attributes:
        websiteURL: Full URL of the page with the captcha.
        websiteKey: The siteKey value found on the page.
        yidunGetLib: Path to the JS file responsible for loading the captcha (full URL).
            Recommended for Enterprise versions with challenge/hcg/hct fields.
        yidunApiServerSubdomain: Subdomain of the Yidun API server.
            Required for custom/Enterprise servers.
        challenge: Unique identifier of the current captcha (Enterprise).
        hcg: Captcha hash used in the request (Enterprise).
        hct: Numeric timestamp used in Enterprise version validation.
        proxy: Optional proxy settings.
    """
    type: str = Field(default="YidunTask", frozen=True)
    websiteURL: str = Field(..., description='Full URL of the page with the captcha.')
    websiteKey: str = Field(..., description='The siteKey value found on the page.')
    yidunGetLib: Optional[str] = Field(
        default=None,
        description='Path to the JS file responsible for loading the captcha (full URL).')
    yidunApiServerSubdomain: Optional[str] = Field(
        default=None,
        description='Subdomain of the Yidun API server for custom/Enterprise servers.')
    challenge: Optional[str] = Field(
        default=None,
        description='Unique identifier of the current captcha (Enterprise).')
    hcg: Optional[str] = Field(
        default=None,
        description='Captcha hash used in the request (Enterprise).')
    hct: Optional[int] = Field(
        default=None,
        description='Numeric timestamp used in Enterprise version validation.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
