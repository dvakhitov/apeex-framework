# config/services.py
from apeex.container.container import Container
from apeex.bundles.demo_bundle.bundle import DemoBundle
from apeex.bundles.demo_bundle.services.hello_services import HelloService
from apeex.bundles.demo_bundle.controllers.hello_controller import HelloController

container = Container()

# Регистрация сервисов напрямую
container.set("hello_service", HelloService())

# Регистрация контроллера через фабрику и autowiring
container.set_factory("hello_controller", lambda c: HelloController(c.get("hello_service")))



# Регистрация bundle
demo_bundle = DemoBundle()
demo_bundle.build(container)
