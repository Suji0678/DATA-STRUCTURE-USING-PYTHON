class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  
            self.front = self.rear = new_node
            print(f"Car '{value}' has entered the parking lot.")
        else:
            self.rear.next = new_node
            self.rear = new_node
            print(f"Car '{value}' has entered the parking lot.")
    def dequeue(self):
        if self.is_empty():
            print("Parking lot is empty. No car to exit.")
            return
        removed_car = self.front.data
        self.front = self.front.next
        if self.front is None:  
            self.rear = None
        print(f"Car '{removed_car}' has exited the parking lot.")
    def display(self):
        if self.is_empty():
            print("Parking lot is empty!")
            return
        temp = self.front
        print("Cars currently in the parking lot:")
        while temp:
            print(f"{temp.data} ---> ", end="")
            temp = temp.next
        print("NULL")
def main():
    parking_queue = Queue()
    while True:
        print("\n--- Car Parking Management System ---")
        print("1. Car Enters (Enqueue)")
        print("2. Car Exits (Dequeue)")
        print("3. Display Cars in Parking Lot")
        print("4. Exit Program")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            car_number = input("Enter car number to park: ")
            parking_queue.enqueue(car_number)
        elif choice == '2':
            parking_queue.dequeue()
        elif choice == '3':
            parking_queue.display()
        elif choice == '4':
            print("Exiting Car Parking Management System.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
