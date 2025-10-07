SIZE = 5  
queue = [None] * SIZE
front = -1
rear = -1
def enqueue(car):
    global rear, queue
    if rear == SIZE - 1:
        print("Queue is FULL!!! Insertion is not possible!!!")
    else:
        rear += 1
        queue[rear] = car
        print(f"Car '{car}' parked successfully.")
def dequeue():
    global front, rear, queue
    if front == rear:
        print("Queue is EMPTY!!! No cars to remove.")
    else:
        front += 1
        removed_car = queue[front]
        print(f"Car '{removed_car}' has left the parking.")
        queue[front] = None
        if front == rear:
            front = -1
            rear = -1
def isEmpty():
    return front == rear
def size():
    return rear - front
def show():
    if isEmpty():
        print("Queue is EMPTY!!!")
    else:
        print("Cars currently in the parking lot:")
        for i in range(front + 1, rear + 1):
            print(f"{i - front}: {queue[i]}")
def menu():
    while True:
        print("\n--- Car Parking Queue Management ---")
        print("1. Park a Car (Enqueue)")
        print("2. Remove a Car (Dequeue)")
        print("3. Is Parking Empty?")
        print("4. Total Cars Parked")
        print("5. Show All Cars")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            car = input("Enter car number to park: ")
            enqueue(car)
        elif choice == '2':
            dequeue()
        elif choice == '3':
            print("Parking is Empty." if isEmpty() else "Parking has cars.")
        elif choice == '4':
            print(f"Total cars parked: {size()}")
        elif choice == '5':
            show()
        elif choice == '6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
menu()
