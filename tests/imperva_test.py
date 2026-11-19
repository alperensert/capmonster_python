import warnings

import pytest

from capmonster_python import ImpervaTask, ImpervaTaskMetadata, ProxyPayload

PROXY = ProxyPayload(proxyType="http", proxyAddress="1.2.3.4", proxyPort=8080)


def test_to_request():
    task = ImpervaTask(
        websiteURL="https://example.com",
        metadata=ImpervaTaskMetadata(
            incapsulaScriptUrl="_Incapsula_Resource?SWJIYLWA=abc",
            incapsulaCookies="visid_incap_1=x; incap_ses_1=y",
            reese84UrlEndpoint="Built-with-the-For-hopence-Hurleysurfecting-the-"
        ),
        proxy=PROXY
    )
    result = task.to_request()
    assert result["type"] == "CustomTask"
    assert result["class"] == "Imperva"
    assert result["metadata"]["incapsulaCookies"] == "visid_incap_1=x; incap_ses_1=y"
    assert "incapsulaCookie" not in result["metadata"]
    assert result["proxyAddress"] == "1.2.3.4"
    assert "proxy" not in result


def test_legacy_cookie_name_warns_and_is_renamed():
    with pytest.warns(DeprecationWarning, match="incapsulaCookies"):
        metadata = ImpervaTaskMetadata(incapsulaScriptUrl="s", incapsulaCookie="c")
    assert metadata.incapsulaCookies == "c"
    with pytest.warns(DeprecationWarning):
        assert metadata.incapsulaCookie == "c"
    task = ImpervaTask(websiteURL="https://example.com", metadata=metadata, proxy=PROXY)
    assert task.to_request()["metadata"] == {"incapsulaScriptUrl": "s", "incapsulaCookies": "c"}


def test_missing_proxy_warns():
    with pytest.warns(UserWarning, match="proxy"):
        ImpervaTask(websiteURL="https://example.com",
                    metadata=ImpervaTaskMetadata(incapsulaScriptUrl="s", incapsulaCookies="c"))


def test_new_cookie_name_does_not_warn():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        ImpervaTaskMetadata(incapsulaScriptUrl="s", incapsulaCookies="c")
