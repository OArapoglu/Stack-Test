class Node:
    """
    A node structure to keep a data and next pointer.

    Attributes:
        data(int): The data of the node.
        next(int): The next node of the current node.
    """

    def __init__(self, data: int):
        """Constructor for Node class."""
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
