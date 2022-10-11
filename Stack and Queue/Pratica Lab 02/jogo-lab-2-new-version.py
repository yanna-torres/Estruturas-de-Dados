from enum import IntEnum, unique
from abc import ABC, abstractmethod
import random


def gerador_numero(maximo, minimo=0):
    """Função que gera um número entre dois limites"""
    random.seed(1)
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

    def __len__(self):
        return len(self.__rio)

    def __inicio_do_mundo(self):
        """Método privado para inicializar o mundo"""
        qtd_peixe = round(len(self.__rio) * 0.2)
        qtd_urso = round(len(self.__rio) * 0.4)
        self.__gerar_animal(qtd_peixe, Peixe)
        self.__gerar_animal(qtd_urso, Urso)

    def __gerar_animal(self, qtd, classe):
        bicho = 0
        while bicho < qtd:
            indice = gerador_numero(len(self.__rio))
            if not self.__rio[indice]:
                self.__rio[indice] = classe()
                bicho += 1

    def fluir(self):
        iteracao = 0
        while iteracao < 5:
            for i in range(len(self.__rio)):
                if self.__rio[i]:
                    a = self.__rio[i]
                    pos = a.andar()
                    new_pos = (pos + i) % len(self.__rio)
                    if new_pos != i:
                        if self.__rio[new_pos]:
                            if isinstance(a, Urso):
                                self.__movimento_urso(a, i, new_pos)
                            elif isinstance(a, Peixe):
                                if a.reproduzir(self.__rio[new_pos]):
                                    self.__gerar_animal(1, Peixe)
                                else:
                                    self.__rio[i] = None
                        else:
                            # efetivamente ando aqui!!!
                            self.__rio[new_pos] = self.__rio[i]
                            self.__rio[i] = None
            iteracao += 1

    def __movimento_urso(self, a, atual, seguinte):
        elem_outra_posicao = self.__rio[seguinte]
        if isinstance(elem_outra_posicao, Urso):
            if a.reproduzir(self.__rio[seguinte]):
                self.__gerar_animal(1, Urso)
            else:
                a.brigar(elem_outra_posicao)
                if not a.get_forca():
                    self.__rio[atual] = None
                elif not elem_outra_posicao.get_forca():
                    self.__rio[seguinte] = None

        elif a.comer(elem_outra_posicao):
            self.__rio[seguinte] = None

    def __movimento_peixe(self, animal, new_pos, old_pos):
        if animal.reproduzir(self.__rio[new_pos]):
            self.__gerar_animal(1, Peixe)
        else:
            self.__rio[old_pos] = None

    def __str__(self):
        s = '| '
        for i in range(len(self.__rio)):
            s = s + self.__rio[i].__str__() + ' |'
        return s


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
        self._forca = gerador_numero(7, 4)

    def andar(self):
        return gerador_numero(Direcao.DIREITA + 1, Direcao.ESQUERDA)

    def comer(self, animal):
        result = False
        if isinstance(animal, Peixe):
            result = True
        return result

    def reproduzir(self, animal):
        result = False
        if isinstance(animal, Urso) and self.get_forca() == animal.get_forca():
            result = True
        return result

    def brigar(self, urso):
        if isinstance(urso, Urso):
            if self.get_forca() > urso.get_forca():
                self.set_forca(self.get_forca() + 1)
                urso.set_forca(urso.get_forca() - 1)
            elif urso.get_forca() > self.get_forca():
                self.set_forca(self.get_forca() - 1)
                urso.set_forca(urso.get_forca() + 1)

    def get_forca(self):
        return self._forca

    def set_forca(self, forca):
        self._forca = forca

    def __str__(self):
        return 'Urso'


if __name__ == '__main__':
    r = Rio(15)
    print(r)
    r.fluir()
    print(r)


"""
Parte 02:

Na minha opniao, as estruturas pilha, fila, deque e outras não seriam boas opcoes para representar o rio. Por si so,
essas estruturas nao possuem os metodos de verificar elementos no meio delas, geralmente so ha metodos para verificar
os elementos no comeco ou  fim. Ocorre a mesma situacao nos metodos de remover e adicionar.

No caso da pilha, o ultimo que entra eh o primeiro que sai e so ha o metodo de verificar o elemento no topo (o ultimo a
ser inserido).
Na fila, o primeiro que entra eh o primeiro que sai, e so ha o metodo de verificar o primeiro elemento dessa fila.
Com a fila com prioridade, o que poderia ser essa 'prioridade'? Ja que o funcionamento dessa estrutura eh todo baseado
na prioridade que um certo elemento possui (e o elemento com menor prioridade eh o primeiro a sair).
Por fim, o deque ainda pode ser considerado o mais usavel, ja que ha como inserir no comeco e no fim e o rio funciona
atraves de um 'for'. Contudo, ao implementar o deque, o rio iria estar cheio de remover no fim e inserir no comeco ou 
o oposto.

Claro que ha formas dessas estruturas serem implementadas, mas teriam que haver metodos costumizados que nao existem
nas 'originais', por assim dizer, e no geral seriam mais complicadas de serem implementadas exatamente por isso.
"""