
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

    def __eq__(self, comp):
        if self.data() == comp:
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


class BarCodeNumberTree:

    def __init__(self):
        self._root = BinaryNode(0)
        self._root.set_left(BinaryNode(0, self._root))
        self._root.set_right(BinaryNode(1, self._root))
        self._left_tree()
        self._right_tree()

    def _left_tree(self):
        left = self._root.left()
        left.set_left(BinaryNode(0, left))
        left.set_right(BinaryNode(1, left))

        left = left.left()
        left.set_right(BinaryNode(1, left))

        right = left.right()
        right.set_left(BinaryNode(0, right))
        right.set_right(BinaryNode(1, right))

        left = right.left()
        left.set_right(BinaryNode(1, left))
        left.right().set_left(BinaryNode(9, left.right()))

        right = right.right()
        right.set_left(BinaryNode(0, right))
        right.left().set_left(BinaryNode(0, right.left()))

        right = self._root.left().right()
        right.set_right(BinaryNode(1, right))
        right.set_left(BinaryNode(0, right))

        left = right.left()
        left.set_left(BinaryNode(0, left))
        left = left.left()
        left.set_right(BinaryNode(1, left))
        left.right().set_left(BinaryNode(2, left.right()))

        right = right.right()
        right.set_left(BinaryNode(0))
        left = right.left()
        left.set_left(BinaryNode(0))
        left.left().set_left(BinaryNode(1, left.left()))

    def _right_tree(self):
        right_main = self._root.right()
        right_main.set_left(BinaryNode(0, right_main))
        right_main.set_right(BinaryNode(1, right_main))

        left = right_main.left()
        left.set_left(BinaryNode(0, left))
        left.set_right(BinaryNode(1, left))

        right = left.right()
        right.set_right(BinaryNode(1, right))
        right = right.right()
        right.set_right(BinaryNode(1, right))
        right.right().set_left(BinaryNode(6, right.right()))

        left = left.left()
        left.set_left(BinaryNode(0, left))
        left.left().set_right(BinaryNode(1, left.left()))
        left.left().right().set_left(BinaryNode(4, left.left().right()))

        right = right_main.right()
        right.set_left(BinaryNode(0, right))
        right.set_right(BinaryNode(1, right))

        left = right.left()
        left.set_left(BinaryNode(0, left))
        left.left().set_left(BinaryNode(0, left.left()))
        left.left().left().set_left(BinaryNode(5, left.left().left()))
        left.set_right(BinaryNode(1, left))
        left.right().set_right(BinaryNode(1, left.right()))
        left.right().right().set_left(BinaryNode(8, left.right().right()))

        right = right.right()
        right.set_left(BinaryNode(0, right))
        right.left().set_right(BinaryNode(1, right.left()))
        right.left().right().set_left(BinaryNode(7, right.left().right()))
        right.set_right(BinaryNode(1))
        right.right().set_left(BinaryNode(0))
        right.right().left().set_left(BinaryNode(3, right.right().left()))

    def inoder_tree(self, root=None):
        """Returns all tree values in a list format, following the order: left, root, right."""
        if self.empty():
            raise EmptyStructure("The tree is empty")

        result = []
        if root is None:
            root = self._root

        if root.left() is not None:
            result = self.inoder_tree(root.left())
        result.append(root)
        if root.right() is not None:
            result = result + self.inoder_tree(root.right())

        return result

    def empty(self):
        return self._root is None

    def search_num(self, numero):
        num = str(numero)
        return self._search(num, self._root)

    def _search(self, num, root):
        if len(num) <= 2:
            return root.left()
        elif root.left() == int(num[1]):
            return self._search(num[1:], root.left())
        else:
            return self._search(num[1:], root.right())


if __name__ == "__main__":
    bc = BarCodeNumberTree()
    print(bc.inoder_tree())
    print(bc.search_num("0111101"))
