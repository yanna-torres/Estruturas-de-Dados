
from list_adt import ListADT


class MyList(ListADT):

    def __init__(self):
        self._data = list()

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def insert(self, indice, elemento):
        self._data.insert(indice, elemento)

    def remove(self, elemento):
        self._data.remove(elemento)

    def count(self, elemento):
        return self._data.count(elemento)

    def clear(self):
        self._data = list()

    def index(self, elemento):
        return self._data.index(elemento)

    def length(self):
        return len(self._data)

    def remove_at(self, indice):
        self._data.pop(indice)

    def element_at(self, indice):
        return self._data[indice]

    def replace(self, indice, elemento):
        self._data[indice] = elemento
