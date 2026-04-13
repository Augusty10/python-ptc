menu={
    "chai ":10,
    "coffee":20,
    "Cookeis":15
}
print(" Welcome to Red Brevarage Shop ")
print("Menu:")
for item,price in menu.items():
    print(f"{item}: ${price}")
total =0
while True:
    order = input("\nEnter item name (or 'exit' to finish): ").lower()
    
    if order == "exit":
        break
    
    if order in menu:
        qty = int(input("Enter quantity: "))
        total += menu[order] * qty  
        print(f"{order} added to your order")
    else:
        print("Item not available")

print("\n Total Bill: ₹", total)
print("Thank you! Visit again ") 