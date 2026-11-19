import pytest

from capmonster_python import HuntTask, HuntMetadata, ProxyPayload, CapmonsterValidationException

PROXY = ProxyPayload(proxyType="http", proxyAddress="1.2.3.4", proxyPort=8080)


def test_to_request_with_data():
    task = HuntTask(
        websiteURL="https://example.com",
        metadata=HuntMetadata(apiGetLib="https://example.com/hd-api/api.js", data="meta_token"),
        proxy=PROXY
    )
    result = task.to_request()
    assert result["type"] == "CustomTask"
    assert result["class"] == "HUNT"
    assert result["websiteURL"] == "https://example.com"
    assert result["metadata"] == {"apiGetLib": "https://example.com/hd-api/api.js", "data": "meta_token"}
    assert result["proxyType"] == "http"
    assert "proxy" not in result
    assert "websiteKey" not in result


def test_to_request_with_widget_url():
    task = HuntTask(
        websiteURL="https://example.com",
        metadata=HuntMetadata(apiGetLib="https://example.com/api.js", widgetUrl="https://captcha.example.com/w?h=1"),
        proxy=PROXY
    )
    assert task.to_request()["metadata"]["widgetUrl"] == "https://captcha.example.com/w?h=1"


def test_x_hd_generation_only_api_get_lib():
    task = HuntTask(websiteURL="https://example.com", metadata=HuntMetadata(apiGetLib="a"), proxy=PROXY)
    assert task.to_request()["metadata"] == {"apiGetLib": "a"}


def test_data_and_widget_url_together():
    with pytest.raises(CapmonsterValidationException):
        HuntMetadata(apiGetLib="a", data="d", widgetUrl="w")


def test_proxy_required():
    with pytest.raises(CapmonsterValidationException):
        HuntTask(websiteURL="https://example.com", metadata=HuntMetadata(apiGetLib="a"))


def test_metadata_or_website_key_required():
    with pytest.raises(CapmonsterValidationException):
        HuntTask(websiteURL="https://example.com", proxy=PROXY)


def test_legacy_website_key_warns_and_keeps_request():
    with pytest.warns(DeprecationWarning, match="HuntTask"):
        task = HuntTask(websiteURL="https://example.com", websiteKey="key123")
    assert task.to_request() == {"type": "HuntTask", "websiteURL": "https://example.com", "websiteKey": "key123"}
