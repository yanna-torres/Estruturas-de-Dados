
from stack_queue_adt import StackADT, EmptyStructure


class Stack(StackADT):

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def push(self, elem):
        self._data.append(elem)

    def pop(self):
        if self.is_empty():
            raise EmptyStructure('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise EmptyStructure('Stack is empty')
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def get_size(self):
        return len(self._data)
