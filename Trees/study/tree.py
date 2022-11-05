from abc import ABC, abstractmethod


class Tree(ABC):

    class Position(ABC):
        def element(self):
            """Return the element stored at this Position."""
            pass

        def __eq__(self, other):
            """Return True if other Position represents the same Position."""
            pass

        def __ne__(self, other):
            """Return True if other does not represet the same Position."""
            pass

    @abstractmethod
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        pass

    @abstractmethod
    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        pass

    @abstractmethod
    def num_children(self, p):
        """Return the number of children that Position p has."""
        pass

    @abstractmethod
    def children(self, p):
        """Generate an interation of Positions representing p's children."""
        pass

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree."""
        pass

    def is_root(self, p):
        """Return True if p represents the root of the tree."""
        pass

    def is_leaf(self, p):
        """Return True if p dos not have any children."""
        pass

    def is_empty(self):
        """Return True if tree is empty."""
        pass
