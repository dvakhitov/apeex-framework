from apeex.http.response import Response

def test_response_default_headers():
    res = Response("OK")
    assert res.status_code == 200
    assert "Content-Type" in res.headers

def test_response_set_header():
    res = Response("data")
    res.set_header("X-Test", "123")
    assert res.headers["X-Test"] == "123"

def test_response_json_factory():
    res = Response.json({"msg": "hello"})
    assert res.headers["Content-Type"] == "application/json"
    assert res.status_code == 200
    assert '"hello"' in res.content

def test_response_text_factory():
    res = Response.text("plain text", status_code=201)
    assert res.content == "plain text"
    assert res.status_code == 201
    assert res.headers["Content-Type"].startswith("text/plain")
