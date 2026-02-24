from capmonster_python import TurnstileWaitingRoomTask, ProxyPayload


def test_to_request():
    task = TurnstileWaitingRoomTask(
        websiteURL="https://example.com",
        websiteKey="0x4AAAAAAAC3",
        htmlPageBase64="PCFET0NUWVBFIGh0bWw+...",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        proxy=ProxyPayload(proxyType="http", proxyAddress="1.2.3.4", proxyPort=8080)
    )
    result = task.to_request()
    assert result["type"] == "TurnstileTask"
    assert result["cloudflareTaskType"] == "wait_room"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "0x4AAAAAAAC3"
    assert result["htmlPageBase64"] == "PCFET0NUWVBFIGh0bWw+..."
    assert result["proxyType"] == "http"
    assert result["proxyAddress"] == "1.2.3.4"
    assert "proxy" not in result
