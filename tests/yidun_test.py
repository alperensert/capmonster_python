from capmonster_python import YidunTask


def test_to_request():
    task = YidunTask(
        websiteURL="https://example.com",
        websiteKey="site_key_123"
    )
    result = task.to_request()
    assert result["type"] == "YidunTask"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "site_key_123"


def test_to_request_enterprise():
    task = YidunTask(
        websiteURL="https://example.com",
        websiteKey="site_key_123",
        yidunGetLib="https://example.com/load.min.js",
        yidunApiServerSubdomain="custom-api",
        challenge="challenge_id",
        hcg="hash_value",
        hct=1234567890
    )
    result = task.to_request()
    assert result["type"] == "YidunTask"
    assert result["yidunGetLib"] == "https://example.com/load.min.js"
    assert result["yidunApiServerSubdomain"] == "custom-api"
    assert result["challenge"] == "challenge_id"
    assert result["hcg"] == "hash_value"
    assert result["hct"] == 1234567890
