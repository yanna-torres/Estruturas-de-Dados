
from list_adt import ListADT


class CircularList(ListADT):

    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def insert(self, indice, elemento):
        self._data.insert(indice, elemento)

    def remove(self, elemento):
        self._data.remove(elemento)

    def remove_at(self, indice):
        pos = indice % len(self._data)
        self._data.pop(pos)

    def count(self, elemento):
        return self._data.count(elemento)

    def clear(self):
        self._data = list()

    def index(self, elemento):
        return self._data.index(elemento)

    def length(self):
        return len(self._data)

    def element_at(self, indice):
        pos = indice % len(self._data)
        return self._data[pos]

    def replace_at(self, indice, elemento):
        pos = indice % len(self._data)
        self._data[pos] = elemento
