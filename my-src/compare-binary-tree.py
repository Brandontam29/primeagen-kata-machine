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


def compare_binary_tree(a: Optional["BinaryNode"], b: Optional["BinaryNode"]):
    if a == None and b == None:
        return True

    if a == None or b == None:
        return False

    if a.value != b.value:
        return False

    return compare_binary_tree(a.left, b.left) and compare_binary_tree(a.right, b.right)


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

one2 = BinaryNode(1)
two2 = BinaryNode(2)
three2 = BinaryNode(3)
four2 = BinaryNode(4)
five2 = BinaryNode(5)
six2 = BinaryNode(6)
seven2 = BinaryNode(7)

one2.left = two2
one2.right = three2

two2.left = four2
two2.right = five2

three2.left = six2
three2.right = seven2


print(compare_binary_tree(one, one2))

one2.right.right = None

print(compare_binary_tree(one, one2))
