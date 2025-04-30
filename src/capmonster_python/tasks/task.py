from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, Literal

from pydantic import BaseModel, model_validator, Field


class TaskPayload(BaseModel, ABC):
    type: str = Field(..., description="Task type")

    @abstractmethod
    def to_request(self) -> Dict[str, Any]:
        """
        Converts the instance's model data into a request-compatible dictionary.

        Returns:
            dict[str, Any]: A dictionary representation of the model data, formatted
            for request purposes.
        """
        pass


class ProxyPayload(BaseModel):
    proxyType: Literal["http", "https", "socks4", "socks5"] = Field(
        ..., description="Type of the proxy (http, https, socks4, socks5)"
    )
    proxyAddress: str = Field(
        ..., title="Proxy Address",
        description="IPv4/IPv6 proxy IP address. Hostnames, transparent and local proxies are not allowed."
    )
    proxyPort: int = Field(
        ..., title="Proxy Port",
        description="Port of the proxy."
    )
    proxyLogin: Optional[str] = Field(
        default=None, description="Username for proxy authentication."
    )
    proxyPassword: Optional[str] = Field(
        default=None, description="Password for proxy authentication."
    )

    @model_validator(mode="after")
    def validate_fields(self) -> "ProxyPayload":
        if self.proxyType and (not self.proxyAddress or not self.proxyPort):
            raise ValueError("proxyAddress and proxyPort are required if proxyType is set.")
        return self


class UserAgentPayload(BaseModel, ABC):
    userAgent: Optional[str] = Field(
        default=None,
        description="Browser User-Agent string used to recognize captcha."
    )


class VanillaTaskPayload(TaskPayload, UserAgentPayload):
    type: str = Field(..., description="Task type string, e.g. 'CustomTask'")
    proxy: Optional[ProxyPayload] = Field(default=None, description="Proxy settings (optional)")

    model_config = {
        "extra": "allow"
    }

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
