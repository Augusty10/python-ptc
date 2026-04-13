name = input("Enter a string: ")

# Forward
for ch in name:
    print(ch, end=" ")

print()

# Backward
for i in range(len(name) - 1, -1, -1):
    print(name[i], end=" ")