# tests/test_http_kernel.py

def test_kernel_initialization():
    from apeex.http import Kernel
    from apeex.container.simple_container import SimpleContainer
    from apeex.http.simple_controller_resolver import SimpleControllerResolver

    # Create a minimal container instance
    container = SimpleContainer()

    # Register a minimal controller_resolver service
    container.register("controller_resolver", SimpleControllerResolver())

    # Initialize the Kernel with the container
    kernel = Kernel(container=container)

    # Check that the Kernel object is created
    assert kernel is not None

    # Ensure the Kernel's container matches the passed container
    assert kernel.container is container
