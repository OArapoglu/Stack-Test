from typing import Any
from stack import Stack
from node import Node
from exception import NullElementException, EmptyStackException


class StackOperation(Stack):
    """
    This is a class for stack operations.

    Attributes:
        root (Node | None): The root node of the stack.
    """

    def __init__(self):
        """Constructor for StackOperation class."""
        self.root = None

    def push(self, data: Any):
        """
        Push a node into the stack.

        Parameters:
            data (Any): The node id for a Node.
        """
        if data:
            node = Node(data)
            if self.root is None:
                self.root = node
            else:
                node.next = self.root
                self.root = node
        else:
            raise NullElementException()

    def pop(self) -> Any:
        """
        Pop a node from the stack.

        Returns:
            data(Any): The data of the popped node.
        """
        if self.is_empty():
            raise EmptyStackException()
        temp = self.root
        self.root = temp.next
        return temp.data

    def peek(self) -> Any:
        """
        Peek a node from the stack.

        Returns:
            data(Any): The data of the peeked node.
        """
        if self.is_empty():
            raise EmptyStackException()
        return self.root.data

    def get_size(self) -> int:
        """
        Get the size of the stack.

        Returns:
            stack_size: The number of nodes in the stack.
        """
        stack_size = 0
        current = self.root
        while current:
            stack_size += 1
            current = current.next
        return stack_size

    def is_empty(self) -> bool:
        """Tests whether the stack is empty or not."""
        return not bool(self.root)

    def display(self):
        """Display all nodes in the stack."""
        if self.is_empty():
            raise EmptyStackException()
        print("The nodes in the stack:")
        current = self.root
        while current:
            print(f"Node {current}")
            current = current.next
        print("************************************")


def print_selection():
    """Selection list."""
    print("************************************")
    print(
        "1-Push a node into the stack.\n"
        "2-Pop a node from the stack.\n"
        "3-Peek a node from the stack.\n"
        "4-Show the size of the stack.\n"
        "5-Display all the nodes of the stack.\n"
        "6-Exit.\n"
    )
    print("************************************")


def main():
    """Main program for stack operations."""
    stack_operation = StackOperation()
    while True:
        try:
            print_selection()
            selection = input("Enter your selection:")
            if selection == "1":
                data = input("Enter node id:")
                stack_operation.push(data)
            elif selection == "2":
                print(f"The node {stack_operation.pop()} is popped.")
            elif selection == "3":
                print(f"The node {stack_operation.peek()} is peeked.")
            elif selection == "4":
                print(f"The size of the stack is {stack_operation.get_size()}")
            elif selection == "5":
                stack_operation.display()
            elif selection == "6":
                break
            else:
                print("The selection is invalid!")
        except ValueError:
            print("You must enter integer value for node id!")


if __name__ == "__main__":
    main()
