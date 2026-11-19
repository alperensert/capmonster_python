from typing import Optional, Any

from pydantic import Field, BaseModel, model_validator

from .task import TaskPayload, UserAgentPayload, ProxyPayload
from .._deprecation import warn_deprecated, warn_proxy_required


class ImpervaTaskMetadata(BaseModel):
    """
    Represents metadata related to an Imperva task.

    Attributes:
        incapsulaScriptUrl: Name of the Incapsula JS file.
        incapsulaCookies: Your cookies from Incapsula. They can be obtained on the
            page using document.cookie. The old `incapsulaCookie` keyword is still
            accepted but deprecated.
        reese84UrlEndpoint: Optional. The name of the endpoint where the reese84
            fingerprint is sent, found among the network requests and typically
            ending with "?d=site.com".
    """
    incapsulaScriptUrl: str = Field(..., description="Name of the Incapsula JS file.")
    incapsulaCookies: str = Field(...,
                                  description="Your cookies from Incapsula. They can be obtained on the page using document.cookie")
    reese84UrlEndpoint: Optional[str] = Field(default=None, description="The name of the endpoint where the reese84 "
                                                                        "fingerprint is sent can be found among the "
                                                                        "requests and ends with ?d=site.com")

    @model_validator(mode="before")
    @classmethod
    def rename_legacy_cookie(cls, data: Any) -> Any:
        if isinstance(data, dict) and "incapsulaCookie" in data:
            warn_deprecated("ImpervaTaskMetadata(incapsulaCookie=...) is deprecated and will be removed in 6.0; "
                            "use incapsulaCookies=... instead.", stacklevel=4)
            data = dict(data)
            legacy = data.pop("incapsulaCookie")
            data.setdefault("incapsulaCookies", legacy)
        return data

    @property
    def incapsulaCookie(self) -> str:
        """Deprecated alias of `incapsulaCookies`."""
        warn_deprecated("ImpervaTaskMetadata.incapsulaCookie is deprecated; use incapsulaCookies.")
        return self.incapsulaCookies


class ImpervaTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for handling and solving an Imperva-based challenge.

    Proxy is required for this task type by CapMonster Cloud; a UserWarning is
    emitted when it is missing.

    Attributes:
        type (str): The identifier for the type of task. This attribute is
        frozen and defaults to "CustomTask".

        class_ (str): The identifier for the class of the task. This attribute is
        frozen, defaults to "Imperva", and is aliased to "class" for external usage.

        websiteURL (str): The URL of the website targeted for solving the challenge.

        metadata (ImpervaTaskMetadata): Encapsulated metadata specific to the
        Imperva challenge, such as the website key.

        proxy (ProxyPayload): Proxy settings.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="Imperva", alias="class", frozen=True)
    websiteURL: str = Field(..., description="URL of the website to be solved.")
    metadata: ImpervaTaskMetadata = Field(..., description="Website key.")
    proxy: Optional[ProxyPayload] = Field(default=None, description="Proxy settings.")

    def model_post_init(self, __context: Any) -> None:
        if self.proxy is None:
            warn_proxy_required("ImpervaTask", stacklevel=4)

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
