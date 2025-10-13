from fastapi import FastAPI, Request, Response
from apeex.http import HttpKernelInterface, RequestInterface, ResponseInterface
from apeex.http import RouterInterface
from typing import Any

class FastAPIRequestAdapter(RequestInterface):
    def __init__(self, request: Request):
        self._request = request
        self.method = request.method
        self.path = request.url.path
        self.headers = dict(request.headers)
        self.query_params = dict(request.query_params)
        self.body = b""

    async def get(self, name: str, default: Any=None) -> Any:
        return self.query_params.get(name, default)

class FastAPIResponseAdapter(ResponseInterface):
    def __init__(self, response: Response):
        self.status_code = response.status_code
        self.headers = dict(response.headers)
        self.body = response.body

    @classmethod
    def from_body(cls, body: bytes, status: int=200, headers=None):
        from fastapi.responses import Response
        return cls(Response(content=body, status_code=status, headers=headers))

class HttpKernelAdapter(HttpKernelInterface):
    def __init__(self, app: FastAPI, router: RouterInterface):
        self._app = app
        self._router = router

    async def handle(self, request: RequestInterface) -> ResponseInterface:
        # Здесь можно использовать router.match() и вызвать контроллер
        # Для MVP просто проброс FastAPI Request
        return FastAPIResponseAdapter(Response(content=b"OK", status_code=200))
