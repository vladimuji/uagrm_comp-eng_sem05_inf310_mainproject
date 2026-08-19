from bin_tree.binary_tree import BinaryTree
from exercices.tic_tac_toe import Tree

tree = BinaryTree()

# # Create the root
# root = tree.create_node(10)

# # Add children
# root.left_child = tree.create_node(5)
# root.right_child = tree.create_node(15)

# # Assign root to the tree
# tree.root = root

# # Basic tests
# print("Tree empty:", tree.is_empty_tree())
# print("Root:", tree.root.data)
# print("Left child:", tree.root.left_child.data)
# print("Right child:", tree.root.right_child.data)
# print("Is root a leaf?", tree.is_leaf(root))
# print("Is left node a leaf?", tree.is_leaf(root.left_child))

#############################################

# tree = Tree()

# # Place a move directly
# tree.root.set_cell(1, 1, "X")
# print("Board:")
# tree.print_tree()

# # Expand into possible next moves
# tree.expand(tree.root, "O")
# print(f"\n{len(tree.root.children)} children generated:")
# tree.print_children(tree.root)

###############################################

# test_binary_tree.py

tree = BinaryTree()

values = [6, 2, 11, 3, 9, 30, 13, 18, 10, 5, 15, 4, 7, 20, 12, 25]

for v in values:
    tree.insert(v)

tree.print_tree_recursive()

print("Pre-order (recursive): ", tree.pre_order())
print("Pre-order (iterative): ", tree._pre_order_iter())

print("In-order (recursive):  ", tree.in_order())
print("In-order (iterative):  ", tree._in_order_iter())

print("Post-order (recursive):", tree.post_order())
print("Post-order (iterative):", tree._post_order_iter())

print("has(9):  ", tree.has(9))
print("has(99): ", tree.has(99))
print("search(9):", tree.search(9))
print("is_empty_tree():", tree.is_empty_tree())
print("is_leaf(root):", tree.is_leaf(tree.root))