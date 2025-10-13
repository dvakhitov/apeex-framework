from typing import List
from apeex.container.container_interface import ContainerInterface
from apeex.bundles.bundle import Bundle

class Kernel:
    """
    Core application Kernel.
    Manages container, bundles, and application lifecycle.
    """
    def __init__(self, container: ContainerInterface):
        self.container = container
        self.bundles: List[Bundle] = []

    def register_bundle(self, bundle: Bundle):
        self.bundles.append(bundle)

    def bootstrap(self):
        """Initialize configuration and container"""
        for bundle in self.bundles:
            bundle.build(self.container)

    def boot(self):
        """Boot all bundles"""
        for bundle in self.bundles:
            bundle.boot(self)

    def shutdown(self):
        """Shutdown all bundles"""
        for bundle in self.bundles:
            bundle.shutdown()
