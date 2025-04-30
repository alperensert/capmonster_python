from typing import Optional, Any

from pydantic import Field

from .task import TaskPayload, UserAgentPayload, ProxyPayload


class BinanceTask(TaskPayload, UserAgentPayload):
    """
    Represents a Binance task to solve captcha challenges with specific payload. Use only to log in with your account.

    This class encapsulates the payload required for a Binance captcha-solving task, including necessary user
    agent and security details. It inherits common task and user agent payloads, allowing for integration
    with systems handling such authentication processes. This class also supports optional proxy configuration.

    Attributes:
        websiteURL: The address of the main page where the captcha is solved.
        websiteKey: A unique parameter for your website's section.
        validateId: A dynamic key representing the value of the parameter validateId, securityId, or
                    securityCheckResponseValidateId.
        proxy: Optional proxy settings used for handling requests during captcha solving.
    """
    type: str = Field(default="BinanceTask", frozen=True)
    websiteURL: str = Field(..., description="The address of the main page where the captcha is solved.")
    websiteKey: str = Field(..., description="A unique parameter for your website's section.")
    validateId: str = Field(..., description="A dynamic key. The value of the parameter validateId, securityId, "
                                             "or securityCheckResponseValidateId.")
    proxy: Optional[ProxyPayload] = Field(default=None, description="Proxy settings.")

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
