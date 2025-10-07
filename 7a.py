class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, current_node, key):
        if current_node.left is None:
            current_node.left = Node(key)
        else:
            new_node = Node(key)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, key):
        if current_node.right is None:
            current_node.right = Node(key)
        else:
            new_node = Node(key)
            new_node.right = current_node.right
            current_node.right = new_node

    # Inorder Traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Preorder Traversal
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")


# Main Program
if __name__ == "__main__":
    # Create tree with root
    tree = BinaryTree('A')

    # Insert nodes (same as manual diagram)
    tree.insert_left(tree.root, 'B')
    tree.insert_right(tree.root, 'C')
    tree.insert_left(tree.root.left, 'D')
    tree.insert_right(tree.root.left, 'E')
    tree.insert_left(tree.root.right, 'F')

    print("Inorder Traversal:")
    tree.inorder(tree.root)

    print("\nPreorder Traversal:")
    tree.preorder(tree.root)

    print("\nPostorder Traversal:")
    tree.postorder(tree.root)
