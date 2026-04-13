students = {
    "Ram": 85,
    "Shyam": 92,
    "Aman": 78,
    "Riya": 95
}

print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

topper = max(students, key=students.get)

print("Topper:", topper)
print("Marks:", students[topper])