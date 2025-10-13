from abc import ABC, abstractmethod
from typing import Any

class ContainerException(Exception):
    pass

class NotFoundException(ContainerException):
    pass

class ContainerInterface(ABC):

    @abstractmethod
    def get(self, service_id: str) -> Any:
        """Returns service by ID or raises NotFoundException."""
        ...

    @abstractmethod
    def has(self, service_id: str) -> bool:
        """Returns True if service exists, False otherwise."""
        ...
