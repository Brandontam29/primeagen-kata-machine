from typing import Optional


class BinaryNode:
    def __init__(
        self,
        value: int,
        left: Optional["BinaryNode"] = None,
        right: Optional["BinaryNode"] = None,
    ):
        self.value = value
        self.left = left
        self.right = right


class Node:
    def __init__(self, value: BinaryNode):
        self.value = value
        self.next = None


# first in first out
class Queue:
    def __init__(self):
        self.length = 0
        self.head: Optional["Node"] = None
        self.tail: Optional["Node"] = None

    # goes in the tail
    def enqueue(self, value: BinaryNode):
        node = Node(value)

        if self.is_empty():
            self.length += 1
            self.head = self.tail = node
            return self

        self.length += 1
        self.tail.next = node
        self.tail = node
        return self

    # leaves the head
    def deque(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        self.length -= 1

        head = self.head
        self.head = head.next
        head = None
        return self

    def peek(self):
        if self.is_empty():
            return None

        return self.head.value

    def is_empty(self):
        return self.head is None


def print_breadth_first_search(
    head: BinaryNode,
) -> bool:
    queue = Queue()
    queue.enqueue(head)

    while queue.length:
        node = queue.head.value
        queue.deque()

        print(node.value)

        if node.left:
            queue.enqueue(node.left)

        if node.right:
            queue.enqueue(node.right)


one = BinaryNode(1)
two = BinaryNode(2)
three = BinaryNode(3)
four = BinaryNode(4)
five = BinaryNode(5)
six = BinaryNode(6)
seven = BinaryNode(7)

one.left = two
one.right = three

two.left = four
two.right = five

three.left = six
three.right = seven
one.right.right = None
print_breadth_first_search(one)
