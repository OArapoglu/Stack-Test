import random
import pytest
from stack_operation import StackOperation
from exception import EmptyStackException, NullElementException

START_ID = 1
FINISH_ID = 100
STRING_DATA = ["Python", "Java", "C"]


def test_stack_init(stack_operation: StackOperation):
    """Test initial size of a stack."""
    assert stack_operation.get_size() == 0


def test_push1_size(stack_operation: StackOperation):
    """Test the size of the stack after pushing 1 node."""
    node_id1 = random.randint(START_ID, FINISH_ID)
    stack_operation.push(node_id1)
    assert stack_operation.get_size() == 1


def test_push1_peek1(stack_operation: StackOperation):
    """Test 1 peek of the stack after pushing 1 node."""
    node_data1 = STRING_DATA[0]
    stack_operation.push(node_data1)
    assert stack_operation.peek() == node_data1


def test_push1_pop1(stack_operation: StackOperation):
    """Test 1 pop of the stack after pushing 1 node."""
    node_data1 = STRING_DATA[1]
    stack_operation.push(node_data1)
    assert stack_operation.pop() == node_data1


def test_push2_peek2(stack_operation: StackOperation):
    """Test 2 peek of the stack after pushing 2 nodes."""
    node_data1 = random.randint(START_ID, FINISH_ID)
    node_data2 = random.randint(START_ID, FINISH_ID)
    stack_operation.push(node_data1)
    stack_operation.push(node_data2)
    assert stack_operation.peek() == node_data2
    assert stack_operation.peek() == node_data2


def test_push2_pop2(stack_operation: StackOperation):
    """Test 2 pop of the stack after pushing 2 nodes."""
    node_data1 = random.randint(START_ID, FINISH_ID)
    node_data2 = random.randint(START_ID, FINISH_ID)
    stack_operation.push(node_data1)
    stack_operation.push(node_data2)
    assert stack_operation.pop() == node_data2
    assert stack_operation.pop() == node_data1


def test_push3_pop1_peek1(stack_operation: StackOperation):
    """Test 1 pop and 1 peek of the stack after pushing 3 nodes."""
    node_data1 = STRING_DATA[0]
    node_data2 = STRING_DATA[1]
    node_data3 = STRING_DATA[2]
    stack_operation.push(node_data1)
    stack_operation.push(node_data2)
    stack_operation.push(node_data3)
    assert stack_operation.pop() == node_data3
    assert stack_operation.peek() == node_data2


def test_is_empty_init(stack_operation: StackOperation):
    """Test if the stack is empty."""
    assert stack_operation.is_empty()


def test_is_empty_push1(stack_operation: StackOperation):
    """Test if the stack is empty after pushing 1 node."""
    node_id1 = random.randint(START_ID, FINISH_ID)
    stack_operation.push(node_id1)
    assert not stack_operation.is_empty()


def test_is_empty_push1_pop1(stack_operation: StackOperation):
    """Test if the stack is empty after pushing 1 node and popping 1."""
    node_id1 = random.randint(START_ID, FINISH_ID)
    stack_operation.push(node_id1)
    stack_operation.pop()
    assert stack_operation.is_empty()


def test_is_empty_push1_peek1(stack_operation: StackOperation):
    """Test if the stack is empty after pushing 1 node and peeking 1."""
    node_id1 = random.randint(START_ID, FINISH_ID)
    stack_operation.push(node_id1)
    stack_operation.peek()
    assert not stack_operation.is_empty()


def test_is_empty_push2_pop2(stack_operation: StackOperation):
    """Test if the stack is empty after pushing 2 nodes and popping 2."""
    node_id1 = random.randint(START_ID, FINISH_ID)
    node_id2 = random.randint(START_ID, FINISH_ID)
    stack_operation.push(node_id1)
    stack_operation.push(node_id2)
    stack_operation.pop()
    stack_operation.pop()
    assert stack_operation.is_empty()


def test_is_empty_push2_peek2(stack_operation: StackOperation):
    """Test if the stack is empty after pushing 2 nodes and peeking 2."""
    node_id1 = random.randint(START_ID, FINISH_ID)
    node_id2 = random.randint(START_ID, FINISH_ID)
    stack_operation.push(node_id1)
    stack_operation.push(node_id2)
    stack_operation.peek()
    stack_operation.peek()
    assert not stack_operation.is_empty()


def test_push_null_element_exception(stack_operation: StackOperation):
    """Test NullElementException for pushing a None value."""
    with pytest.raises(NullElementException):
        stack_operation.push(None)

def test_pop_empty_stack_exception(stack_operation: StackOperation):
    """Test EmptyStackException for popping when the stack is empty."""
    with pytest.raises(EmptyStackException):
        stack_operation.pop()


def test_peek_empty_stack_exception(stack_operation: StackOperation):
    """Test EmptyStackException for peeking when the stack is empty."""
    with pytest.raises(EmptyStackException):
        stack_operation.peek()

