from typing import Optional, Dict, Any, Literal

from pydantic import Field, model_validator

from .task import TaskPayload, ProxyPayload
from ..exceptions import CapmonsterValidationException


class TurnstileTask(TaskPayload):
    """
    Represents a TurnstileTask used for solving captcha.

    Attributes:
        websiteURL: A required string containing the page address where the captcha
            is solved.
        websiteKey: A required string for the Turnstile key.
        pageAction: An optional string representing the action field that can be
            found in the callback function to load the captcha.
        data: An optional string containing the value of the data field, which can
            be obtained from the cData parameter.
    """
    type: str = Field(default="TurnstileTaskProxyless", frozen=True)
    websiteURL: str = Field(..., description='The page address, where the captcha is solved')
    websiteKey: str = Field(..., description='Turnstile key.')
    pageAction: Optional[str] = Field(default=None, description='The action field that can be found in the callback '
                                                                'function to load the captcha')
    data: Optional[str] = Field(default=None,
                                description='The value of the data field can be taken from the cData parameter.')

    def to_request(self) -> Dict[str, Any]:
        return self.model_dump(exclude_none=True)


class TurnstileCloudFlareTask(TurnstileTask):
    """
    Represents a Turnstile task for Cloudflare challenges.

    Attributes:
        cloudflareTaskType: Specifies the Cloudflare challenge type. Expected
            values are "token" or "cf_clearance".
        userAgent: Browser User-Agent string, must originate from a Windows OS.
        apiJsUrl: Optional captcha script URL, applicable only for "token" type tasks.
        htmlPageBase64: Base64-encoded HTML page content, required for tasks
            with "cf_clearance" type.
        proxy: Optional proxy settings; mandatory for the "cf_clearance" type and
            omitted for the "token" type.

    Raises:
        CapmonsterValidationException: When field requirements specific to the `cloudflareTaskType`
            are not satisfied.
    """
    type: str = Field(default="TurnstileTask")
    cloudflareTaskType: Literal["token", "cf_clearance"] = Field(default="token",
                                                                 description="Type of Cloudflare challenge")
    userAgent: str = Field(..., description="Browser User-Agent string (must be from Windows OS)")
    apiJsUrl: Optional[str] = Field(default=None, description="Captcha script URL (only for token-based tasks)")
    htmlPageBase64: Optional[str] = Field(default=None,
                                          description="Base64-encoded HTML page content, required for cf_clearance type")
    proxy: Optional[ProxyPayload] = Field(
        default=None, description="Proxy settings (required if type is cf_clearance)"
    )

    @model_validator(mode="after")
    def check_fields_match_type(self) -> "TurnstileCloudFlareTask":
        if self.cloudflareTaskType == "token":
            if not self.apiJsUrl:
                raise CapmonsterValidationException("apiJsUrl is required for cloudflareTaskType='token'")
            if self.proxy is not None:
                raise CapmonsterValidationException("proxy must be omitted for cloudflareTaskType='token'")
        elif self.cloudflareTaskType == "cf_clearance":
            if not self.htmlPageBase64:
                raise CapmonsterValidationException("htmlPageBase64 is required for cloudflareTaskType='cf_clearance'")
            if self.proxy is None:
                raise CapmonsterValidationException("proxy is required for cloudflareTaskType='cf_clearance'")
        return self

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
