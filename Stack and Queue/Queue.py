
from stack_queue_adt import QueueEdADT, EmptyStack


class Queue(QueueEdADT):

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def enqueue(self, elem):
        self._data.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise EmptyStack('Queue is empty')
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise EmptyStack('Queue is empty')
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def get_size(self):
        return len(self._data)

