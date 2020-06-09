"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         if not self.storage:
#             return self.size
#         else:
#             for element in self.storage:
#                 self.size + 1
#             return self.size

#     def push(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def pop(self):
#         if not self.storage:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node


class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        size = 0
        if not self.head:
            return size
        else:
            while self.head is not None:
                size + 1
                self.head = self.head.next_node
            return size

    def push(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.size += 1
        else:
            while self.tail.get_next() is not None:
                self.tail = self.tail.get_next()
            self.tail.set_next(new_node)
            self.size += 1

    def pop(self):

        if not self.tail:
            return None
        else:
            # removed_value = self.head.get_value()
            while self.tail.get_next() is not None:
                self.tail = self.tail.get_next()
                removed_value = self.tail.get_value()
            # print(self.tail.get_value(), 'valuyeeSeee')
            self.tail = self.tail.get_value()
            self.size -= 1
            print(self.size)
            return removed_value
