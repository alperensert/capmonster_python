from typing import Any

from pydantic import Field

from .task import TaskPayload, UserAgentPayload


class TemuTask(TaskPayload, UserAgentPayload):
    """
    Represents a Temu task for CAPTCHA challenge handling.

    Attributes:
        class_ (str): The class name for the task, aliased as "class" for JSON
            compatibility. This is always set to "Temu" and is immutable.
        websiteURL (str): The full URL of the webpage where the CAPTCHA is loaded.
        cookie (str): Cookies obtained from the webpage where the CAPTCHA is
            loaded. These cookies are typically required for CAPTCHA validation.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="Temu", alias="class", frozen=True)
    websiteURL: str = Field(..., description="The full URL of the page where the CAPTCHA is loaded.")
    cookie: str = Field(..., description="Cookies obtained from the page where the CAPTCHA is loaded.")

    def to_request(self) -> dict[str, Any]:
        base = self.model_dump(exclude_none=True, by_alias=True)
        cookie = base.pop("cookie")

        if "metadata" not in base:
            base["metadata"] = {}

        base["metadata"]["cookie"] = cookie
        return base
