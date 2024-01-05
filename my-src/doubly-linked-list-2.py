class Node:
    def __init__(self, value: int):
        self.value = value
        self.prev: None | Node = None
        self.next: None | Node = None


class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def prepend(self, value):
        newNode = Node(value)
        self.length += 1
        if self.length == 1:
            self.head = newNode
            self.tail = newNode
            return self

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

        return self

    def append(self, value):
        newNode = Node(value)
        self.length += 1
        if self.length == 1:
            self.head = newNode
            self.tail = newNode
            return self

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

        return self

    def remove_at(self, index: int):
        if index >= self.length:
            raise Exception("remove_at is targeting out of bound")

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
            return self

        if index == self.length:
            before_tail = self.tail.prev
            before_tail.next = None
            self.tail = before_tail
            return self

        if index == 0:
            head = self.head
            self.head = head.next

            head = None
            return self

        curr = self.head
        for _ in range(index):
            curr = curr.next

        prev = curr.prev
        next = curr.next
        prev.next = next
        next.prev = prev
        curr = None
        return self

    def get_at(self, index):
        if index >= self.length:
            raise Exception("get_at is targeting out of bound")

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.value

    def debug(self):
        out = ""
        curr = self.head

        if not curr:
            print("length is 0")
        out += str.format("{}: {};  ", 0, curr.value)
        for n in range(self.length - 1):
            curr = curr.next
            out += str.format("{}: {};  ", n, curr.value)

        print(out)


ll = DoublyLinkedList()

ll.append(1).append(2).append(3).append(4).append(5).prepend(0)

ll.debug()

ll.remove_at(0)
ll.remove_at(1)

ll.debug()

print(ll.get_at(2))
