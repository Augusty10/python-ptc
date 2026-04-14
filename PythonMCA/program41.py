
print("Name - Swati Yadav ")
print("Class - MCA 2 nd ")
print("Role No. - 56")

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# Passing multiple values
add_numbers(10, 20, 30)
