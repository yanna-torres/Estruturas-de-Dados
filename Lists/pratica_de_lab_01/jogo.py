# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:48:27 2022

@author: Yanna Torres
"""


import random
from enum import IntEnum, unique
from abc import ABC, abstractmethod


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
        self.__rio = [None] * tamanho
        self.__inicio_do_mundo()

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
            if not self.__rio[indice]:
                self.__rio[indice] = classe()
                bicho += 1

    def fluir(self):
        iteracao = 0
        while iteracao < 15:
            for i in range(len(self.__rio)):
                print("")
                print(self.__str__())
                if self.__rio[i]:
                    a = self.__rio[i]
                    pos = a.andar()
                    if 0 <= pos + i < len(self.__rio) and pos + i != i:
                        if self.__rio[pos + i]:
                            if isinstance(a, Urso):
                                print(f"urso na posicao {i} vai tentar se mover para a posicao {pos + i}")
                                self.__movimento_urso(i, pos + i)
                            elif isinstance(a, Peixe):
                                print(f"peixe na posicao {i} vai tentar se mover para a posicao {pos + i}")
                                if a.reproduzir(self.__rio[pos + i]):
                                    self.__gerar_animal(1, Peixe)
                                    print("novo peixe")
                                else:
                                    print("peixe morreu")
                                    self.__rio[i] = None
                        else:
                            print(f"animal na posicao {i} se moveu para a posicao {pos + i} que estava vazia")
                            self.__rio[pos + i] = self.__rio[i]
                            self.__rio[i] = None
                    else:
                        print(f"animal na posicao {i} não andou")
                else:
                    print(f"posicao {i} esta vazia")
            iteracao += 1

    def __movimento_urso(self, i, new_pos):
        b = self.__rio[new_pos]
        a = self.__rio[i]
        if isinstance(b, Urso):
            if a.reproduzir(self.__rio[new_pos]):
                self.__gerar_animal(1, Urso)
                print("novo urso add")
            else:
                a.brigar(self.__rio[new_pos])
                self.__mata_urso(a, i)
                self.__mata_urso(b, i)
        elif a.comer(self.__rio[new_pos]):
            self.__rio[new_pos] = None
            print(f"urso na posicao {i} matou o peixe na posicao {new_pos}")

    def __movimento_peixe(self, animal, new_pos, old_pos):
        if animal.reproduzir(self.__rio[new_pos]):
            self.__gerar_animal(1, Peixe)
        else:
            self.__rio[old_pos] = None
        pass

    def __str__(self):
        s = '| '
        for i in range(len(self.__rio)):
            s = s + self.__rio[i].__str__() + ' |'
        return s

    def __mata_urso(self, a, pos):
        if a.forca == 0:
            self.__rio[pos] = None
            print(f"urso morreu na posicao {pos}. sua forca zerou. forca = {a.forca}")


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
    r = Rio(8)
    print(r)
    r.fluir()
    print(r)
