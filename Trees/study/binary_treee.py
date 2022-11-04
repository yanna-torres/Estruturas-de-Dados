
class EmptyStructure(Exception):
    pass


class BinaryTree:

    class _Node:
        def __init__(self, data=None, parent=None, left=None, right=None):
            self._data = data
            self._parent = parent
            self._left = left
            self._right = right

        def get_data(self):
            return self._data

        def get_left(self):
            return self._left

        def get_right(self):
            return self._right

        def set_data(self, value):
            self._data = value

        def set_left(self, value):
            self._left = value

        def set_right(self, value):
            self._right = value

    def __init__(self, root=None, parent=None):
        self._root = self._Node(root, parent)

    def insert(self, value):
        """Inserts a new value on the tree. If the tree is empty, this value goes on the root,
        if the value is smaller, goes to the left and if is bigger goes to the right."""
        if self._root.get_data() is None:
            self._root.set_data(value)
        elif value <= self._root.get_data():
            if self._root.get_left() is None:
                self._root.set_left(BinaryTree(value, self._root))
            else:
                self._root.get_left().insert(value)
        else:
            if self._root.get_right() is None:
                self._root.set_right(BinaryTree(value, self._root))
            else:
                self._root.get_right().insert(value)

    def in_order(self):
        """Returns all tree values in a list format, following the order: left, root, right."""
        result = []
        if self._root.get_data() is not None:
            if self._root.get_left() is not None:
                result = self._root.get_left().in_order()
            result.append(self._root.get_data())
            if self._root.get_right() is not None:
                result = result + self._root.get_right().in_order()
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def pre_order(self):
        """Returns all tree values in a list format, following the order: root, left, right."""
        result = []
        if self._root.get_data() is not None:
            result.append(self._root.get_data())
            if self._root.get_left() is not None:
                result = result + self._root.get_left().pre_order()
            if self._root.get_right() is not None:
                result = result + self._root.get_right().pre_order()
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def post_order(self):
        """Returns all tree values in a list format, following the order: left, right, root."""
        result = []
        if self._root.get_data() is not None:
            if self._root.get_left() is not None:
                result = result + self._root.get_left().post_order()
            if self._root.get_right() is not None:
                result = result + self._root.get_right().post_order()
            result.append(self._root.get_data())
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def remove(self, value):
        pass

    def search(self, value):
        pass

    def is_sibling(self, value1, value2):
        if self._root.get_data() is None:
            raise EmptyStructure("The tree is empty")
        else:
            pass

    def is_cousin(self, value1, value2):
        if self._root.get_data() is None:
            raise EmptyStructure("The tree is empty")
        else:
            pass

    def left(self, parent):
        """Returns"""
        pass


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
