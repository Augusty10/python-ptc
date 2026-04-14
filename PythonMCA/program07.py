
print("Name - Swati Yadav ")
print("Class - MCA 2 nd ")
print("Role No. - 56")

year = int(input(" Happy new Year : "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print(" not leap year ")
