while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exiting...")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")