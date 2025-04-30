from typing import Optional, Any

from pydantic import Field, BaseModel

from .task import TaskPayload, UserAgentPayload


class ImpervaTaskMetadata(BaseModel):
    """
    Represents metadata related to an Imperva task.

    Attributes:
        incapsulaScriptUrl: Name of the Incapsula JS file.
        incapsulaCookie: Your cookies from Incapsula. They can be obtained on the
            page using document.cookie.
        reese84UrlEndpoint: Optional. The name of the endpoint where the reese84
            fingerprint is sent, found among the network requests and typically
            ending with "?d=site.com".
    """
    incapsulaScriptUrl: str = Field(..., description="Name of the Incapsula JS file.")
    incapsulaCookie: str = Field(...,
                                 description="Your cookies from Incapsula. They can be obtained on the page using document.cookie")
    reese84UrlEndpoint: Optional[str] = Field(default=None, description="The name of the endpoint where the reese84 "
                                                                        "fingerprint is sent can be found among the "
                                                                        "requests and ends with ?d=site.com")


class ImpervaTask(TaskPayload, UserAgentPayload):
    """
    Represents a task for handling and solving an Imperva-based challenge.

    Attributes:
        type (str): The identifier for the type of task. This attribute is
        frozen and defaults to "CustomTask".

        class_ (str): The identifier for the class of the task. This attribute is
        frozen, defaults to "Imperva", and is aliased to "class" for external usage.

        websiteURL (str): The URL of the website targeted for solving the challenge.

        metadata (ImpervaTaskMetadata): Encapsulated metadata specific to the
        Imperva challenge, such as the website key.
    """
    type: str = Field(default="CustomTask", frozen=True)
    class_: str = Field(default="Imperva", alias="class", frozen=True)
    websiteURL: str = Field(..., description="URL of the website to be solved.")
    metadata: ImpervaTaskMetadata = Field(..., description="Website key.")

    def to_request(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)
