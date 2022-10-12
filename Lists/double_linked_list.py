
from list_adt import ListADT


class DoublyLinkedList(ListADT):

    class _DoublyNode:

        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

        def __str__(self):
            if self._elem is not None:
                return str(self._elem) + ' '
            else:
                return '|'

    def __init__(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._header
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'

    def __len__(self):
        return self._length

    def insert(self, index, elem):
        if index >= self._length:  # se o indice se inserÃ§Ã£o passado for maior que a lista
            index = self._length  # atualiza para o Ãºltimo indice
        if self.empty():  # Caso da lista vazia
            new_node = self._DoublyNode(elem, self._header, self._trailer)
            self._header._next = new_node
            self._trailer._prev = new_node
        elif index == 0:  # caso da inserÃ§Ã£o na primeira posiÃ§Ã£o da lista
            new_node = self._DoublyNode(elem, self._header, self._header._next)
            self._header._next._prev = new_node
            self._header._next = new_node
        else:  # outros casos de inserÃ§Ã£o
            this = self._header._next
            successor = this._next
            pos = 0
            while pos < index - 1:
                this = successor
                successor = this._next
                pos += 1
            new_node = self._DoublyNode(elem, this, successor)
            this._next = new_node
            successor._prev = new_node

        self._length += 1

    def append(self, elemento):
        if self.empty():  # Caso da lista vazia
            new_node = self._DoublyNode(elemento, self._header, self._trailer)
            self._header._next = new_node
            self._trailer._prev = new_node
        else:  # outros casos de inserÃ§Ã£o
            this = self._header._next
            successor = this._next
            pos = 0
            while pos < self._length - 1:
                this = successor
                successor = this._next
                pos += 1
            new_node = self._DoublyNode(elemento, this, successor)
            this._next = new_node
            successor._prev = new_node
        self._length += 1

    def remove(self, elemento):
        if not self.empty():
            node = self._header._next
            pos = 0
            found = False
            while not found and pos < self._length:
                if node._elem == elemento:
                    found = True
                else:
                    node = node._next
                    pos += 1
            if found:
                node._prev._next = node._next
                node._next._prev = node._prev
                self._length -= 1

    def count(self, elem):
        result = 0
        this = self._header._next
        if self._length > 0:
            while this._next is not None:  # aqui a lista Ã© percorrida
                if this._elem == elem:
                    result += 1
                this = this._next
        return result

    def clear(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def index(self, elem):
        result = None  # armazena a primeira posiÃ§Ã£o do elemento
        found = False
        pos = 0
        aux = self._header._next
        # Vamos percorrer a lista em busca de elem
        while not found and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if aux._elem is elem:
                found = True
                result = pos
            aux = aux._next
            pos += 1
        return result  # se o elemento nÃ£o estiver na lista, retorna None

    def length(self):
        return self._length

    def empty(self):
        return self._length == 0

    def remove_at(self, indice):
        if not self.empty():
            node = self._header._next
            pos = 0
            found = False
            while not found and pos < self._length:
                if pos == indice:
                    found = True
                else:
                    node = node._next
                    pos += 1
            if found:
                node._prev._next = node._next
                node._next._prev = node._prev
                self._length -= 1

    def element_at(self, indice):
        result = None  # armazena a primeira posiÃ§Ã£o do elemento
        found = False
        pos = 0
        aux = self._header._next
        # Vamos percorrer a lista em busca de elem
        while not found and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if pos == indice:
                found = True
                result = aux._elem
            aux = aux._next
            pos += 1
        return result  # se o elemento nÃ£o estiver na lista, retorna None

    def replace_at(self, indice, elemento):
        found = False
        pos = 0
        aux = self._header._next
        # Vamos percorrer a lista em busca de elem
        while not found and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if pos == indice:
                found = True
                aux._elem = elemento
            aux = aux._next
            pos += 1
