from apeex.http.exceptions import HttpException, NotFound, MethodNotAllowed


def test_http_exception_default_values():
    exc = HttpException()
    assert exc.status_code == 500
    assert "Internal" in str(exc)


def test_http_exception_custom_message():
    exc = HttpException("Oops!", 418)
    assert str(exc) == "Oops!"
    assert exc.status_code == 418


def test_not_found_exception_defaults():
    exc = NotFound()
    assert exc.status_code == 404
    assert "Not Found" in str(exc)


def test_method_not_allowed_defaults():
    exc = MethodNotAllowed()
    assert exc.status_code == 405
    assert "Method Not Allowed" in str(exc)
