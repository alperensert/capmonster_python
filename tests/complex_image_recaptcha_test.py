import pytest

from capmonster_python import ComplexImageRecaptchaTask, ComplexImageRecaptchaMetadata


def test_to_request():
    task = ComplexImageRecaptchaTask(
        imageUrls=["url1", "url2"],
        metadata=ComplexImageRecaptchaMetadata(Task="Click on traffic lights", Grid="4x4")
    )
    result = task.to_request()
    assert result["type"] == "ComplexImageTask"
    assert result["class"] == "recaptcha"
    assert result["type"] == "ComplexImageTask"


def test_to_request_raises_value_error_if_url_and_base64_are_provided_together():
    with pytest.raises(ValueError):
        task = ComplexImageRecaptchaTask(
            imageUrls=["url1", "url2"],
            imagesBase64=["base64_1", "base64_2"],
            metadata=ComplexImageRecaptchaMetadata(Task="Click on traffic lights", Grid="4x4")
        )
        task.to_request()


def test_to_request_raises_value_error_if_url_or_base64_are_not_provided():
    with pytest.raises(ValueError):
        task = ComplexImageRecaptchaTask(
            metadata=ComplexImageRecaptchaMetadata(Task="Click on traffic lights", Grid="4x4")
        )
        task.to_request()
