import pytest
from fastapi import FastAPI, Response
from apeex.adapters.http import (
    FastAPIRequestAdapter,
    FastAPIResponseAdapter,
    HttpKernelAdapter
)
from apeex.contracts.http import RequestInterface, ResponseInterface
from unittest.mock import MagicMock, AsyncMock

# -------------------------------
# FastAPIRequestAdapter tests
# -------------------------------
def test_fastapi_request_adapter_reads_fields():
    class DummyRequest:
        method = "GET"
        url = type("URL", (), {"path": "/test"})()
        headers = {"x-test": "123"}
        query_params = {"q": "value"}

    req = DummyRequest()
    adapter = FastAPIRequestAdapter(req)

    assert adapter.method == "GET"
    assert adapter.path == "/test"
    assert adapter.headers == {"x-test": "123"}
    assert adapter.query_params == {"q": "value"}

@pytest.mark.asyncio
async def test_fastapi_request_adapter_get_method():
    class DummyRequest:
        method = "GET"
        url = type("URL", (), {"path": "/test"})()
        headers = {}
        query_params = {"param": "value"}

    req = DummyRequest()
    adapter = FastAPIRequestAdapter(req)

    val = await adapter.get("param")
    assert val == "value"

    default_val = await adapter.get("missing", default="default")
    assert default_val == "default"

# -------------------------------
# FastAPIResponseAdapter tests
# -------------------------------
def test_fastapi_response_adapter_fields():
    resp = Response(content=b"Hello", status_code=201, headers={"X-Test": "yes"})
    adapter = FastAPIResponseAdapter(resp)

    assert adapter.status_code == 201
    assert adapter.body == b"Hello"
    assert adapter.headers["x-test"] == "yes"

def test_fastapi_response_adapter_from_body():
    adapter = FastAPIResponseAdapter.from_body(b"Body", status=202, headers={"A": "B"})
    assert adapter.body == b"Body"
    assert adapter.status_code == 202
    assert adapter.headers["a"] == "B"


# -------------------------------
# HttpKernelAdapter tests
# -------------------------------
@pytest.mark.asyncio
async def test_http_kernel_adapter_handle_returns_response_interface():
    app = FastAPI()
    mock_router = MagicMock()
    kernel = HttpKernelAdapter(app, mock_router)

    class DummyRequest(RequestInterface):
        method = "GET"
        path = "/"
        headers = {}
        query_params = {}
        body = b""
        async def get(self, name, default=None):
            return default

    req = DummyRequest()
    resp = await kernel.handle(req)
    assert isinstance(resp, ResponseInterface)
