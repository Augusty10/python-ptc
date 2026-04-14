
print("Name - Swati Yadav ")
print("Class - MCA 2 nd ")
print("Role No. - 56")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(a, b):
    for num in range(a, b + 1):
        if is_prime(num):
            print(num, end=" ")

# Example
print_primes(10, 30)
