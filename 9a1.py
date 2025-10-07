
class Student:
    def __init__(self, enrollment_id, name, course):
        self.enrollment_id = enrollment_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"[ID: {self.enrollment_id}, Name: {self.name}, Course: {self.course}]"

class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def get_height(self, root):
        return 0 if not root else root.height
    def get_balance(self, root):
        return 0 if not root else self.get_height(root.left) - self.get_height(root.right)   
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    def insert(self, root, student):
        if not root:
            return Node(student)
        elif student.enrollment_id < root.student.enrollment_id:
            root.left = self.insert(root.left, student)
        elif student.enrollment_id > root.student.enrollment_id:
            root.right = self.insert(root.right, student)
        else:
            print("Duplicate Enrollment ID not allowed!")
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        if balance > 1 and student.enrollment_id < root.left.student.enrollment_id:
            return self.rotate_right(root)
        if balance < -1 and student.enrollment_id > root.right.student.enrollment_id:
            return self.rotate_left(root)
        if balance > 1 and student.enrollment_id > root.left.student.enrollment_id:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and student.enrollment_id < root.right.student.enrollment_id:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)
    def delete(self, root, enrollment_id):
        if not root:
            print("Record not found!")
            return root
        if enrollment_id < root.student.enrollment_id:
            root.left = self.delete(root.left, enrollment_id)
        elif enrollment_id > root.student.enrollment_id:
            root.right = self.delete(root.right, enrollment_id)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.student = temp.student
            root.right = self.delete(root.right, temp.student.enrollment_id)
        if not root:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root
   
    def search(self, root, key):
        if not root:
            return None
        if key == root.student.enrollment_id:
            return root.student
        elif key < root.student.enrollment_id:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.student)
            self.inorder(root.right)
    def count_nodes(self, root):
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
if __name__ == "__main__":
    tree = AVLTree()
    root = None
    while True:
        print("\n===== STUDENT ENROLLMENT SYSTEM (AVL TREE) =====")
        print("a) Insert an enrollment record")
        print("b) Delete a record by enrollment ID")
        print("c) Search for a student enrollment")
        print("d) Traverse all enrollment records (Inorder)")
        print("e) Count total enrollments")
        print("f) Exit")
        choice = input("Enter your choice: ").lower()
        if choice == 'a':
            eid = int(input("Enter Enrollment ID: "))
            name = input("Enter Student Name: ")
            course = input("Enter Course: ")
            student = Student(eid, name, course)
            root = tree.insert(root, student)
            print("✅ Student added successfully!")
        elif choice == 'b':
            eid = int(input("Enter Enrollment ID to delete: "))
            root = tree.delete(root, eid)
            print("✅ Record deleted (if it existed).")
        elif choice == 'c':
            eid = int(input("Enter Enrollment ID to search: "))
            student = tree.search(root, eid)
            print(student if student else "❌ Student not found!")
        elif choice == 'd':
            print("\n📋 All Enrollment Records (Sorted by ID):")
            tree.inorder(root)
        elif choice == 'e':
            total = tree.count_nodes(root)
            print(f"📊 Total Enrollments: {total}")
        elif choice == 'f':
            print("👋 Exiting... Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
