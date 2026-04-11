# Dictionary list to store each product
inventory = [{"Name": "Notebook", "Price": 3500., "Quantity": 10},
             {"Name": "Eraser", "Price": 2000., "Quantity": 20},
            ]

# Function to display inventory
def show_inventory(lista):
    print("\n* * * * * INVENTORY * * * * *")
    if not lista:
      print("Empty inventory")
    else:
      for product in lista:
        print(f"Name: {product['Name']}, Price: {product['Price']}, Quantity: {product['Quantity']}")

# Function to add products
def add_product(name, quantity, price):
  product = {"Name": name, "Price": price, "Quantity": quantity} # Dictionary with product data
  inventory.append(product) # Dictionary added to list
  print("Product added to inventory")

def calculate_statistics(lista):
  total_inventory = 0
  print("\n * * * STATISTICS * * *")
  for product in lista:
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
      show_inventory(inventory)
    elif opcion == "2":
      name = input("\nName: ") # Ask for the product name
      while True:
        try:
          quantity = int(input("Quantity: "))
          price = float(input("Price: ")) # Ask for the product price
          if quantity < 0 or price < 0: # Conditional to evaluate if the price is negative
            print("The data entered must be positive.\n")
            continue
          break
        except:
          print("Error value\n")
      add_product(name, quantity, price)
    elif opcion == "3":
      calculate_statistics(inventory)
    elif opcion == "4":
      print("Exiting the system...")
      break
    else:
        print("Enter a valid option")

# This code allows the user to view stored products, add new items with data validation (price and quantity),
# and calculate statistics such as the total inventory value and the number of registered products.
# It also features an interactive menu that facilitates navigation between the different options,
# making the system easy to use and understand.