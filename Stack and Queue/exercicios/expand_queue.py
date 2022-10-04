
from abc import ABC, abstractmethod


class EmptyStructure(Exception):
    pass


class FullStructure(Exception):
    pass


class QueueEdADT(ABC):

    @abstractmethod
    def enqueue(self, elem):
        """Enfileira <elemento>"""
        pass

    @abstractmethod
    def dequeue(self):
        """Desenfileira elemento da pilha"""
        pass

    @abstractmethod
    def first(self):
        """Verifica qual eh o elemento que esta no inicio da fila, sem remove-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a fila esta vazia"""
        pass

    def get_size(self):
        """Retorna o tamanho da fila"""
        pass


class Queue(QueueEdADT):

    def __init__(self, maxlen=None):
        self._data = list()
        self._maxlen = maxlen

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def enqueue(self, elem):
        if self._maxlen:
            if self.get_size() >= self._maxlen:
                raise FullStructure("Queue is at max capacity!")
        self._data.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise EmptyStructure('Queue is empty')
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise EmptyStructure('Queue is empty')
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def get_size(self):
        return len(self._data)
