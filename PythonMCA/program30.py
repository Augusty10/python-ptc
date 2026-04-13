roll_numbers = [101, 102, 103, 104, 105]

num = int(input("Enter roll number to search: "))

if num in roll_numbers:
    print("Roll number exists")
else:
    print("Roll number not found")