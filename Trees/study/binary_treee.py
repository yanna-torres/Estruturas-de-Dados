
class EmptyStructure(Exception):
    pass


class BinaryTree:

    class _Node:
        def __init__(self, data=None, parent=None, left=None, right=None):
            self._data = data
            self._parent = parent
            self._left = left
            self._right = right

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

        def get_node(self):
            return {"value": self.data(), "parent": self.parent().data() if self.parent() is not None else None,
                    "left child": self.left().data() if self.left() is not None else None,
                    "right child": self.right().data() if self.right() is not None else None}

    def __init__(self, root=None):
        self._root = self._Node(root)

    def insert(self, value, root=None):
        """Inserts a new value on the tree. If the tree is empty, this value goes on the root,
        if the value is smaller, goes to the left and if is bigger goes to the right."""
        if root is None:
            root = self._root

        if root.data() is None:
            root.set_data(value)
        elif value <= root.data():
            if root.left() is None:
                root.set_left(self._Node(value, root))
            else:
                self.insert(value, root.left())
        else:
            if root.right() is None:
                root.set_right(self._Node(value, root))
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
            result.append(root.data())
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
            result.append(root.data())
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
            result.append(root.data())
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def remove(self, value, root=None):
        if root is None:
            root = self._root

        if value < root.data():
            return self.remove(value, root.left())
        elif value > root.data():
            return self.remove(value, root.right())
        else:
            pass

    def search(self, value, root=None):
        """Returns if a value is or not on the tree"""
        if root is None:
            root = self._root

        if value == root.data():
            return True, root.get_node()
        elif value < root.data() and root.left() is not None:
            return self.search(value, root.left())
        elif value > root.data() and root.right() is not None:
            return self.search(value, root.right())
        else:
            return False


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
    print("")
    print("search")
    print(bt.search(7))
