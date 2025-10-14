from apeex.kernel.core_kernel import CoreKernel
from apeex.container.container import Container
from apeex.bundles.demo_bundle import DemoBundle
from apeex.bundles.demo_bundle import HelloService


def test_kernel_lifecycle():
    container = Container()
    kernel = CoreKernel(container)
    bundle = DemoBundle()
    kernel.register_bundle(bundle)

    kernel.bootstrap()
    kernel.boot()

    # Test service access
    hello_service = container.get("HelloService")
    assert hello_service.say_hello("Alice") == "Hello, Alice!"
    kernel.shutdown()
