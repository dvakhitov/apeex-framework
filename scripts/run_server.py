from fastapi import FastAPI, Request, Response
import uvicorn
from apeex.http.kernel import Kernel
from apeex.container.simple_container import SimpleContainer
from apeex.http.simple_controller_resolver import SimpleControllerResolver
from bundles.app_bundle.controllers.product_controller import ProductController
from apeex.http.response_interface import ResponseInterface

app = FastAPI()

# --- Setup framework manually (like in bootstrap) ---
container = SimpleContainer()
resolver = SimpleControllerResolver()
container.register("controller_resolver", resolver)

# Register routes
resolver.add_route("/products", "GET", ProductController().list)

kernel = Kernel(container)


# --- FastAPI adapter ---
@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def handle_request(request: Request, path: str):
    # Convert FastAPI request to our internal RequestInterface
    class SimpleRequest:
        def __init__(self, path, method, body=None):
            self.path = "/" + path
            self.method = method
            self.body = body

    req = SimpleRequest(path, request.method)

    # Let the kernel handle it
    response: ResponseInterface = kernel.handle(req)

    # Convert our ResponseInterface to FastAPI Response
    return Response(
        content=response.body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.headers.get("Content-Type", "application/json"),
    )


if __name__ == "__main__":
    uvicorn.run("scripts.run_server:app", host="0.0.0.0", port=8000, reload=True)
