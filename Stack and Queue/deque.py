
from stack_queue_adt import DequeADT, EmptyStructure


class Deque(DequeADT):

    def __init__(self):
        self._data = list()

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def add_first(self, elem):
        self._data.insert(0, elem)

    def add_last(self, elem):
        self._data.append(elem)

    def remove_first(self):
        if self.is_empty():
            raise EmptyStructure('Deque is empty')
        return self._data.pop(0)

    def remove_last(self):
        if self.is_empty():
            raise EmptyStructure('Deque is empty')
        return self._data.pop()

    def first(self):
        if self.is_empty():
            raise EmptyStructure('Deque is empty')
        return self._data[0]

    def last(self):
        if self.is_empty():
            raise EmptyStructure('Deque is empty')
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def get_size(self):
        return len(self._data)
