from abc import ABC, abstractmethod
from typing import Any


class Stack(ABC):
    """This is an abstract class for stack objects."""

    @abstractmethod
    def push(self, data: Any):
        """Push a node into the stack."""

    @abstractmethod
    def pop(self) -> Any:
        """Pop a node from the stack."""

    @abstractmethod
    def peek(self) -> Any:
        """Peek a node from the stack."""

    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the stack."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Test if the stack is empty."""
