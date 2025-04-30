from typing import Optional, Any

from pydantic import Field, BaseModel, model_validator

from .task import TaskPayload, UserAgentPayload, ProxyPayload
from ..exceptions import CapmonsterValidationException


class DataDomeMetadata(BaseModel):
    """
    Represents metadata related to DataDome.

    Attributes:
        htmlPageBase64: Optional; Contains additional data about the captcha in
            Base64-encoded format.
        captchaUrl: Optional; URL pointing to the captcha, typically formatted
            like: "https://geo.captcha-delivery.com/captcha/?initialCid=...".
        datadomeCookie: Mandatory; Stores the DataDome cookies, retrievable on
            the page using `document.cookie`.

    Raises:
        CapmonsterValidationException: If neither `htmlPageBase64` nor `captchaUrl` is provided,
            or if both are provided at the same time.
    """
    htmlPageBase64: Optional[str] = Field(default=None,
                                          description="Object that contains additional data about the captcha.")
    captchaUrl: Optional[str] = Field(default=None,
                                      description="\"captchaUrl\" - link to the captcha. Usually it looks like this: \"https://geo.captcha-delivery.com/captcha/?initialCid=...\"")
    datadomeCookie: str = Field(...,
                                description="Your cookies from datadome. You can get it on the page using document.cookie")

    @model_validator(mode="after")
    def validate_fields(self) -> "DataDomeMetadata":
        if self.htmlPageBase64 is None and self.captchaUrl is None:
            raise CapmonsterValidationException("htmlPageBase64 or captchaUrl required.")
        if self.htmlPageBase64 is not None and self.captchaUrl is not None:
            raise CapmonsterValidationException("htmlPageBase64 and captchaUrl are mutually exclusive.")
        return self


class DataDomeTask(TaskPayload, UserAgentPayload):
    """
    Represents a task payload for solving captchas on the DataDome platform.

    Attributes:
        websiteURL: A string that contains the address of the page where the captcha is solved.
        proxy: Optional proxy settings, represented as a ProxyPayload. Defaults to None.
        metadata: Additional metadata about the captcha, represented as a DataDomeMetadata.
            Defaults to None.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="DataDome", alias="class", frozen=True)
    websiteURL: str = Field(..., description="Address of the page on which the captcha is solved.")
    proxy: Optional[ProxyPayload] = Field(default=None, description="Proxy settings.")
    metadata: DataDomeMetadata = Field(default=None, description="Additional data about the captcha.")

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
