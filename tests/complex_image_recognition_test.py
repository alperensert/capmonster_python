from capmonster_python import ComplexImageRecognitionTask


def test_to_request():
    task = ComplexImageRecognitionTask(
        imagesBase64=["first", "second", "third"],
        task="oocl_rotate_double_new"
    )
    result = task.to_request()
    assert result["type"] == "ComplexImageTask"
    assert result["class"] == "recognition"
    assert result["metadata"]["Task"] == "oocl_rotate_double_new"


def test_task_argument_is_sent():
    task = ComplexImageRecognitionTask(imagesBase64=["img"], task="bls_3x3", taskArgument="123")
    assert task.to_request()["metadata"] == {"Task": "bls_3x3", "TaskArgument": "123"}


def test_task_argument_required():
    import pytest
    from capmonster_python import CapmonsterValidationException
    with pytest.raises(CapmonsterValidationException):
        ComplexImageRecognitionTask(imagesBase64=["img"], task="portugal_text_find_icon")


def test_bills_audio_sets_payload_type():
    task = ComplexImageRecognitionTask(imagesBase64=["audio"], task="bills_audio")
    assert task.to_request()["metadata"] == {"Task": "bills_audio", "PayloadType": "Audio"}


def test_new_task_names():
    for name in ("baidu", "dli", "MathSum"):
        task = ComplexImageRecognitionTask(imagesBase64=["img"], task=name)
        assert task.to_request()["metadata"]["Task"] == name


def test_legacy_bls_warns_and_is_renamed():
    import pytest
    with pytest.warns(DeprecationWarning, match="bls_3x3"):
        task = ComplexImageRecognitionTask(imagesBase64=["img"], task="bls")
    assert task.to_request()["metadata"]["Task"] == "bls_3x3"
