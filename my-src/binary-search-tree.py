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


def find_binary_search_tree(node: Optional["BinaryNode"], target: int) -> bool:
    if not node:
        return False

    if node.value == target:
        return True

    if target < node.value:
        return find_binary_search_tree(node.left, target)

    return find_binary_search_tree(node.right, target)


#           4
#       /       \
#      3         7
#     / \       / \
#    2   4     6   8
#   /         /
#  1         5
one = BinaryNode(1)
two = BinaryNode(2)
three = BinaryNode(3)
four = BinaryNode(4)
five = BinaryNode(5)
six = BinaryNode(6)
seven = BinaryNode(7)
eight = BinaryNode(8)

four.left = three
four.right = seven

three.left = two
three.right = four

two.left = one

seven.left = six
seven.right = eight

six.left = five

head = four

print("/*** TRUES ***/")
print(find_binary_search_tree(head, 1))
print(find_binary_search_tree(head, 2))
print(find_binary_search_tree(head, 3))
print(find_binary_search_tree(head, 4))
print(find_binary_search_tree(head, 5))
print(find_binary_search_tree(head, 6))
print(find_binary_search_tree(head, 7))
print(find_binary_search_tree(head, 8))

print("/*** FALSES ***/")
print(find_binary_search_tree(head, 0))
print(find_binary_search_tree(head, 10))
print(find_binary_search_tree(head, 11))
