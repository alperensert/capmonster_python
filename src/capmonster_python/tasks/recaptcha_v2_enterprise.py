from typing import Optional, Any

from pydantic import Field

from .task import TaskPayload, ProxyPayload, UserAgentPayload


class RecaptchaV2EnterpriseTask(TaskPayload, UserAgentPayload):
    """
    Represents a task payload for solving Google reCAPTCHA V2 Enterprise challenges.

    Attributes:
        websiteURL: The address of a webpage with Google reCAPTCHA Enterprise.
        websiteKey: The reCAPTCHA website key.
        enterprisePayload: An optional parameter containing additional values passed
            to the 'grecaptcha.enterprise.render' method along with the sitekey.
        apiDomain: An optional domain address from which to load reCAPTCHA Enterprise.
            This parameter should only be set if explicitly needed.
        cookies: Optional cookies to be sent with the request.
        proxy: Optional proxy settings for handling the task.
    """
    type: str = Field(default="RecaptchaV2EnterpriseTask", frozen=True)
    websiteURL: str = Field(..., description='Address of a webpage with Google reCAPTCHA Enterprise.')
    websiteKey: str = Field(..., description='reCAPTCHA website key.')
    enterprisePayload: Optional[str] = Field(default=None,
                                             description='Some implementations of the reCAPTCHA Enterprise widget '
                                                         'may contain additional parameters that are passed to the '
                                                         '“grecaptcha.enterprise.render” method along with the sitekey.')
    apiDomain: Optional[str] = Field(default=None,
                                     description='Domain address from which to load reCAPTCHA Enterprise. '
                                                 'Don\'t use a parameter if you don\'t know why it\'s needed.')
    cookies: Optional[str] = Field(default=None, description='Cookies to be sent with the request.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
