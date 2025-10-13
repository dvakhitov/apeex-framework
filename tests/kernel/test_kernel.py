from apeex.kernel.kernel import Kernel
from apeex.container.container import Container
from apeex.bundles.demo_bundle.bundle import DemoBundle

def test_kernel_lifecycle():
    container = Container()
    kernel = Kernel(container)
    bundle = DemoBundle()
    kernel.register_bundle(bundle)

    kernel.bootstrap()
    kernel.boot()
    # Test service access
    hello_service = container.get("HelloService")
    assert hello_service.say_hello("Alice") == "Hello, Alice!"
    kernel.shutdown()
