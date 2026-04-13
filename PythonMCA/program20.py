main_str = input("Enter main string: ")
sub_str = input("Enter substring: ")

index = main_str.find(sub_str)

if index != -1:
    print("First occurrence at index:", index)
else:
    print("Substring not found")