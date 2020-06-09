"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class Queue:
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

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def dequeue(self):
#         if not self.storage:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop(0)

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        if not self.head:
            return self.size
        else:
            while self.head.next_node is not None:
                self.size + 1
            return self.size

    def enqueue(self, value):
        new_node = Node(value)
        head = self.head
        if not self.head:
            self.head = new_node
            self.size += 1
        else:
            while head.get_value() is not None:
                head = self.head.get_next()
            self.size += 1
            head.set_next(new_node)

    def dequeue(self):
        if not self.head:
            return None
        else:
            while self.head is not None:
                self.head = self.head.get_next()
            removed_value = self.head.get_value()
            self.head = self.head.get_next()
            return removed_value
