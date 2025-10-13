from typing import Optional, Mapping

from apeex.container import SimpleContainer
from apeex.http.request_interface import RequestInterface
from apeex.http.response_interface import ResponseInterface
from apeex.http.controller_resolver_interface import ControllerResolverInterface
from apeex.http.http_kernel_interface import HttpKernelInterface
import json


class SimpleResponse(ResponseInterface):
    def __init__(self, body: bytes, status_code: int = 200, headers: Optional[Mapping[str,str]] = None):
        self.body = body
        self.status_code = status_code
        self.headers = headers or {}

    @classmethod
    def from_body(cls, body, status: int = 200, headers: Optional[Mapping[str,str]] = None) -> "SimpleResponse":
        # Convert body to bytes if needed
        if isinstance(body, (dict, list)):
            body_bytes = json.dumps(body).encode("utf-8")
        elif isinstance(body, str):
            body_bytes = body.encode("utf-8")
        elif isinstance(body, bytes):
            body_bytes = body
        else:
            body_bytes = str(body).encode("utf-8")
        return cls(body_bytes, status, headers)

class Kernel(HttpKernelInterface):
    """Minimal HTTP kernel implementing HttpKernelInterface."""

    def __init__(self, container: SimpleContainer):
        self.container = container
        self.resolver: ControllerResolverInterface = container.get("controller_resolver")

    def handle(self, request: RequestInterface) -> ResponseInterface:
        controller_callable = self.resolver.resolve(request.path, request.method)
        if controller_callable is None:
            return SimpleResponse(json.dumps({"error": "Not Found"}).encode("utf-8"), status_code=404)

        result = controller_callable(request)

        # Ensure ResponseInterface
        if not isinstance(result, ResponseInterface):
            result = SimpleResponse(result)

        return result
