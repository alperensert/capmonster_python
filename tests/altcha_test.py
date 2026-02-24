from capmonster_python import AltchaTask, AltchaMetadata


def test_to_request():
    task = AltchaTask(
        websiteURL="https://example.com",
        metadata=AltchaMetadata(
            challenge="challenge_abc",
            iterations="50000",
            salt="random_salt",
            signature="sig_xyz"
        )
    )
    result = task.to_request()
    assert result["type"] == "CustomTask"
    assert result["class"] == "altcha"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == ""
    assert result["metadata"]["challenge"] == "challenge_abc"
    assert result["metadata"]["iterations"] == "50000"
    assert result["metadata"]["salt"] == "random_salt"
    assert result["metadata"]["signature"] == "sig_xyz"
