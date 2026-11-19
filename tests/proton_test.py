import pytest
from pydantic import ValidationError

from capmonster_python import ProtonTask, ProtonMetadata, ProxyPayload

PROXY = ProxyPayload(proxyType="http", proxyAddress="8.8.8.8", proxyPort=8080, proxyLogin="l", proxyPassword="p")


def test_to_request():
    task = ProtonTask(
        websiteURL="https://yourwebsite.com/",
        metadata=ProtonMetadata(HumanVerificationToken="token", pageAction="login"),
        proxy=PROXY
    )
    assert task.to_request() == {
        "type": "CustomTask",
        "class": "proton",
        "websiteURL": "https://yourwebsite.com/",
        "metadata": {"HumanVerificationToken": "token", "pageAction": "login"},
        "proxyType": "http",
        "proxyAddress": "8.8.8.8",
        "proxyPort": 8080,
        "proxyLogin": "l",
        "proxyPassword": "p"
    }


def test_proxy_required():
    with pytest.raises(ValidationError):
        ProtonTask(websiteURL="https://x", metadata=ProtonMetadata(HumanVerificationToken="t", pageAction="signup"))


def test_page_action_values():
    with pytest.raises(ValidationError):
        ProtonMetadata(HumanVerificationToken="t", pageAction="register")
