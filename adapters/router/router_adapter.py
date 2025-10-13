from fastapi import APIRouter
from apeex.http import RouterInterface, RequestInterface
from typing import Any, Iterable, Mapping

class RouterAdapter(RouterInterface):
    def __init__(self):
        self._router = APIRouter()
        self._routes = []

    def add_route(self, path: str, methods: Iterable[str], handler: Any, name: str|None=None) -> None:
        self._router.add_api_route(path, handler, methods=list(methods), name=name)

    def match(self, request: RequestInterface) -> Mapping[str, Any] | None:
        # Для MVP можно вернуть пустой словарь
        return {}
