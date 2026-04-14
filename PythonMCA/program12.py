
print("Name - Swati Yadav ")
print("Class - MCA 2 nd ")
print("Role No. - 56")

num = int(input(" Enter the number : "))

sum_digit=0
product=1

while num>0:
    digit=num%10
    sum_digit+=digit
    product *=digit
    num = num//10
    
print("Sum:", sum_digit)
print("Product:", product)
