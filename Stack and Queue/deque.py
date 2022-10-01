
# from stack_queue_adt import DequeADT, EmptyStructure
from abc import ABC, abstractmethod


class EmptyStructure(Exception):
    pass


class DequeADT(ABC):

    @abstractmethod
    def add_first(self, elem):
        """Insere <elemento> na frente"""
        pass

    @abstractmethod
    def add_last(self, elem):
        """Insere <elemento> atras do deque"""
        pass

    @abstractmethod
    def remove_first(self):
        """Remove <elemento> da frente"""
        pass

    @abstractmethod
    def remove_last(self):
        """Remove <elemento> de tras"""
        pass

    @abstractmethod
    def first(self):
        """Verifica qual <elemento> esta na frente"""
        pass

    @abstractmethod
    def last(self):
        """Verifica qual <elemento> esta no fim"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verfica se o deque esta vazio"""
        pass

    @abstractmethod
    def get_size(self):
        """Retorna o tamanho do deque"""
        pass


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
