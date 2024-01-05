class DoublyLinkedList:
    previous = None
    next = None
    value = None

    def __init__(self, value):
        self.value = value

    def add_node(self, value):
        new_node = DoublyLinkedList(value)

        self.next = new_node
        new_node.previous = self

        return new_node

    def remove_node(self):
        previous_node = self.previous
        next_node = self.next

        self = None

        if not previous_node and not next_node:
            return

        if previous_node and not next_node:
            previous_node.next = None
            return

        if next_node and not previous_node:
            next_node.previous = None
            return

        if next_node and previous_node:
            next_node.previous = previous_node
            previous_node.next = next_node
            return

    def find_head(self):
        if self.previous:
            return self.previous.find_head()

        return self

    def find_value(self, target):
        if self.value == target:
            return self

        if not self.next:
            return None

        return self.next.find_value(target)

    def print_all(self):
        print(self.value)

        if self.next:
            self.next.print_all()


ll = DoublyLinkedList(0)

ll.add_node(1).add_node(2).add_node(3).add_node(4).add_node(5)

ll.print_all()

found_node = ll.find_value(4)


found_node.print_all()
