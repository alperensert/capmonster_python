from capmonster_python import TSPDTask, TSPDMetadata, ProxyPayload


def test_to_request():
    task = TSPDTask(
        websiteURL="https://example.com",
        metadata=TSPDMetadata(
            tspdCookie="cookie_value",
            htmlPageBase64="PCFET0NUWVBFIGh0bWw+..."
        ),
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        proxy=ProxyPayload(
            proxyType="http",
            proxyAddress="1.2.3.4",
            proxyPort=8080,
            proxyLogin="user",
            proxyPassword="pass"
        )
    )
    result = task.to_request()
    assert result["type"] == "CustomTask"
    assert result["class"] == "tspd"
    assert result["websiteURL"] == "https://example.com"
    assert result["metadata"]["tspdCookie"] == "cookie_value"
    assert result["metadata"]["htmlPageBase64"] == "PCFET0NUWVBFIGh0bWw+..."
    assert result["proxyType"] == "http"
    assert result["proxyAddress"] == "1.2.3.4"
    assert result["proxyPort"] == 8080
    assert "proxy" not in result
