
# from stack_queue_adt import StackADT, EmptyStructure
from abc import ABC, abstractmethod


class EmptyStructure(Exception):
    pass


class StackADT(ABC):

    @abstractmethod
    def push(self, elem):
        """Empilha <elemento>"""
        pass

    @abstractmethod
    def pop(self):
        """Desempilha elemento da pilha"""
        pass

    @abstractmethod
    def top(self):
        """Verifica qual eh o elemento que esta no topo da pilha, sem remove-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a pilha estÃ¡ vazia"""
        pass

    def get_size(self):
        """Retorna o tamanho da pilha"""
        pass


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
