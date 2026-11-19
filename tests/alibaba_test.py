import pytest

from capmonster_python import AlibabaTask, AlibabaMetadata, CapmonsterValidationException


def test_to_request():
    task = AlibabaTask(
        websiteURL="https://www.example.com",
        userAgent="ua",
        metadata=AlibabaMetadata(sceneId="1ww7426c", prefix="dlw3kug", region="sgp")
    )
    assert task.to_request() == {
        "type": "CustomTask",
        "class": "alibaba",
        "websiteURL": "https://www.example.com",
        "userAgent": "ua",
        "metadata": {"sceneId": "1ww7426c", "prefix": "dlw3kug", "region": "sgp"}
    }


def test_punish_url_replaces_scene_id_and_prefix():
    task = AlibabaTask(
        websiteURL="https://www.example.com",
        metadata=AlibabaMetadata(punishUrl="https://example.com/_____tmd_____/punish?x5secdata=abc",
                                 cookieRequired=True)
    )
    assert task.to_request()["metadata"] == {"punishUrl": "https://example.com/_____tmd_____/punish?x5secdata=abc",
                                             "cookieRequired": True}


def test_scene_id_and_prefix_required():
    with pytest.raises(CapmonsterValidationException):
        AlibabaMetadata(sceneId="only")
