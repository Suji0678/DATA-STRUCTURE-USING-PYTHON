class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
class BookStack:
    def __init__(self):
        self.top = None 
    def push(self, book_title):
        new_node = Node(book_title)
        if self.top is None: 
            new_node.next = None 
        else:
            new_node.next = self.top
        self.top = new_node 
        print(f'"{book_title}" added to the stack.')
    def pop(self):
        if self.top is None: 
            print("Stack is empty! Cannot pop.")
        else:
            temp = self.top 
            self.top = self.top.next 
            print(f'"{temp.data}" removed from the stack.')
            del temp 
    def peek(self):
        if self.top is None:
            print("Stack is empty. No top book to display.")
        else:
            print(f'Top book in stack: "{self.top.data}"')
    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            temp = self.top
            print("Books in the stack (Top to Bottom):")
            while temp:
                print(f' {temp.data} --->', end="")
                temp = temp.next
            print(" NULL")
if __name__ == "__main__":
    book_stack = BookStack()
    while True:
        print("\n--- Stack Operations (Linked List) ---")
        print("1. Push (Add Book)")
        print("2. Pop (Remove Book)")
        print("3. Peek (View Top Book)")
        print("4. Display Stack")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            book = input("Enter book title to add: ")
            book_stack.push(book)
        elif choice == '2':
            book_stack.pop()
        elif choice == '3':
            book_stack.peek()
        elif choice == '4':
            book_stack.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
