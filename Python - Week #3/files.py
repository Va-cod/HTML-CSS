import os
from services import *

# Function to save csv
def save_csv(inventory, file):
    """
    Saves the inventory data into a CSV file.

    The function:
    - Validates that the inventory is not empty.
    - Writes a header (Name,Price,Quantity).
    - Writes each product as a row in the file.
    - Handles permission and general errors.

    Parameters:
    inventory (list): A list of dictionaries with product data.
    file (str): The path or name of the file to save.

    Returns:
    None
    """
    # Validate that the inventory is not empty.
    if not inventory:
        print("The inventory is empty. There is no data to save.")
        return
    try:
        with open(file, mode="w") as archivo:
            # Write header
            archivo.write("Name,Price,Quantity\n")
            # Write the inventory data
            for product in inventory:
                Name = product.get("Name", "")
                Price = product.get("Price", 0)
                Quantity = product.get("Quantity", 0)
                archivo.write(f"{Name},{Price},{Quantity}\n")
        route = os.path.abspath(file)
        print(f"Inventory saved in: {route}")
    except PermissionError:
        print("Error: You do not have permission to write to the specified path.")
    except Exception:
        print(f"Error saving the file: {Exception}")

# Funtion to upload csv
def upload_csv(file, inventory):
    """
    Loads products from a CSV file and updates the inventory.

    The function:
    - Validates the file header (Name,Price,Quantity).
    - Reads and validates each row.
    - Converts Price to float and Quantity to int.
    - Skips invalid rows.
    - Asks the user if they want to overwrite or merge data.
    - Merges by product name if not overwritten.

    Parameters:
    file (str): The path or name of the CSV file to read.
    inventory (list): The current inventory list.

    Returns:
    None
    """
    added_products = []
    invalid_rows = 0

    try:
        archivo = open(file, "r")
        # Read header
        header = archivo.readline().strip()
        if header != "Name,Price,Quantity":
            print("Error: invalid header. Must be: Name,Price,Quantity")
            archivo.close()
            return

        # Read lines
        for line in archivo:
            try:
                parts = line.strip().split(",")

                if len(parts) != 3:
                    raise ValueError
                
                Name = parts[0].strip()
                Price = float(parts[1])
                Quantity = int(parts[2])

                if Price < 0 or Quantity < 0:
                    raise ValueError

                added_products.append({
                    "Name": Name,
                    "Price": Price,
                    "Quantity": Quantity
                })

            except ValueError:
                invalid_rows += 1

        archivo.close()

    except FileNotFoundError:
        print("Error: File not found.")
        return
    except UnicodeDecodeError:
        print("Error: File encoding problem.")
        return
    except Exception as error:
        print(f"Unexpected error: {error}")
        return

    # Ask the user
    opcion = input("Overwrite current inventory? (Y/N): ").strip().upper()

    if opcion == "Y":
        inventory = added_products
        accion = "Replacement"
    else:
        # Fusion by name
        inventory_dict = {}
        for product in inventory:
            inventory_dict[product["Name"]] = product

        for product in added_products:
            Name = product["Name"]
            if Name in inventory_dict:
                inventory_dict[Name]["Quantity"] += product["Quantity"]
                if inventory_dict[Name]["Price"] != product["Price"]:
                    inventory_dict[Name]["Price"] = product["Price"]
            else:
                inventory_dict[Name] = product

        inventory = list(inventory_dict.values())
        accion = "Merge: Quantity added and Price updated"

    # Summary
    print("\nSummary:")
    print("Products loaded:", len(added_products))
    print("Invalid rows omitted:", invalid_rows)
    print("Action taken:", accion)