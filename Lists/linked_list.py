
from list_adt import ListADT


class Node:

    def __init__(self, element=None, next_element=None):
        self._element = element
        self._next = next_element

    def __str__(self):
        return '|' + self._element.__str__() + '|'


class LinkedList(ListADT):

    def __init__(self, elem=None):
        if elem:
            self._head = Node(elem)  # AtenÃ§Ã£o ao manipular esta referÃªncia
            self._tail = self._head  # Facilita a inserÃ§Ã£o no fim da lista
            self._length = 1
        else:
            self._head = None  # AtenÃ§Ã£o ao manipular esta referÃªncia
            self._tail = None  # Facilita a inserÃ§Ã£o no fim da lista
            self._length = 0

    def insert(self, indice, elem):
        """Insere <elemento> na posicao <index>"""
        # a insercao pode acontecer em tres locais: inicio, meio e fim da lista
        # separei em metodos diferentes (privados) para facilitar o entendimento
        if indice == 0:  # primeiro local de insercao no comeco da lista
            self.__insert_at_beginning(elem)
        elif indice > self._length:  # segundo local de insercao no fim da lista
            self.__insert_at_end(elem)  # se o indice passado foi maior que o tamanho da lista, insero no fim
        else:  # por fim, a insercao no meio da lista
            self.__insert_in_between(indice, elem)

        self._length += 1  # apos inserido, o tamanho da lista eh modificado

    def __insert_at_beginning(self, elem):
        n = Node(elem)  # primeiro criamos o nÃ³ com o elemento a ser inserido
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:  # se houver elemento na lista
            n._next = self._head  # o head atual passa a ser o segundo elemento
            self._head = n  # e o novo nÃ³ criado passa a ser o novo head

    def __insert_at_end(self, elem):
        n = Node(elem)  # primeiro criamos o nÃ³ com o elemento a ser inserido
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:
            self._tail._next = n  # o Ãºltimo elemento da lista aponta para o nÃ³ criado
            self._tail = n  # o nÃ³ criado passa a ser o Ãºltimo elemento

    def __empty_list_insertion(self, node):
        # na inserÃ§Ãµa na lista vazia, head e tail apontam para o nÃ³
        self._head = node
        self._tail = node

    def __insert_in_between(self, index, elem):  # 3
        n = Node(elem)  # primeiro criamos o nÃ³ com o elemento a ser inserido
        pos = 0  # a partir daqui vamos localizar a posiÃ§Ã£o de inserÃ§Ã£o
        aux = self._head  # variÃ¡vel auxiliar para nos ajudar na configuraÃ§Ã£o da posiÃ§Ã£o do novo nÃ³
        while pos < index - 1:  # precorre a lista atÃ© a posiÃ§Ã£o imediatamente anterior
            aux = aux._next  # Ã  posiÃ§Ã£o onde o elemento serÃ¡ inserido
            pos += 1
        n._next = aux._next  # quando a posiÃ§Ã£o correta tiver sido alcanÃ§ada, insere o nÃ³
        aux._next = n

    def remove(self, elem):
        if not self.empty():  # so pode remover se a lista nao estiver vazia
            pos = 1  # pos = 1, pois para a posicao 0 eh verificado separadamente
            aux = self._head  # comeca no head
            if aux._element == elem:  # Caso especial: elemento a ser removido esta no head
                self._head = aux._next  # head passa a ser o segundo elemento da lista
            else:
                removed = False  # Flag que marca quando a remoÃ§Ã£o foi feita
                while pos < self._length and not removed:  # verifico se estamos no fim da lista e nÃ£o foi removido elemento
                    prev = aux
                    aux = aux._next  # passo para o prÃ³ximo elemento
                    if aux._element == elem:  # se for o elemento desejado, removo da lista
                        prev._next = aux._next
                        removed = True  # marco que foi removido
                        self._length -= 1  # diminui o tamanho da lista
                    pos += 1

    def remove_at(self, indice):
        if not self.empty():  # se a lista não tiver vazia
            pos = 1  # pos inicial igual a 1, pq o indice 0 eh analisado separadamente
            aux = self._head  # comeca no head
            # Vamos percorrer a lista em busca de indice
            if indice < self._length:  # se o indice estiver nos limites da lista
                if indice == 0:  # Caso especial: indice a ser removido eh o head (0)
                    self._head = aux._next  # head passa a ser o segundo elemento (1) da lista
                else:
                    removed = False  # para o loop parar
                    while pos < self._length and not removed:
                        prev = aux
                        aux = aux._next  # passa para o proximo elemento
                        if pos == indice:  # se a pos atual for igual o indice
                            removed = True  # para o loop parar
                            self._length -= 1  # diminui o tamanho da lista
                            prev._next = aux._next  # atualiza as referencias
                        pos += 1

    def count(self, elem):
        counter = 0
        if not self.empty():  # Verifica se a lista nÃ£o estÃ¡ vazia (sÃ³ faz sentido contar em lists nÃ£o vazias!)
            aux = self._head  # Se a lista nÃ£o estiver vazia, percorre a lista contando as ocorrÃªncias
            if aux._element is elem:
                counter += 1
            while aux._next:  # precorrendo a lista....
                aux = aux._next
                if aux._element is elem:
                    counter += 1
        return counter

    def clear(self):
        self._head = None  # todos os nÃ³s que compunham a lista serÃ£o removidos da memÃ³ria pelo coletor de lixo
        self._tail = None
        self._length = 0

    def index(self, elemento):
        result = None
        pos = 0
        aux = self._head
        # Vamos percorrer a lista em busca de elemento
        while not result and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if aux._element is elemento:
                result = pos
            aux = aux._next
            pos += 1
        return result  # se o elemento nÃ£o estiver na lista, retorna None

    def length(self):
        return self._length

    def empty(self):
        """Verifica se a lista esta vazia"""
        result = False
        if not self._head:
            result = True
        return result

    def element_at(self, indice):
        found = False
        result = None  # variavel para controlar o que ira ser retornado
        pos = 0  # pos se inicia em 0, pois nao ha caso especial nesta funcao
        aux = self._head  # comeca no elemento (0) head
        # Vamos percorrer a lista em busca de indice
        if indice < self._length:  # se o indice passado esta dentro dos limites
            while pos < self._length and not found:
                if pos == indice:  # se a pos for igual o indice passado
                    found = True  # elemento encontrado
                    result = aux._element  # resultado igual o elemento na posicao
                aux = aux._next  # passa para o proximo elemento
                pos += 1
        return result  # devolve ou None ou o elemento na posicao

    def replace_at(self, indice, elemento):
        # segue a mesma logica do metodo {element_at} e {index}, mas nao retorna nada so atualiza os valores
        found = False  # se ja encontrou o indice
        pos = 0  # pos se inicia em 0, pois nao ha caso especial nesta funcao
        aux = self._head  # comeca no elemento (0) head
        # Vamos percorrer a lista em busca de indice
        if indice < self._length:  # se o  indice passado esta dentro dos limites
            while pos < self._length and not found:
                if pos == indice:  # se a pos for igual o indice passado
                    found = True  # elemento encontrado
                    aux._element = elemento  # atualiza o valor da posicao atual pelo passado
                aux = aux._next  # passa para o proximo elemento
                pos += 1

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._head
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'

    def __len__(self):
        return self._length
