from typing import Optional, Any

from pydantic import Field

from capmonster_python.tasks.task import TaskPayload, ProxyPayload


class ProsopoTask(TaskPayload):
    """
    Represents a Prosopo CAPTCHA solving task.

    Attributes:
        websiteURL: The full URL of the CAPTCHA page that needs to be solved.
        websiteKey: The site key parameter value obtained from the CAPTCHA page.
        proxy: Optional proxy settings to be used in sending the task request.

    Methods:
        to_request:
            Converts the data of the task, including proxy settings if provided,
            into a dictionary format suitable for creating task requests.
    """
    type: str = Field(default="ProsopoTask", frozen=True)
    websiteURL: str = Field(..., description="The full URL of the CAPTCHA page.")
    websiteKey: str = Field(..., description="The value of the siteKey parameter found on the page.")
    proxy: Optional[ProxyPayload] = Field(default=None, description="Proxy settings.")

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True)
        proxy_dict = base.pop("proxy", {})
        if proxy_dict:
            base.update(proxy_dict)
        return base
