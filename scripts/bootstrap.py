# scripts/bootstrap.py
import json
from bundles.app_bundle.controllers.product_controller import ProductController
from apeex.http.kernel import Kernel
from apeex.http.request_interface import RequestInterface
from apeex.http.http_kernel_interface import HttpKernelInterface
from apeex.container.simple_container import SimpleContainer
from apeex.http.simple_controller_resolver import SimpleControllerResolver

# ----------------------------
# 1. Initialize the DI container
# ----------------------------
container = SimpleContainer()

# Register services (adapters)
resolver = SimpleControllerResolver()
container.register("controller_resolver", resolver)

# ----------------------------
# 2. Register routes
# ----------------------------
product_controller = ProductController()
resolver.add_route("/products", "GET", product_controller.list)

# ----------------------------
# 3. Initialize the Kernel
# ----------------------------
kernel: HttpKernelInterface = Kernel(container)

# ----------------------------
# 4. Create a request
# ----------------------------
class SimpleRequest(RequestInterface):
    def __init__(self, path: str, method: str):
        self.path = path
        self.method = method.upper()

request = SimpleRequest("/products", "GET")
print("Registered routes:", resolver.routes)
print("Request key:", (request.path, request.method))
# ----------------------------
# 5. Handle the request via the kernel
# ----------------------------
# Kernel internally uses the resolver from the container
response = kernel.handle(request)

# ----------------------------
# 6. Print the result
# ----------------------------
print("Status:", response.status_code)
print("Body:", json.loads(response.body.decode()))
