from apeex.bundles.bundle import Bundle
from apeex.container.container_interface import ContainerInterface
from apeex.bundles.demo_bundle.services.hello_services import HelloService
from apeex.bundles.demo_bundle.controllers.hello_controller import HelloController

class DemoBundle(Bundle):
    """Example bundle demonstrating services and controllers."""

    def build(self, container: ContainerInterface) -> None:
        container.set("HelloService", HelloService())
        container.set_factory("HelloController", lambda c: HelloController(c.get("HelloService")))

    def boot(self, kernel):
        print("DemoBundle booting...")

    def shutdown(self):
        print("DemoBundle shutting down...")
