from capmonster_python import TurnstileCloudFlareTask, ProxyPayload

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


def test_token_with_page_data():
    task = TurnstileCloudFlareTask(
        websiteURL="https://example.com",
        websiteKey="0x4AAAAAAA",
        userAgent=UA,
        pageAction="managed",
        data="cdata",
        pageData="chl_page_data",
        apiJsUrl="https://challenges.cloudflare.com/turnstile/v0/g/api.js"
    )
    result = task.to_request()
    assert result["type"] == "TurnstileTask"
    assert result["cloudflareTaskType"] == "token"
    assert result["pageData"] == "chl_page_data"


def test_token_without_api_js_url_and_with_proxy():
    task = TurnstileCloudFlareTask(
        websiteURL="https://example.com",
        websiteKey="0x4AAAAAAA",
        userAgent=UA,
        proxy=ProxyPayload(proxyType="http", proxyAddress="1.2.3.4", proxyPort=8080)
    )
    result = task.to_request()
    assert "apiJsUrl" not in result
    assert result["proxyAddress"] == "1.2.3.4"
