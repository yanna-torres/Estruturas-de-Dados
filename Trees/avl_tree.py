
class EmptyStructure(Exception):
    pass


class NotFound(Exception):
    pass


class BinaryNode:

    def __init__(self, data, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right
        self._height = 1
        self._bf = 0

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

    def height(self):
        return self._height

    def set_data(self, value):
        """Set the value of the main element in the node"""
        self._data = value

    def set_left(self, value):
        """Set the value of the left child"""
        self._left = value

    def set_right(self, value):
        """Set the value of the right child"""
        self._right = value

    def set_height(self, new_height):
        self._height = new_height
    #
    # def get_node(self):
    #     """Returns a dictionary with the all the elements in the node"""
    #     return {"value": self, "parent": self.parent(),
    #             "left child": self.left(), "right child": self.right()}


class AVLTree:

    def __init__(self, root=None):
        self._root = BinaryNode(root)

    def root(self):
        return self._root

    def empty(self):
        return self.root().data() is None

    def insert(self, value):
        """Inserts a new value on the tree. If the tree is empty, this value goes on the root,
        if the value is smaller, goes to the left and if is bigger goes to the right."""
        new_node = BinaryNode(value)
        return self._insert(value, self.root(), new_node)

    def in_order(self):
        """Returns all tree values in a list format, following the order: left, root, right."""
        return self._in_order(self.root())

    def pre_order(self):
        """Returns all tree values in a list format, following the order: root, left, right."""
        return self._pre_order(self.root())

    def post_order(self):
        """Returns all tree values in a list format, following the order: left, right, root."""
        return self._post_order(self.root())

    def search(self, value):
        """Returns if a value is or not on the tree"""
        return self._search(value, self.root())

    def remove(self, value):
        b = self.search(value)
        if b[0] is False:
            raise NotFound("The value is not on the tree")
        return self._remove(b[1])

    def min(self):
        """Returns the minimum value within the tree"""
        return self._min(self.root())

    def max(self):
        """Returns the maximum value within the tree"""
        return self._max(self.root())

    def _insert(self, value, root, node):
        if root.data is None:
            root.set_data(value)
        elif node <= root:
            if root.left() is None:
                root.set_left(BinaryNode(value, root))
            else:
                self._insert(value, root.left(), node)
        else:
            if root.right() is None:
                root.set_right(BinaryNode(value, root))
            else:
                self._insert(value, root.right(), node)

    def _in_order(self, root):
        result = []

        if root.data() is not None:
            if root.left() is not None:
                result = self._in_order(root.left())
            result.append(root.data())
            if root.right() is not None:
                result = result + self._in_order(root.right())
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def _pre_order(self, root):
        result = []

        if root.data() is not None:
            result.append(root.data())
            if root.left() is not None:
                result = result + self._pre_order(root.left())
            if root.right() is not None:
                result = result + self._pre_order(root.right())
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def _post_order(self, root):
        """Returns all tree values in a list format, following the order: left, right, root."""
        result = []

        if root.data() is not None:
            if root.left() is not None:
                result = result + self._post_order(root.left())
            if root.right() is not None:
                result = result + self._post_order(root.right())
            result.append(root)
        else:
            raise EmptyStructure("The tree is empty")
        return result

    def _search(self, value, root):
        """Returns if a value is or not on the tree"""

        if value == root.data():
            return True, root
        elif value < root.data() and root.left() is not None:
            return self._search(value, root.left())
        elif value > root.data() and root.right() is not None:
            return self._search(value, root.right())
        else:
            return False, f"The value {value} is not on the tree"

    def _remove(self, node):
        if node.left() is None and node.right() is None:
            node = None
        else:
            pass

    def _min(self, root):
        if root.left() is None:
            return root
        else:
            return self._min(root.left())

    def _max(self, root):
        if root.right() is None:
            return root
        else:
            return self._max(root.right())


if __name__ == "__main__":
    bt = AVLTree(5)
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
    print(bt.search(5))
    print(bt.min())
    print(bt.max())
    print(bt.root().height())
