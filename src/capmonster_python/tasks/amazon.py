from typing import Any, Optional

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class AmazonTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Amazon AWS WAF captcha and challenge.

    Supports multiple solving options:
        - Option 1: websiteURL + websiteKey + captchaScript (simple captcha)
        - Option 2: websiteURL + websiteKey + challengeScript + context + iv (full challenge)
        - Option 3: websiteURL + challengeScript (invisible challenge only)

    Attributes:
        websiteURL: The main page address where the captcha is solved.
        websiteKey: Found in the apiKey field when rendering captcha.
        captchaScript: Link to jsapi.js or captcha.js on the HTML page.
        challengeScript: Link to challenge.js.
        context: Obtained from window.gokuProps.context.
        iv: Obtained from window.gokuProps.iv.
        cookieSolution: If true, returns aws-waf-token cookie instead of voucher/token.
        proxy: Optional proxy settings.
    """
    type: str = Field(default="AmazonTask", frozen=True)
    websiteURL: str = Field(..., description='The main page address where the captcha is solved.')
    websiteKey: Optional[str] = Field(
        default=None,
        description='Can be found in the apiKey field when rendering captcha.')
    captchaScript: Optional[str] = Field(
        default=None,
        description='Link to jsapi.js or captcha.js on the HTML page.')
    challengeScript: Optional[str] = Field(
        default=None,
        description='Link to challenge.js.')
    context: Optional[str] = Field(
        default=None,
        description='Obtained from window.gokuProps.context.')
    iv: Optional[str] = Field(
        default=None,
        description='Obtained from window.gokuProps.iv.')
    cookieSolution: Optional[bool] = Field(
        default=None,
        description='If true, returns aws-waf-token cookie instead of captcha_voucher and existing_token.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
