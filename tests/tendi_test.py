from capmonster_python import TenDITask, TenDIMetadata


def test_to_request_minimal():
    task = TenDITask(websiteURL="https://example.com", websiteKey="189123456")
    result = task.to_request()
    assert result == {"type": "CustomTask", "class": "TenDI", "websiteURL": "https://example.com",
                      "websiteKey": "189123456"}


def test_to_request_with_metadata():
    task = TenDITask(
        websiteURL="https://example.com",
        websiteKey="189123456",
        metadata=TenDIMetadata(captchaUrl="https://global.captcha.example.com/TCaptcha.js", aidEncrypted="enc")
    )
    assert task.to_request()["metadata"] == {"captchaUrl": "https://global.captcha.example.com/TCaptcha.js",
                                             "aidEncrypted": "enc"}


def test_empty_metadata_is_omitted():
    task = TenDITask(websiteURL="https://example.com", websiteKey="1", metadata=TenDIMetadata())
    assert "metadata" not in task.to_request()


def test_explicit_none_proxy_still_works():
    task = TenDITask(websiteURL="https://example.com", websiteKey="1", proxy=None)
    assert "proxyType" not in task.to_request()
