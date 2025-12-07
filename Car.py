class CarWashStack:
    def __init__(self, capacity):
        self.stack = []          # will store car numbers / IDs
        self.capacity = capacity

    def is_full(self):
        return len(self.stack) == self.capacity

    def is_empty(self):
        return len(self.stack) == 0

    def arrive(self, car_number):
        if self.is_full():
            print(f"Car {car_number} cannot enter. Car wash line is FULL!")
        else:
            self.stack.append(car_number)
            print(f"Car {car_number} has entered the car wash line.")

    def wash_car(self):
        if self.is_empty():
            print("No cars to wash. Line is EMPTY!")
        else:
            car = self.stack.pop()
            print(f"Car {car} is being washed and leaving the car wash.")

    def show_line(self):
        if self.is_empty():
            print("Car wash line is empty.")
        else:
            print("Current car wash line (bottom --> top):")
            print(" | ".join(str(c) for c in self.stack))


def main():
    print("=== CAR WASH SIMULATION (STACK) ===")
    capacity = int(input("Enter maximum number of cars in car wash line: "))

    car_wash = CarWashStack(capacity)

    while True:
        print("\nMenu:")
        print("1. Car arrives")
        print("2. Wash next car (pop)")
        print("3. Show current line")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            car_number = input("Enter car number/ID: ")
            car_wash.arrive(car_number)

        elif choice == "2":
            car_wash.wash_car()

        elif choice == "3":
            car_wash.show_line()

        elif choice == "4":
            print("Exiting simulation. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
