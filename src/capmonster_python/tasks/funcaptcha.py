from typing import Any, Optional

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class FunCaptchaTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving FunCaptcha (Arkose Labs) challenges.

    Attributes:
        websiteURL: The URL of the page where the captcha is located.
        websitePublicKey: FunCaptcha public key (pk).
        funcaptchaApiJSSubdomain: Arkose Labs API subdomain, only if it differs
            from the default client-api.arkoselabs.com.
        data: Additional data parameter, required if the site uses data[blob].
        cookies: Additional cookies in the format cookieName1=value1; cookieName2=value2.
        proxy: Optional proxy settings.
    """
    type: str = Field(default="FunCaptchaTask", frozen=True)
    websiteURL: str = Field(..., description='The URL of the page where the captcha is located.')
    websitePublicKey: str = Field(..., description='FunCaptcha public key (pk).')
    funcaptchaApiJSSubdomain: Optional[str] = Field(
        default=None,
        description='Arkose Labs subdomain (surl). Specify only if it differs from client-api.arkoselabs.com.')
    data: Optional[str] = Field(
        default=None,
        description='Additional data parameter, required if the site uses data[blob].')
    cookies: Optional[str] = Field(
        default=None,
        description='Additional cookies in the format: cookieName1=value1; cookieName2=value2.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
