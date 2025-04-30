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
