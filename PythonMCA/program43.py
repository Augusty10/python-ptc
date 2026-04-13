# Global variable
x = 10

def show():
    # Local variable
    y = 5
    print("Inside function:")
    print("Global x =", x)
    print("Local y =", y)

show()

print("\nOutside function:")
print("Global x =", x)