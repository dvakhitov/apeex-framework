def test_kernel_initialization():
    from apeex.http import HttpKernel
    from apeex.container.simple_container import SimpleContainer
    from apeex.http.simple_controller_resolver import SimpleControllerResolver

    # Create a minimal container instance
    container = SimpleContainer()

    # Register a minimal controller_resolver service
    container.register("controller_resolver", SimpleControllerResolver())

    # Initialize the Kernel with the container
    kernel = HttpKernel(container=container)

    # Check that the Kernel object is created
    assert kernel is not None

    # Ensure the Kernel's container matches the passed container
    assert kernel.container is container
