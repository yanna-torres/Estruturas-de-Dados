"""
Esta semana vocês vão implementar a classe Binary Tree. A classe deve conter o método insert (que está descrito nos
slides), mas também os métodos: inOrderTraverse, preOrderTraverse e postOrderTraverse.

Como saída de cada um destes métodos eu espero uma lista contendo todos os elementos da árvore em diferentes ordens de
acordo com o método escolhido.

Utilizem a lista implementada por vocês ou o tipo list do próprio Python.
"""


class EmptyStructure(Exception):
    pass


class BinaryNode:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def __repr__(self):
        return str(self._data)

    def __eq__(self, other):
        if isinstance(other, BinaryNode):
            if self.data() == other.data():
                return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        if isinstance(other, BinaryNode):
            return self.data() <= other.data()
        else:
            return False

    def data(self):
        """Returns the value of the main element in the node"""
        return self._data

    def left(self):
        """Returns the value of the left child"""
        return self._left

    def right(self):
        """Returns the value of the right child"""
        return self._right

    def parent(self):
        """Returns the value of the parent of the Node"""
        return self._parent

    def set_data(self, value):
        """Set the value of the main element in the node"""
        self._data = value

    def set_left(self, value):
        """Set the value of the left child"""
        self._left = value

    def set_right(self, value):
        """Set the value of the right child"""
        self._right = value

    def set_parent(self, value):
        """Set the value of the parent"""
        self._parent = value


class BinaryTree:

    def __init__(self, data=None):
        self._root = BinaryNode(data)

    def root(self):
        return self._root

    def empty(self):
        return self._root.data() is None

    def insert(self, value, root=None):
        """Inserts a new value on the tree. If the tree is empty, this value goes on the root,
        if the value is smaller, goes to the left and if is bigger goes to the right."""
        if root is None:
            root = self._root

        if root.data() is None:
            root.set_data(value)
        elif value <= root.data():
            if root.left() is None:
                root.set_left(BinaryNode(value, root))
            else:
                self.insert(value, root.left())
        else:
            if root.right() is None:
                root.set_right(BinaryNode(value, root))
            else:
                self.insert(value, root.right())

    def in_order(self, root=None):
        """Returns all tree values in a list format, following the order: left, root, right."""
        result = []
        if root is None:
            root = self._root

        if root.data() is not None:
            if root.left() is not None:
                result = self.in_order(root.left())
            result.append(root)
            if root.right() is not None:
                result = result + self.in_order(root.right())
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def pre_order(self, root=None):
        """Returns all tree values in a list format, following the order: root, left, right."""
        result = []
        if root is None:
            root = self._root

        if root.data() is not None:
            result.append(root)
            if root.left() is not None:
                result = result + self.pre_order(root.left())
            if root.right() is not None:
                result = result + self.pre_order(root.right())
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def post_order(self, root=None):
        """Returns all tree values in a list format, following the order: left, right, root."""
        result = []
        if root is None:
            root = self._root

        if root.data() is not None:
            if root.left() is not None:
                result = result + self.post_order(root.left())
            if root.right() is not None:
                result = result + self.post_order(root.right())
            result.append(root)
        else:
            raise EmptyStructure("The tree is empty")
        return result


if __name__ == "__main__":
    bt = BinaryTree(5)
    bt.insert(2)
    bt.insert(6)
    bt.insert(1)
    bt.insert(5)
    bt.insert(-1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(6)
    bt.insert(7)
    bt.insert(8)
    print("")
    print("in order traverse")
    print(bt.in_order())
    print("")
    print("pre order traverse")
    print(bt.pre_order())
    print("")
    print("post order traverse")
    print(bt.post_order())
