
from abc import ABC, abstractmethod


class EmptyStructure(Exception):
    pass


class PriorityQueueADT(ABC):

    @abstractmethod
    def add(self, key, value):
        """Adiciona uma tupla com uma chave <key> e valor <value>"""
        pass

    @abstractmethod
    def min(self):
        """Retorna a tupla (key, value) onde o <key> eh o menor valor, sem remover a tupla"""
        pass

    @abstractmethod
    def remove_min(self):
        """Remove a tupla (key, value) onde o <key> eh o menor valor"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a lista esta vazia"""
        pass

    @abstractmethod
    def get_size(self):
        """Retorna o tamanho da fila"""
        pass


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
        for e in self._data:
            if e[0] < result[0]:
                result = e
        return result

    def remove_min(self):
        if self.is_empty():
            raise EmptyStructure("Queue is empty")
        return self._data.remove(self.min())

    def priority(self, priority_value):
        """Localiza a primeira ocorrencia de <priority_value>"""
        if self.is_empty():
            raise EmptyStructure("Queue is empty")
        result = self._data[0]
        found = False
        for e in self._data:
            if e[0] == priority_value and not found:
                found = True
                result = e
        return result

    def remove_priority(self, priority_value):
        """Remove a primeira ocorrencia que possui a prioridade <priority_value>"""
        if self.is_empty():
            raise EmptyStructure("Queue is empty")
        return self._data.remove(self.priority(priority_value))

    def is_empty(self):
        return len(self._data) == 0

    def get_size(self):
        return len(self._data)

