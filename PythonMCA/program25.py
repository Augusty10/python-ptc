print("Name - Swati Yadav ")
print("Class - MCA 2 nd ")
print("Role No. - 56")

s = input("Enter a string: ")
count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)
