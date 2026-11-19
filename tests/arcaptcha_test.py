from capmonster_python import ARCaptchaTask


def test_to_request():
    task = ARCaptchaTask(websiteURL="https://example.com", websiteKey="key", isInvisible=True)
    assert task.to_request() == {"type": "ArCaptchaTask", "websiteURL": "https://example.com",
                                 "websiteKey": "key", "isInvisible": True}


def test_minimal():
    assert "isInvisible" not in ARCaptchaTask(websiteURL="https://example.com", websiteKey="key").to_request()
