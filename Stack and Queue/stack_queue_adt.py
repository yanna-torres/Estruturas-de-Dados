
"""
Created on Wed Sep 28 08:41:05

@author: Yanna Torres
"""

from abc import ABC, abstractmethod


class EmptyStack(Exception):
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
