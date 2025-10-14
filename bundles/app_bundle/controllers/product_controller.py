import json
from typing import Mapping
from apeex.contracts.http.request_interface import RequestInterface
from apeex.contracts.http.response_interface import ResponseInterface

class ProductController:
    """Example controller for products."""

    def list(self, request: RequestInterface) -> ResponseInterface:
        # Simple inline Response
        class SimpleResponse(ResponseInterface):
            def __init__(
                    self,
                    body: bytes | str | dict | list,
                    status_code: int = 200,
                    headers: Mapping[str, str] | None = None,
            ):
                if isinstance(body, (dict, list)):
                    body = json.dumps(body).encode("utf-8")
                elif isinstance(body, str):
                    body = body.encode("utf-8")

                self.body = body
                self.status_code = status_code
                self.headers = headers or {"Content-Type": "application/json"}

            @classmethod
            def from_body(
                    cls,
                    body: bytes | str | dict | list,
                    status: int = 200,
                    headers: Mapping[str, str] | None = None,
            ) -> "SimpleResponse":
                return cls(body, status_code=status, headers=headers)

        # Return example product list
        return SimpleResponse(body={"id": 1, "name": "Product 1"})

    def create(self, request: RequestInterface) -> ResponseInterface:
        class SimpleResponse(ResponseInterface):
            def __init__(self, body, status_code=201):
                self.body = body
                self.status_code = status_code

        # In real app, create product in database
        return SimpleResponse(body={"id": 2, "name": "New Product"})
