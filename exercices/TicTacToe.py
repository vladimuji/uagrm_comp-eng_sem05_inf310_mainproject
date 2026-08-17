"""
Module: tic_tac_toe.py
Subject: INF310 - Data Structures II
Description: Node and Tree classes supporting a 3x3 matrix data
             structure for representing a Tic-Tac-Toe game. Each Node
             holds one board state; its children are the possible next
             board states after placing one mark on an empty cell.
             Not a binary tree: a node may have up to 9 children.

Author: Vladimir
"""

import copy


class Node:
    """Represents one Tic-Tac-Toe board state (a 3x3 matrix) and its
    possible next states (children)."""

    def __init__(self, matrix=None):
        self._matrix = matrix if matrix is not None else Node.empty_matrix()
        self._children = []

    @staticmethod
    def empty_matrix():
        """Return a fresh empty 3x3 board (all cells set to None)."""
        return [[None for _ in range(3)] for _ in range(3)]

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children

    # ------------------------------------------------------------------
    # Cell-level access
    # ------------------------------------------------------------------
    def get_cell(self, row, column):
        return self._matrix[row][column]

    def set_cell(self, row, column, value):
        self._matrix[row][column] = value

    # ------------------------------------------------------------------
    # Tree-building
    # ------------------------------------------------------------------
    def generate_children(self, mark):
        """Create one child Node per empty cell, placing 'mark' ('X' or
        'O') there. Each child gets its own independent copy of the
        board, so modifying one child never affects another."""
        self._children = []
        for row in range(3):
            for column in range(3):
                if self._matrix[row][column] is None:
                    child_matrix = copy.deepcopy(self._matrix)
                    child_matrix[row][column] = mark
                    self._children.append(Node(child_matrix))
        return self._children

    def is_leaf(self):
        return len(self._children) == 0

    def __str__(self):
        rows = [" | ".join(cell or " " for cell in row) for row in self._matrix]
        return "\n---------\n".join(rows)


class Tree:
    """Wraps a root Node and lets you expand it into a tree of possible
    next moves."""

    def __init__(self):
        self._root = Node()

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node

    # ------------------------------------------------------------------
    # Operations
    # ------------------------------------------------------------------
    def reset_board(self):
        self._root = Node()

    def expand(self, node, mark):
        """Generate the children (possible next moves) of a given node."""
        return node.generate_children(mark)

    def print_tree(self):
        print(self._root)

    def print_children(self, node):
        """Print every child board of a given node, one after another."""
        for index, child in enumerate(node.children):
            print(f"--- Option {index + 1} ---")
            print(child)


if __name__ == "__main__":
    tree = Tree()

    # Play a couple of moves directly on the root board.
    tree.root.set_cell(1, 1, "X")
    print("Current board:")
    tree.print_tree()

    # Expand the root: every empty cell becomes a possible O move.
    tree.expand(tree.root, "O")
    print(f"\nGenerated {len(tree.root.children)} possible next moves for O:")
    tree.print_children(tree.root)