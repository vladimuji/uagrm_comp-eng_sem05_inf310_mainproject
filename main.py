from bin_tree.BinaryTree import BinaryTree

tree = BinaryTree()

# Create the root
root = tree.create_node(10)

# Add children
root.left_child = tree.create_node(5)
root.right_child = tree.create_node(15)

# Assign root to the tree
tree.root = root

# Basic tests
print("Tree empty:", tree.is_empty_tree())
print("Root:", tree.root.data)
print("Left child:", tree.root.left_child.data)
print("Right child:", tree.root.right_child.data)
print("Is root a leaf?", tree.is_leaf(root))
print("Is left node a leaf?", tree.is_leaf(root.left_child))