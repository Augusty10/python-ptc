str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 < str2:
    print(str1, "comes first alphabetically")
elif str1 > str2:
    print(str2, "comes first alphabetically")
else:
    print("Both strings are equal")