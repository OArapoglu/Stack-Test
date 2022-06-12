"""
    Exceptions for stack objects.
"""


class NullElementException(Exception):
    """Raise NullElementException if a value is None."""


class EmptyStackException(Exception):
    """Raise EmptyStackException if stack is empty."""
