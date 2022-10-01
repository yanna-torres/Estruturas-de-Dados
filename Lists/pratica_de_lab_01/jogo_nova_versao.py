# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:48:27 2022

@author: Yanna Torres
"""

import random
from enum import IntEnum, unique
from abc import ABC, abstractmethod
from lists import LinkedList


def gerador_numero(maximo, minimo=0):
    """Funcao que gera um numero entre dois limites"""
    return random.randrange(minimo, maximo)


@unique
class Direcao(IntEnum):
    ESQUERDA = -1
    DIREITA = 1
    PARADO = 0


class Rio:
    """Classe que modela e implementa o comportamento do rio"""

    def __init__(self, tamanho=100):
        self.__rio = self.__lista_vazia(tamanho)
        self.__inicio_do_mundo()

    @staticmethod
    def __lista_vazia(tamanho):
        lista = LinkedList()
        i = 0
        while i < tamanho:
            lista.insert(i, None)
            i += 1
        return lista

    def __inicio_do_mundo(self):
        """metodo privado para inicializar o mundo"""
        qtd_peixe = round(len(self.__rio) * 0.2)
        qtd_urso = round(len(self.__rio) * 0.5)
        self.__gerar_animal(qtd_peixe, Peixe)
        self.__gerar_animal(qtd_urso, Urso)

    def __gerar_animal(self, qtd, classe):
        """insere animais nas posicoes vazias"""
        bicho = 0
        while bicho < qtd:
            indice = gerador_numero(len(self.__rio))
            if not self.__rio.element_at(indice):
                self.__rio.replace(indice, classe())
                bicho += 1

    def fluir(self):
        iteracao = 0
        while iteracao < 15:
            for i in range(len(self.__rio)):
                # print("")
                # print(self.__str__())
                if self.__rio.element_at(i):
                    a = self.__rio.element_at(i)
                    pos = a.andar()
                    if 0 <= pos + i < len(self.__rio) and pos + i != i:
                        if self.__rio.element_at(pos + i):
                            if isinstance(a, Urso):
                                # print(f"urso na posicao {i} vai tentar se mover para a posicao {pos + i}")
                                self.__movimento_urso(i, pos + i)
                            elif isinstance(a, Peixe):
                                # print(f"peixe na posicao {i} vai tentar se mover para a posicao {pos + i}")
                                self.__movimento_peixe(i, pos + i)
                                if a.reproduzir(self.__rio.element_at(pos + i)):
                                    self.__gerar_animal(1, Peixe)
                                    # print("novo peixe")
                                else:
                                    # print("peixe morreu")
                                    self.__rio.replace(i, None)
                        else:
                            # print(f"animal na posicao {i} se moveu para a posicao {pos + i} que estava vazia")
                            self.__rio.replace(pos + i, self.__rio.element_at(i))
                            self.__rio.replace(i, None)
            iteracao += 1

    def __movimento_urso(self, i, new_pos):
        b = self.__rio.element_at(new_pos)
        a = self.__rio.element_at(i)
        if isinstance(b, Urso):
            if a.reproduzir(b):
                self.__gerar_animal(1, Urso)
                # print("novo urso add")
            else:
                a.brigar(b)
                self.__mata_urso(a, i)
                self.__mata_urso(b, i)
        elif a.comer(b):
            self.__rio.replace(new_pos, None)
            # print(f"urso na posicao {i} matou o peixe na posicao {new_pos}")

    def __movimento_peixe(self, old_pos, new_pos):
        b = self.__rio.element_at(new_pos)
        a = self.__rio.element_at(old_pos)
        if a.reproduzir(b):
            self.__gerar_animal(1, Peixe)
            # print("novo peixe")
        else:
            # print("peixe morreu")
            self.__rio.replace(old_pos, None)

    def __mata_urso(self, a, pos):
        if a.forca == 0:
            self.__rio.replace(pos, None)
            # print(f"urso morreu na posicao {pos}. sua forca zerou. forca = {a.forca}")

    def __str__(self):
        return self.__rio.__str__()

    def __len__(self):
        return len(self.__rio)


class Animal(ABC):

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self, animal):
        pass

    @abstractmethod
    def reproduzir(self, animal):
        pass


class Peixe(Animal):

    def andar(self):
        return gerador_numero(Direcao.DIREITA + 1, Direcao.ESQUERDA)

    def comer(self, animal):
        return False

    def reproduzir(self, animal):
        result = False
        if isinstance(animal, Peixe):
            result = True
        return result

    def __str__(self):
        return 'Peixe'


class Urso(Animal):

    def __init__(self):
        self.forca = gerador_numero(7, 4)

    def get_forca(self):
        return self.forca

    def set_forca(self, forca):
        self.forca = forca

    def andar(self):
        return gerador_numero(Direcao.DIREITA + 1, Direcao.ESQUERDA)

    def comer(self, animal):
        result = False
        if isinstance(animal, Peixe):
            result = True
        return result

    def reproduzir(self, animal):
        result = False
        if isinstance(animal, Urso):
            if self.get_forca() == animal.get_forca():
                result = True
        return result

    def brigar(self, animal):
        if isinstance(animal, Urso):
            if self.get_forca() > animal.get_forca():
                self.set_forca(self.get_forca() + 1)
                animal.set_forca(animal.get_forca() - 1)
            elif self.get_forca() < animal.get_forca():
                self.set_forca(self.get_forca() - 1)
                animal.set_forca(animal.get_forca() + 1)

    def __str__(self):
        return 'Urso'


if __name__ == '__main__':
    r = Rio(15)
    print(r)
    r.fluir()
    print(r)
