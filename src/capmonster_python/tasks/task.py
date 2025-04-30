from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, Literal

from pydantic import BaseModel, Field


class TaskPayload(BaseModel, ABC):
    """
    Represents a base payload structure for a specific task type.

    This class serves as an abstract base model for defining the structure
    and behavior of task payloads. The `type` attribute specifies the type
    of task, and subclasses are required to implement the `to_request` method,
    which converts the instance into a format compatible with API requests.

    Attributes:
        type (str): The task type identifier sent to the Capmonster API, generally constant.
    """
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
    """
    Represents proxy information and validation for usage.

    This class defines the structure and validation logic for a proxy configuration.
    It includes fields for the proxy type, address, port, and optional authentication
    credentials. It ensures that mandatory fields such as proxyAddress and proxyPort
    are provided if proxyType is specified.

    Attributes:
        proxyType (Literal["http", "https", "socks4", "socks5"]): The type of proxy.
        proxyAddress (str): The IP address or hostname of the proxy server.
        proxyPort (int): The port number of the proxy server.
        proxyLogin (Optional[str]): The username for proxy authentication, if required.
        proxyPassword (Optional[str]): The password for proxy authentication, if required.

    Example:
            ```python
            client = CapmonsterClient("YOUR_API_KEY")
            task_id = client.create_task(
                RecaptchaV2Task(
                    websiteURL="https://www.google.com/recaptcha/api2/demo",
                    websiteKey="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
                    proxy=ProxyPayload(
                        proxyType="https",
                        proxyAddress="192.168.1.1",
                        proxyPort=8080,
                        proxyLogin="<USERNAME>",
                        proxyPassword="<PASSWORD>")
                    )
                )
            ```
    """
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


class UserAgentPayload(BaseModel, ABC):
    """
    Represents a payload containing a browser User-Agent string.

    This class is designed as a data model for handling the browser User-Agent
    string, typically used to recognize and handle captcha services effectively.
    It extends from BaseModel to provide data validation and supports optional
    specification of the User-Agent string.

    Attributes:
        userAgent: Field containing the browser User-Agent string. When
            provided, it helps to identify specific browser instances for captcha
            recognition.
    """
    userAgent: Optional[str] = Field(
        default=None,
        description="Browser User-Agent string used to recognize captcha."
    )


class VanillaTaskPayload(TaskPayload, UserAgentPayload):
    """
    Base class for forward-compatible CAPTCHA task payloads.

    This class is designed to support rapid user adaptation to new or evolving Capmonster task formats.
    It enables developers to define payloads for newly introduced task types, or to extend existing tasks
    with additional fields without waiting for an official library update.

    Intended for:
        - Users who need to work with task types not yet implemented in the SDK.
        - Scenarios where Capmonster API introduces new fields to existing tasks.

    Attributes:
        type (str): The task type identifier sent to the Capmonster API. Must be overridden in subclasses.

    Notes:
        - Can be subclassed to define completely custom tasks.
        - Provides a stable structure while allowing dynamic extension.

    Example:
        Use this as a base to quickly integrate a new task format:

        ```python
        class CustomCaptchaTask(VanillaTaskPayload):
            type: str = "NewCustomTask"
            custom_field: str
        ```
    """

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
