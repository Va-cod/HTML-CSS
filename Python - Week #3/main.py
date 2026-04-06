from services import show_inventory, add_product, calculate_statistics, search_product, update_product, delate_product, inventory
from files import save_csv, upload_csv

# Block to view the menu and execute the available options
while True:
    print("\n * * * * MENU * * * * \n1. Display inventory \n2. Add products \n3. Calculate statistics \n4. Search product \n5. Update product \n6. Delate product \n7. Save cvs \n8. Upload csv \n9. Log out")
    option = input("\nEnter an option: ")
    if option == "1":
        show_inventory(inventory)
    elif option == "2":
        name = input("\nName: ").capitalize() # Ask for the product name
        # Block to validate errors
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
    elif option == "3":
        calculate_statistics(inventory)
    elif option == "4":
        product = input("\nProduct to search: ").capitalize()
        search = search_product(product, inventory)
        if search == None:
            print("\nProduct not found")
        else:
            print(search)
    elif option == "5":
        name = input("\nName: ").capitalize() # Ask for the product name
        search = search_product(name, inventory)
        if search == None:
            print("This product cannot be updated because it is not in stock.")
        else:
            # Block to validate errors
            while True:
                try:
                    new_quantity = int(input("Quantity: "))
                    new_price = float(input("Price: ")) # Ask for the product price
                    if new_quantity < 0 or new_price < 0: # Conditional to evaluate if the price is negative
                        print("The data entered must be positive.\n")
                        continue
                    break
                except:
                    print("Error value\n")
            update_product(name, new_quantity, new_price, inventory)
    elif option == "6":
        name = input("\nName: ").capitalize() # Ask for the product name
        delate_product(name, inventory)
    elif option == "7":
        file = "inventory.csv"
        save_csv(inventory, file)
    elif option == "8":
        new_inventory = []
        new_inventory = upload_csv("inventory.csv", inventory)
        print(new_inventory)
    elif option == "9":
        print("Exiting the system...")
        break
    else:
        print("Enter a valid option")

"""
This system is an inventory manager.

It can show all products in the list.
It can add new products with name, price, and quantity.
It can search a product by name.
It can update product information.
It can delete a product from the inventory.

Also, the system can calculate statistics like:
total value, most expensive product, and product with more quantity.

The system can save the inventory in a CSV file.
It can also load products from a CSV file.

When loading a file, it checks errors and ignores bad rows.
The user can choose to replace the inventory or merge the data.

This system helps to organize and manage products in a simple way.
"""