from capmonster_python import FunCaptchaTask, ProxyPayload


def test_to_request():
    task = FunCaptchaTask(
        websiteURL="https://www.example.com",
        websitePublicKey="EX72CCFB-26EX-40E5-91E6-85EX70BE98ED",
        funcaptchaApiJSSubdomain="example-api.arkoselabs.com",
        data='{"blob":"test_blob_value"}',
    )
    result = task.to_request()
    assert result["type"] == "FunCaptchaTask"
    assert result["websiteURL"] == "https://www.example.com"
    assert result["websitePublicKey"] == "EX72CCFB-26EX-40E5-91E6-85EX70BE98ED"
    assert result["funcaptchaApiJSSubdomain"] == "example-api.arkoselabs.com"
    assert result["data"] == '{"blob":"test_blob_value"}'


def test_to_request_with_proxy():
    task = FunCaptchaTask(
        websiteURL="https://www.example.com",
        websitePublicKey="EX72CCFB-26EX-40E5-91E6-85EX70BE98ED",
        proxy=ProxyPayload(proxyType="http", proxyAddress="1.2.3.4", proxyPort=8080)
    )
    result = task.to_request()
    assert result["type"] == "FunCaptchaTask"
    assert result["proxyType"] == "http"
    assert result["proxyAddress"] == "1.2.3.4"
    assert result["proxyPort"] == 8080
    assert "proxy" not in result


def test_to_request_minimal():
    task = FunCaptchaTask(
        websiteURL="https://www.example.com",
        websitePublicKey="pk_value"
    )
    result = task.to_request()
    assert result["type"] == "FunCaptchaTask"
    assert "funcaptchaApiJSSubdomain" not in result
    assert "data" not in result
    assert "cookies" not in result
