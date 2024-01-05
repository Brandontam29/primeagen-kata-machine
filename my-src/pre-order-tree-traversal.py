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


def walk(curr: BinaryNode, path: list[int]):
    if not curr:
        return

    path.append(curr.value)
    walk(curr.left, path)
    walk(curr.right, path)


def pre_order_search(head: BinaryNode) -> list[int]:
    path = []
    walk(head, path)
    return path


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

print(pre_order_search(one))

#      1
#    /   \
#   2     3
#  / \   / \
# 4  5  6   7
#
# [1, 2, 4, 5, 3, 6, 7]
