# scripts/bootstrap.py
from apeex.container.container import Container
from apeex.kernel.core_kernel import CoreKernel
from apeex.http.http_kernel import HttpKernel
from apeex.adapters.http.router_adapter import RouterAdapter
from apeex.http.controller_resolver import ControllerResolver
from apeex.bundles.demo_bundle.bundle import DemoBundle


def bootstrap() -> tuple[CoreKernel, HttpKernel]:
    print('\nStart bootstrapping Apeex Kernel!!!\n')

    # Создаём контейнер
    container = Container()

    # Регистрируем RouterAdapter и ControllerResolver
    router = RouterAdapter()
    container.set("router", router)
    container.set("controller_resolver", ControllerResolver(container, router))

    # Создаём CoreKernel (главное приложение)
    core_kernel = CoreKernel(container)
    core_kernel.register_bundle(DemoBundle())
    # Регистрацией сервисов из config.services займётся CoreKernel.bootstrap()
    core_kernel.bootstrap()
    core_kernel.boot()

    # Создаём HttpKernel
    http_kernel = HttpKernel(container)

    print('Bootstrap complete\n')
    return core_kernel, http_kernel
