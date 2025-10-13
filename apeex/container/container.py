import inspect
from typing import Any, Callable, Type, Dict
from apeex.container.container_interface import ContainerInterface

class Container(ContainerInterface):
    """
    Simple MVP Dependency Injection container supporting:
    - service/factory registration
    - autowiring via type hints
    - singleton scope
    """

    def __init__(self):
        self._services: Dict[str, Any] = {}
        self._factories: Dict[str, Callable[['Container'], Any]] = {}
        self._singletons: Dict[str, Any] = {}

    def set(self, name: str, service: Any) -> None:
        """Register a service instance directly."""
        self._services[name] = service

    def set_factory(self, name: str, factory: Callable[['Container'], Any]) -> None:
        """Register a factory function for lazy service creation."""
        self._factories[name] = factory

    def get(self, name: str) -> Any:
        """Retrieve a service by name; instantiate via factory if needed."""
        if name in self._singletons:
            return self._singletons[name]

        if name in self._services:
            return self._services[name]

        if name in self._factories:
            service = self._factories[name](self)
            self._singletons[name] = service  # singleton
            return service

        raise KeyError(f"Service '{name}' not found in container")

    def has(self, name: str) -> bool:
        return name in self._services or name in self._factories or name in self._singletons

    def autowire(self, cls: Type) -> Any:
        """Create instance automatically, resolving constructor dependencies."""
        # Return singleton if exists
        if cls.__name__ in self._singletons:
            return self._singletons[cls.__name__]

        signature = inspect.signature(cls.__init__)
        kwargs = {}
        for param in signature.parameters.values():
            if param.name == "self":
                continue
            if param.annotation != inspect.Parameter.empty:
                dep_name = param.annotation.__name__
                if self.has(dep_name):
                    kwargs[param.name] = self.get(dep_name)
                else:
                    kwargs[param.name] = self.autowire(param.annotation)

        instance = cls(**kwargs)
        self._singletons[cls.__name__] = instance  # save singleton
        return instance

    def build_bundle(self, bundle) -> None:
        """Call bundle.build(container) hook to register bundle services."""
        bundle.build(self)
