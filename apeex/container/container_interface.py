from abc import ABC, abstractmethod
from typing import Any, Protocol, Type, runtime_checkable

class ContainerException(Exception):
    pass

class NotFoundException(ContainerException):
    pass

@runtime_checkable
class ContainerInterface(Protocol):
    """
    Interface for a Dependency Injection container.
    """

    def set(self, name: str, service: Any) -> None:
        """Register a service instance or factory by name."""

    def get(self, name: str) -> Any:
        """Retrieve a service by name; raise exception if not found."""

    def has(self, name: str) -> bool:
        """Check if a service is registered."""

    def autowire(self, cls: Type) -> Any:
        """Create an instance of cls, automatically resolving dependencies."""
