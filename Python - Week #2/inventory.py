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

# Function to add products
def add_product():
  name = input("\nName: ") # Ask for the product name
  
  # Data validation block
  while True:
    try:
      price = float(input("Price: ")) # Ask for the product price
      if price < 0: # Conditional to evaluate if the price is negative
        print("Price must be positive.\n")
        continue
      break
    except:
      print("Error value\n")

  # Data validation block
  while True:
    try:
      quantity = int(input("Quantity: ")) # Ask for the product quantity
      if quantity < 0: # Conditional to evaluate if the quantity is negative
        print("Quantity must be positive.\n")
        continue
      break
    except:
      print("Error value\n")
  
  product = {"Name": name, "Price": price, "Quantity": quantity} # Dictionary with product data
  inventory.append(product) # Dictionary added to list
  print("Product added to inventory") 

# Function to calculate and display statistics
def calculate_statistics():
  total_inventory = 0
  print("\n * * * STATISTICS * * *")
  for product in inventory:
    total = product["Price"] * product["Quantity"] # Variable that stores the total cost for each product
    total_inventory += total # Variable that stores the total cost of inventory
    print(f"{product['Name']} ---> ${total}")
  total_products = len(inventory)
  print("-----------------------")
  print(f"Total products: {total_products}")
  print(f"Total inventory: {total_inventory}")

# Block to view the menu and execute the available options
while True:
    print("\n * * * * MENU * * * * \n1. Display inventory \n2. Add products \n3. Calculate statistics \n4. Log out")

    opcion = input("\nEnter an option: ")

    if opcion == "1":
      show_inventory()
    elif opcion == "2":
      add_product()
    elif opcion == "3":
      calculate_statistics()
    elif opcion == "4":
      print("Exiting the system...")
      break
    else:
        print("Enter a valid option")

# This code allows the user to view stored products, add new items with data validation (price and quantity), 
# and calculate statistics such as the total inventory value and the number of registered products. 
# It also features an interactive menu that facilitates navigation between the different options, 
# making the system easy to use and understand.