from capmonster_python import FengkongCloudTask, FengkongCloudMetadata


def test_to_request():
    task = FengkongCloudTask(
        websiteURL="https://example.com",
        websiteKey="site_key",
        metadata=FengkongCloudMetadata(apiJsUrl="https://castatic.fengkongcloud.com/pr/v1.0.4/smcp.min.js")
    )
    assert task.to_request() == {
        "type": "CustomTask",
        "class": "fengkongcloud",
        "websiteURL": "https://example.com",
        "websiteKey": "site_key",
        "metadata": {"apiJsUrl": "https://castatic.fengkongcloud.com/pr/v1.0.4/smcp.min.js"}
    }


def test_metadata_optional():
    task = FengkongCloudTask(websiteURL="https://example.com", websiteKey="k", metadata=FengkongCloudMetadata())
    assert "metadata" not in task.to_request()
