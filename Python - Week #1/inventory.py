# Enter the product name
name = input("Product name: ")

# Data validation block
while True:
    try:
        price = float(input("Price: ")) # Enter the product price
        if price < 0:
            print("Price must be positive.\n")
            continue
        break
    except:
        print("Error value\n")

# Data validation block
while True:
    try:
        quantity = int(input("Quantity: ")) # Enter the quantity of the product
        if quantity < 0:
            print("Quantity must be positive.\n")
            continue
        break
    except:
        print("Error value\n")

# Calculate the total cost
total_cost = quantity * price

# Print the information
print(f"\nProduct: {name}\nPrice: {price}\nQuantity: {quantity}\nTotal: {total_cost}")


# The following code simulates a simple inventory system. 
# First, the program asks for the product name, price, and quantity. 
# Then, it calculates the total profit. 
# Finally, it shows the product information on the screen.
