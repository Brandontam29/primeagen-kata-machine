class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    # goes in the tail
    def enqueue(self, value):
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

    def peek(self):
        if self.is_empty():
            return None

        return self.head.value

    def is_empty(self):
        return self.head is None


myqueue = Queue()

myqueue.enqueue(1).enqueue(2).enqueue(3).enqueue(4).enqueue(5).enqueue(6)

print(myqueue.peek())

myqueue.deque()
print(myqueue.peek())

myqueue.deque()
print(myqueue.peek())

myqueue.deque()
print(myqueue.peek())

myqueue.deque()
print(myqueue.peek())

myqueue.deque()
print(myqueue.peek())

myqueue.deque()
print(myqueue.peek())

myqueue.deque()
print(myqueue.peek())
