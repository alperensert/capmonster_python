from capmonster_python import HeyTapTask, HeyTapMetadata


def test_to_request():
    task = HeyTapTask(
        websiteURL="https://example.com",
        websiteKey="key",
        userAgent="ua",
        metadata=HeyTapMetadata(apiServer="captcha-sec.heytapmobi.com")
    )
    assert task.to_request() == {
        "type": "CustomTask",
        "class": "heytap",
        "websiteURL": "https://example.com",
        "websiteKey": "key",
        "userAgent": "ua",
        "metadata": {"apiServer": "captcha-sec.heytapmobi.com"}
    }


def test_metadata_optional():
    assert "metadata" not in HeyTapTask(websiteURL="https://example.com", websiteKey="key").to_request()
