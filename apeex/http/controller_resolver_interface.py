from typing import Protocol, Callable, Optional
from apeex.http import RequestInterface
from apeex.http import ResponseInterface

# ----------------------------
# Интерфейс ControllerResolver
# ----------------------------
class ControllerResolverInterface(Protocol):
    """
    Интерфейс для реализации маршрута в контроллере.
    """
    def get_controller(self, path: str, method: str) -> Optional[Callable[[RequestInterface], ResponseInterface]]:
        ...

    def resolve(self, path: str, method: str) -> Optional[Callable]:
        ...