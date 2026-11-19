from capmonster_python import FriendlyTask, FriendlyMetadata, ProxyPayload


def test_to_request():
    task = FriendlyTask(
        websiteURL="https://example.com",
        websiteKey="FCMST5VUMCBOCGQ9",
        metadata=FriendlyMetadata(apiGetLib="https://cdn.jsdelivr.net/npm/@friendlycaptcha/sdk@0.1.8/site.min.js"),
        proxy=ProxyPayload(proxyType="http", proxyAddress="1.2.3.4", proxyPort=8080)
    )
    result = task.to_request()
    assert result["type"] == "CustomTask"
    assert result["class"] == "friendly"
    assert result["websiteKey"] == "FCMST5VUMCBOCGQ9"
    assert result["metadata"] == {"apiGetLib": "https://cdn.jsdelivr.net/npm/@friendlycaptcha/sdk@0.1.8/site.min.js"}
    assert result["proxyPort"] == 8080
    assert "proxy" not in result
