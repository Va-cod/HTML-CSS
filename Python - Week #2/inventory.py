# Dictionary list to store each product
inventory = [{"Name": "Notebook", "Price": 3500., "Quantity": 10},
             {"Name": "Eraser", "Price": 2000., "Quantity": 20},
            ]

# Function to display inventory
def show_inventory():
    print("\n* * * * * INVENTORY * * * * *")
    if not inventory:
        print("Empty inventory")
    else:  
      for product in inventory:
        print(f"Name: {product['Name']}, Price: {product['Price']}, Quantity: {product['Quantity']}")