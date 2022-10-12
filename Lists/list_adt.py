
"""
Created on Tue Sep 21 19:50:12 2022

@author: Yanna Torres
"""

from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """Insere <elemento> na posicao <indice>"""
        pass

    @abstractmethod
    def append(self, elemento):
        """Adiciona um elemento ao fim da lista"""
        pass

    @abstractmethod
    def remove(self, elemento):
        """Remove primeira ocorrencia de <elemento>"""
        pass

    @abstractmethod
    def remove_at(self, indice):
        """Remove o elemento na posicao <indice>"""
        pass

    @abstractmethod
    def replace_at(self, indice, elemento):
        """Substitui o elemento na posicao <indice> po <elemento>"""
        pass

    @abstractmethod
    def clear(self):
        """Apaga a lista"""
        pass

    @abstractmethod
    def count(self, elemento):
        """Conta a quantidade de <elemento> na lista"""
        pass

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro indice de <elemento>"""
        pass

    @abstractmethod
    def element_at(self, indice):
        """Retorna o elemento na posicao <indice>"""
        pass

    @abstractmethod
    def length(self):
        """Retorna o tamanho da lista"""
        pass


