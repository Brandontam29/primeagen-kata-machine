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


# first in last out
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


def breadth_first_search(head: BinaryNode, needle: int) -> bool:
    queue = Queue()
    queue.enqueue(head)

    while queue.length:
        node = queue.head.value
        queue.deque()

        if node.value == needle:
            return True

        if node.left:
            queue.enqueue(node.left)

        if node.right:
            queue.enqueue(node.right)

    return False


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

print("/*** TRUES ***/")
print(breadth_first_search(one, 1))
print(breadth_first_search(one, 2))
print(breadth_first_search(one, 3))
print(breadth_first_search(one, 4))
print(breadth_first_search(one, 5))
print(breadth_first_search(one, 6))
print(breadth_first_search(one, 7))

print("/*** FALSES ***/")
print(breadth_first_search(one, 8))
print(breadth_first_search(one, 0))
print(breadth_first_search(one, 10))
print(breadth_first_search(one, 11))

#      1
#    /   \
#   2     3
#  / \   / \
# 4  5  6   7
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
