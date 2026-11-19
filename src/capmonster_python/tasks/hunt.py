from typing import Optional, Any

from pydantic import Field, BaseModel, model_validator

from .task import TaskPayload, ProxyPayload, UserAgentPayload
from .._deprecation import warn_deprecated
from ..exceptions import CapmonsterValidationException


class HuntMetadata(BaseModel):
    """
    Metadata for Hunt task.

    Pass only `apiGetLib` to generate an X-HD value. To solve the captcha, also pass
    either `data` (the `meta.token` returned by the site) or `widgetUrl`, never both.

    Attributes:
        apiGetLib: Full URL of the Hunt `api.js` file.
        data: The `meta.token` value obtained from the site.
        widgetUrl: Full URL of the Hunt captcha widget, including the query string.
    """
    apiGetLib: str = Field(..., description='Full URL of the Hunt api.js file.')
    data: Optional[str] = Field(default=None, description='The meta.token value obtained from the site.')
    widgetUrl: Optional[str] = Field(default=None, description='Full URL of the Hunt captcha widget.')

    @model_validator(mode="after")
    def check_data_or_widget(self) -> "HuntMetadata":
        if self.data is not None and self.widgetUrl is not None:
            raise CapmonsterValidationException("data and widgetUrl must not be used together",
                                                task="HuntTask")
        return self


class HuntTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for solving Hunt captcha challenges.

    Uses CustomTask type with class "HUNT". Proxy is required for this task type.

    Attributes:
        websiteURL: The URL of the webpage containing the captcha.
        metadata: Hunt-specific metadata (apiGetLib, data or widgetUrl).
        proxy: Proxy settings.
        websiteKey: Deprecated. Sends the legacy `HuntTask` request; use `metadata` instead.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="HUNT", alias="class", frozen=True)
    websiteURL: str = Field(..., description='Address of a webpage with captcha.')
    metadata: Optional[HuntMetadata] = Field(default=None, description='Hunt-specific metadata.')
    websiteKey: Optional[str] = Field(default=None, description='Deprecated: legacy Hunt site key.')
    proxy: Optional[ProxyPayload] = Field(default=None, description='Proxy settings.')

    @model_validator(mode="before")
    @classmethod
    def set_legacy_type(cls, data: Any) -> Any:
        if isinstance(data, dict) and data.get("metadata") is None and data.get("websiteKey") is not None:
            data = {**data, "type": "HuntTask"}
        return data

    @model_validator(mode="after")
    def check_mode(self) -> "HuntTask":
        if self.metadata is None:
            if self.websiteKey is None:
                raise CapmonsterValidationException("metadata is required", field="metadata", task="HuntTask")
            warn_deprecated("HuntTask(websiteKey=...) sends the legacy 'HuntTask' request and will be removed "
                            "in 6.0; pass metadata=HuntMetadata(apiGetLib=..., ...) and a proxy instead.",
                            stacklevel=4)
        elif self.proxy is None:
            raise CapmonsterValidationException("proxy is required", field="proxy", task="HuntTask")
        return self

    def to_request(self) -> dict[str, Any]:
        if self.metadata is None:
            base = self.model_dump(exclude_none=True, exclude={"class_", "metadata"})
        else:
            base = self.model_dump(exclude_none=True, by_alias=True, exclude={"websiteKey"})
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
