from capmonster_python import AmazonTask, ProxyPayload


def test_to_request_option1():
    task = AmazonTask(
        websiteURL="https://example.com",
        websiteKey="api_key_123",
        captchaScript="https://example.com/jsapi.js",
    )
    result = task.to_request()
    assert result["type"] == "AmazonTask"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "api_key_123"
    assert result["captchaScript"] == "https://example.com/jsapi.js"


def test_to_request_option2():
    task = AmazonTask(
        websiteURL="https://example.com",
        websiteKey="api_key_123",
        challengeScript="https://example.com/challenge.js",
        captchaScript="https://example.com/captcha.js",
        context="ctx_value",
        iv="iv_value",
    )
    result = task.to_request()
    assert result["type"] == "AmazonTask"
    assert result["challengeScript"] == "https://example.com/challenge.js"
    assert result["context"] == "ctx_value"
    assert result["iv"] == "iv_value"


def test_to_request_with_cookie_solution():
    task = AmazonTask(
        websiteURL="https://example.com",
        websiteKey="key",
        captchaScript="https://example.com/jsapi.js",
        cookieSolution=True,
    )
    result = task.to_request()
    assert result["cookieSolution"] is True


def test_to_request_with_proxy():
    task = AmazonTask(
        websiteURL="https://example.com",
        websiteKey="key",
        captchaScript="https://example.com/jsapi.js",
        proxy=ProxyPayload(proxyType="socks5", proxyAddress="10.0.0.1", proxyPort=1080)
    )
    result = task.to_request()
    assert result["proxyType"] == "socks5"
    assert result["proxyAddress"] == "10.0.0.1"
    assert "proxy" not in result
