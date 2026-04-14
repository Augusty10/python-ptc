
print("Name - Swati Yadav ")
print("Class - MCA 2 nd ")
print("Role No. - 56")

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Passing key-value pairs
student_info(name="Rahul", age=21, course="MCA")
