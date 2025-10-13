from typing import Protocol
from .request_interface import RequestInterface
from .response_interface import ResponseInterface

class HttpKernelInterface(Protocol):
    def handle(self, request: RequestInterface) -> ResponseInterface: ...