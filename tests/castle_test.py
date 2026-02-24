from capmonster_python import CastleTask, CastleMetadata


def test_to_request():
    task = CastleTask(
        websiteURL="https://example.com",
        websiteKey="pk_1Tk5Yzr1WFzxrJCh7WzMZzY1rHpaOtdK",
        metadata=CastleMetadata(
            wUrl="https://example.com/cw.js",
            swUrl="https://example.com/csw.js",
            count=5
        )
    )
    result = task.to_request()
    assert result["type"] == "CustomTask"
    assert result["class"] == "Castle"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "pk_1Tk5Yzr1WFzxrJCh7WzMZzY1rHpaOtdK"
    assert result["metadata"]["wUrl"] == "https://example.com/cw.js"
    assert result["metadata"]["swUrl"] == "https://example.com/csw.js"
    assert result["metadata"]["count"] == 5


def test_to_request_minimal():
    task = CastleTask(
        websiteURL="https://example.com",
        websiteKey="pk_key",
        metadata=CastleMetadata(
            wUrl="https://example.com/cw.js",
            swUrl="https://example.com/csw.js"
        )
    )
    result = task.to_request()
    assert "count" not in result["metadata"]
