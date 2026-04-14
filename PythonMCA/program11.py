


print("Name - Swati Yadav ")
print("Class - MCA 2 nd ")
print("Role No. - 56")

name=input("Enter your name : ")
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5

average = total / 5

percentage = (total / 500) * 100

if percentage>60:
    print("Grade A")
elif percentage>40:
    print("Grade B")
else:
    print(" fail ")


print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
print("Student Name : " ,name)
