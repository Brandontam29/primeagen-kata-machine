import math
from typing import List


class Heap:
    def __init__(self, data):
        self.data: List[int] = data

    def heapify_up(self, index):
        v = self.data[index]
        parentI = self.find_parent_index(index)
        parentV = self.data[parentI]

        while index != 0:
            if v > parentV:
                break

            self.data[parentI] = v
            self.data[index] = parentV

            index = parentI
            v = self.data[index]
            parentI = self.find_parent_index(index)
            parentV = self.data[parentI]

    def insert(self, n):
        self.data.append(n)
        self.heapify_up(len(self.data) - 1)

    def heapify_down(self, index):
        (li, ri) = self.find_children(index)

        if index >= len(self.data) or li >= len(self.data) or ri >= len(self.data):
            return

        v = self.data[index]
        lv = self.data[li]
        rv = self.data[ri]

        if lv < rv and lv < v:
            self.data[index] = lv
            self.data[li] = v
            self.heapify_down(li)

        elif rv < lv and rv < v:
            self.data[index] = rv
            self.data[ri] = v
            self.heapify_down(ri)

    def delete(self, index):
        if len(self.data) == 0:
            return

        if len(self.data) == 1:
            out = self.data[0]
            self.data = []
            return out

        self.data[0] = self.data[-1]
        self.data = self.data[:-1]
        self.heapify_down(index)

    def find_children(self, index):
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        return (left_index, right_index)

    def find_parent_index(self, index):
        if index == 0:
            return 0

        parent_index = math.floor((index - 1) / 2)
        return parent_index

    def find_parent(self, index):
        if index == 0:
            return None

        parent_index = self.find_parent_index(index)
        return self.data[parent_index]

    def debug(self):
        n = len(self.data)
        if n == 0:
            print("Heap is empty")
            return

        # Calculate the height of the heap
        height = 0
        while (2**height - 1) < n:
            height += 1

        # Print the heap level by level
        index = 0
        for level in range(height):
            for i in range(2**level):
                if index < n:
                    print(self.data[index], end=" ")
                    index += 1
            print()

        print()


heap = Heap([50, 100, 200, 130, 101, 290, 220])
heap.debug()  # [0, 50, 200, 100, 101, 290, 220, 130]

heap.insert(0)
heap.debug()  # [0, 50, 200, 100, 101, 290, 220, 130]

heap.delete(0)
heap.debug()  # [0, 50, 200, 100, 101, 290, 220, 130]

heap.insert(30)
heap.insert(600)
heap.insert(31)
heap.insert(3)
heap.insert(145)
heap.insert(0)
heap.insert(222)
heap.insert(51)
heap.debug()  # [0, 50, 200, 100, 101, 290, 220, 130]

heap.delete(0)
heap.delete(0)
heap.delete(0)
heap.delete(0)
heap.debug()
