class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class Stack:
    def __init__(self):
        self.length = 0
        self.head = None

    # goes in the head
    def push(self, value):
        node = Node(value)

        if self.is_empty():
            self.length += 1
            self.head = node
            return self

        self.length += 1
        node.next = self.head
        self.head = node
        return self

    # leaves the head
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        self.length -= 1

        head = self.head
        self.head = head.next
        head = None

    def peek(self):
        if self.is_empty():
            return None

        return self.head.value

    def is_empty(self):
        return self.head is None


mystack = Stack()

mystack.push(1).push(2).push(3).push(4).push(5).push(6)

print(mystack.peek())

mystack.pop()
print(mystack.peek())

mystack.pop()
print(mystack.peek())

mystack.pop()
print(mystack.peek())

mystack.pop()
print(mystack.peek())

mystack.pop()
print(mystack.peek())

mystack.pop()
print(mystack.peek())

mystack.pop()
print(mystack.peek())
