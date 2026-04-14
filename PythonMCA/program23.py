print("Name - Swati Yadav ")
print("Class - MCA 2 nd ")
print("Role No. - 56")

correct_id = "admin"
correct_pass = "admin123"

while True:
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if user_id == correct_id and password == correct_pass:
        print("Login Successful")
        break
    else:
        print("Invalid credentials, try again")
