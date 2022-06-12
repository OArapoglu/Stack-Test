import pytest
from stack_operation import StackOperation


@pytest.fixture
def stack_operation() -> StackOperation:
    """Create a new stack object."""
    stack_operation = StackOperation()
    assert isinstance(stack_operation, StackOperation)
    return stack_operation
