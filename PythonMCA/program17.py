name = input("Enter a string: ")

# Forward
i = 0
while i < len(name):
    print(name[i], end=" ")
    i += 1

print()

# Backward
i = len(name) - 1
while i >= 0:
    print(name[i], end=" ")
    i -= 1
    