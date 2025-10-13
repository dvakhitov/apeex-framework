from apeex.http.request import Request

def test_request_query_params_parsing():
    req = Request("GET", "/users", query_string="name=John&age=30&hobby=music&hobby=reading")
    params = req.query_params
    assert params["name"] == "John"
    assert params["age"] == "30"
    assert params["hobby"] == ["music", "reading"]

def test_get_header_case_insensitive():
    req = Request("GET", "/", headers={"content-type": "application/json"})
    assert req.get_header("content-type") == "application/json"
    assert req.get_header("missing", "default") == "default"

def test_from_scope_builds_request():
    scope = {
        "method": "POST",
        "path": "/submit",
        "headers": [(b"content-type", b"application/json")],
        "query_string": b"user=Bob",
    }
    req = Request.from_scope(scope, body={"key": "value"})
    assert req.method == "POST"
    assert req.path == "/submit"
    assert req.get_header("content-type") == "application/json"
    assert req.query_params["user"] == "Bob"
    assert req.body == {"key": "value"}
