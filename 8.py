class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, root, name, time, purpose):
        if root is None:
            return Node(name, time, purpose)
        if name < root.name:
            root.left = self.insert(root.left, name, time, purpose)
        else:
            root.right = self.insert(root.right, name, time, purpose)
        return root
    def search(self, root, name):
        if root is None or root.name == name:
            return root
        if name < root.name:
            return self.search(root.left, name)
        return self.search(root.right, name)
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def delete(self, root, name):
        if root is None:
            return root
        if name < root.name:
            root.left = self.delete(root.left, name)
        elif name > root.name:
            root.right = self.delete(root.right, name)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.name, root.time, root.purpose = temp.name, temp.time, temp.purpose
            root.right = self.delete(root.right, temp.name)
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.name, root.time, root.purpose)
            self.inorder(root.right)
    def preorder(self, root):
        if root:
            print(root.name, root.time, root.purpose)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.name, root.time, root.purpose)
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
tree = BST()
root = None
root = tree.insert(root, "Alice", "10:00", "Meeting")
root = tree.insert(root, "Bob", "10:30", "Project Discussion")
root = tree.insert(root, "Charlie", "11:00", "Interview")
print("\nInorder Traversal (Sorted by Name):")
tree.inorder(root)
print("\nSearch for Bob:")
node = tree.search(root, "Bob")
if node:
    print(f"Found: {node.name}, {node.time}, {node.purpose}")
else:
    print("Not Found")
print("\nDeleting Bob...")
root = tree.delete(root, "Bob")
print("\nInorder after Deletion:")
tree.inorder(root)
print("\nTotal Entries:", tree.countNodes(root))

