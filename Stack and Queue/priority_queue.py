
from stack_queue_adt import PriorityQueueADT, EmptyStructure


class PriorityQueue(PriorityQueueADT):

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def add(self, key, value):
        item = (key, value)
        self._data.append(item)

    def min(self):
        if self.is_empty():
            raise EmptyStructure("Queue is empty")
        result = self._data[0]
        pos = 0
        while pos < len(self._data):
            item = self._data[pos]
            if item[0] < result[0]:
                result = item
            pos += 1
        return result

    def remove_min(self):
        if self.is_empty():
            raise EmptyStructure("Queue is empty")
        return self._data.remove(self.min())

    def is_empty(self):
        return len(self._data) == 0

    def get_size(self):
        return len(self._data)
