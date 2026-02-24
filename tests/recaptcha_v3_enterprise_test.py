from capmonster_python import RecaptchaV3EnterpriseTask


def test_to_request():
    task = RecaptchaV3EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="6Le0xVgUAAAAAIt20XEB4rVhYOODgTl00d4TuRTE",
        minScore=0.7,
        pageAction="login_test"
    )
    result = task.to_request()
    assert result["type"] == "RecaptchaV3EnterpriseTask"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "6Le0xVgUAAAAAIt20XEB4rVhYOODgTl00d4TuRTE"
    assert result["minScore"] == 0.7
    assert result["pageAction"] == "login_test"


def test_to_request_minimal():
    task = RecaptchaV3EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="sitekey123"
    )
    result = task.to_request()
    assert result["type"] == "RecaptchaV3EnterpriseTask"
    assert "minScore" not in result
    assert "pageAction" not in result
