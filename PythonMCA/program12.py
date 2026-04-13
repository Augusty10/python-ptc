num = int(input(" Enter the number : "))

sum_digits=0
product=1

while num>0:
    digit=num%10
    sum_digit+=digit
    product *=digit
    num = num//10
    
print("Sum:", sum_digits)
print("Product:", product)
