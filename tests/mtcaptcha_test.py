from capmonster_python import MTCaptchaTask


def test_to_request():
    task = MTCaptchaTask(
        websiteURL="https://example.com",
        websiteKey="sk_abcdef",
        pageAction="custom_action",
        isInvisible=True
    )
    result = task.to_request()
    assert result["type"] == "MTCaptchaTask"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "sk_abcdef"
    assert result["pageAction"] == "custom_action"
    assert result["isInvisible"] is True


def test_to_request_minimal():
    task = MTCaptchaTask(
        websiteURL="https://example.com",
        websiteKey="sk_123"
    )
    result = task.to_request()
    assert result["type"] == "MTCaptchaTask"
    assert "pageAction" not in result
    assert "isInvisible" not in result
