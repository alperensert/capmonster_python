from typing import Optional, Any

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class RecaptchaV2Task(TaskPayload, UserAgentPayload):
    """
    Represents a payload structure for solving reCAPTCHA v2 challenges.

    Attributes:
        type: The constant string value identifying the task type as "RecaptchaV2Task".
        websiteURL: The URL of the webpage containing the reCAPTCHA challenge.
        websiteKey: The site key associated with the reCAPTCHA on the webpage.
        recaptchaDataSValue: A one-time token specific to certain custom
            implementations of reCAPTCHA v2. If applicable, this parameter needs
            to be retrieved for each challenge-solving attempt.
        isInvisible: When set to True, specifies that the challenge
            being solved is an invisible reCAPTCHA.
        proxy: Proxy settings to route the request through a specified
            proxy server.
    """
    type: str = Field(default="RecaptchaV2Task", frozen=True)
    websiteURL: str = Field(..., description='Address of a webpage with captcha.')
    websiteKey: str = Field(..., description='reCAPTCHA website key.')
    recaptchaDataSValue: Optional[str] = Field(default=None,
                                               description='Some custom implementations may contain additional "data-s" '
                                                           'parameter in ReCaptcha2 div, which is in fact a one-time token '
                                                           'and must be grabbed every time you want to solve a reCAPTCHA v2.')
    isInvisible: Optional[bool] = Field(default=None,
                                        description='Set to true if you want to solve invisible reCAPTCHA.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
