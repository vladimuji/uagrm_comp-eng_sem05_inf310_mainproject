"""
Module: binary_tree.py
Subject: INF310 - Data Structures II
Description: Basic Binary Tree structure, with its node class and
             properties (getters/setters), following PEP8 standards.

Author: Vladimir
"""


class BinaryNode:
    """Represents a node inside a Binary Tree."""

    def __init__(self, data):
        self._data = data
        self._left_child = None
        self._right_child = None

    # ------------------------------------------------------------------
    # Properties (Pythonic getters and setters)
    # ------------------------------------------------------------------
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, node):
        self._left_child = node

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, node):
        self._right_child = node

    def __str__(self):
        return str(self._data)


class BinaryTree:
    """Basic Binary Tree structure (no insertion order enforced)."""

    def __init__(self):
        self._root = None
        self._empty_node = None

    # ------------------------------------------------------------------
    # Properties (Pythonic getters and setters)
    # ------------------------------------------------------------------
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node

    @property
    def empty_node(self):
        return self._empty_node

    # ------------------------------------------------------------------
    # Support methods (used by subclasses)
    # ------------------------------------------------------------------
    def is_empty_node(self, node):
        """Return True if the given node is the empty node (None)."""
        return node is self._empty_node

    def is_empty_tree(self):
        """Return True if the tree has no root."""
        return self._root is None

    def create_node(self, data):
        """Create and return a new BinaryNode with the given data."""
        return BinaryNode(data)

    def is_leaf(self, node):
        """Return True if the node has no children (left nor right)."""
        return (
            self.is_empty_node(node.left_child)
            and self.is_empty_node(node.right_child)
        )