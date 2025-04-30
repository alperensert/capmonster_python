from typing import Any

from pydantic import Field

from .task import TaskPayload, UserAgentPayload


class BasiliskTask(TaskPayload, UserAgentPayload):
    """
    BasiliskTask represents a specific task payload used for solving captcha on a given website.

    Attributes:
        websiteURL (str): The address of the main page where the captcha is solved.
        websiteKey (str): Can be found in the html code in the attribute data-sitekey of the captcha container or in
            the payload of a POST request to the https://basiliskcaptcha.com/challenge/check-site in the field site_key.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="Basilisk", alias="class", frozen=True)
    websiteURL: str = Field(..., description="The address of the main page where the captcha is solved.")
    websiteKey: str = Field(...,
                            description="Can be found in the html code in the attribute data-sitekey of the captcha container.")

    def to_request(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)
