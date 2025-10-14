# bundles/app_bundle/bundle.py
from apeex.contracts.bundle import BundleInterface
from apeex.container import SimpleContainer

class AppBundle(BundleInterface):
    """Example application bundle."""

    def build(self, container: SimpleContainer):
        # Register services or controllers here
        pass

    def boot(self):
        # Code to execute when the bundle is booted
        pass

    def shutdown(self):
        # Cleanup when shutting down
        pass
