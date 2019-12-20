from doubly_linked_list import DoublyLinkedList

#  When the ring buffer is full and a new element is inserted, 
# the oldest element in the ring buffer is overwritten with the newest element

# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = 0 #set to 0 no None
#         self.storage = DoublyLinkedList()
# # The append method adds elements to the buffer
# # The get method, which is provided, returns all 
# # of the elements in the buffer in a list in their given order
# # It should not return any None values in the list even if 
# # they are present in the ring buffer

    # def append(self, item):
    #     if len(self.storage) == self.capacity:

    #           self.storage[self.current] = item
    #         self.current += 1
    #     if self.current != self.capacity:
    #         self.current == 0

    # def get(self):
    #     # Note:  This is the only [] allowed
    #     value = []
    #     storage = [i for i in self.storage if i is not None]
    #     return value
# SOME REALLY REALLY UGLY CODE

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current is not self.capacity -1:
            self.current += 1
        else:
            self.current = 0
    #possibly some redundant code

    def get(self):
        return [item for item in self.storage if item is not None]


buffer = RingBuffer(3)

print(buffer.get())  # should return [] TESTED pass

buffer.append("p")
buffer.append('o')
buffer.append('p')

print(buffer.get())   # ['p', 'o', 'p'] TESTED pass

# 'c' overwrites the oldest value in the ring buffer, which is 'p'
buffer.append('c')

print(buffer.get())   # ['c', 'o', 'p'] TESTED pass

buffer.append('a')
buffer.append('n')

print(buffer.get())   # ['c', 'a', 'n'] TESTED pass

buffer.append('c')
buffer.append('a')
buffer.append('t')

print(buffer.get())   # ['c', 'a', 't'] TESTED pass

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
