# Simple inventory management application.
# Each item in the inventory will have a name, price, quantity, and category.
# Program has basic maintenance functions to add, change, delete and view items.
#
# The inventory is maintained as a list of dictionaries. Each dictionary element is
# an inventory item composed of the following keys: name, price, quantity, and category.


def fetch_inventory():
    return [
        {'name': 'Oat milk', 'price': 2.59, 'quantity': 25, 'category': 'dairy'},
        {'name': 'Cheddar cheese', 'price': 2.08, 'quantity': 50, 'category': 'dairy'}
    ]


# Function to add an item to an inventory.
# Parameters:
#   inventory_list - list of dictionaries, inventory to update
#   new_item       - dictionary, item to be added
def add_item(inventory_list, new_item):
    inventory_list.append(new_item)


# Function to update an item in an inventory.
# The item name should match an existing item in the inventory. If it doesn't, no change will occur.
# All the values in the existing inventory item are replaced from the passed item data.
# Parameters:
#   inventory_list - list of dictionaries, inventory
#   item_data      - dictionary, item data to replace the existing item in the inventory
# Returns: message giving results of update
def update_item(inventory_list, item_data):
    item_found = False
    for item in inventory_list:
        if item['name'].lower() == item_data['name'].lower():
            item_data['name'] = item_data['name'].capitalize()
            item.update(item_data)
            item_found = True
            break
    if item_found:
        return item_data['name'] + " updated in inventory"
    else:
        return "Update error: No inventory item exists with the name " + item_data['name']


# Function to remove an item from an inventory.
# The item name should match an existing item in the inventory. If it doesn't, no change will occur.
# Parameters:
#   inventory_list - list of dictionaries, inventory
#   name_value     - string, name of the item to delete
# Returns: message giving results of removal
def remove_item(inventory_list, name_value):
    item_found = False
    for i in range(len(inventory_list)):
        if inventory_list[i].get('name').lower() == name_value.lower():
            inventory_list.pop(i)
            item_found = True
            break
    if item_found:
        return name_value + " deleted"
    else:
        return "Delete error: No inventory item exists with the name " + name_value


# Function to print an inventory's contents showing all the details.
# Parameters:
#   inventory_list - list of dictionaries, inventory
def print_inventory(inventory_list):
    for item in inventory_list:
        print(f"Item Name={item['name']}, Price={item['price']:.2f}, Quantity={item['quantity']}, Category={item['category']}")


# Function to view an inventory.
# Parameters:
#   inventory_list - list of dictionaries, inventory
def view_inventory(inventory_list):
    print()
    print("List of Inventory:")
    print_inventory(inventory_list)


# Function to search an inventory for all items in a particular category.
# Parameters:
#   inventory_list - list of dictionaries, inventory
#   categ_value    - string, category to search for in the inventory
def search_by_category(inventory_list, categ_value):
    selected_items = [item for item in inventory_list if item['category'] == categ_value]
    print()
    if len(selected_items) > 0:
        print(f"List of items in Category {categ_value}:")
        print_inventory(selected_items)
    else:
        print("No items in the inventory with a category of", categ_value)


# Function to get the data for an item from the user.
# Returns: a dictionary containing the data for the item
def get_item_data():
    new_name = input("Enter the item name: ").capitalize()
    new_price = float(input("Enter the price: "))
    new_qty = int(input("Enter the quantity: "))
    new_categ = input("Enter the category: ")
    return {'name': new_name, 'price': new_price, 'quantity': new_qty, 'category': new_categ}


def main():

    # Loop to receive and process user input
    while True:
        print()
        print("Enter one of the following options:")
        print("l=list all inventory, a=add item, u=update item, d=delete item, s=search for items in a category, q=quit")
        request = input(": ")
        if request == 'q':
            break

        if request == 'l':
            view_inventory(inventory)
        elif request == 'a':
            item_data = get_item_data()
            add_item(inventory, item_data)
        elif request == 'u':
            item_data = get_item_data()
            print(update_item(inventory, item_data))
        elif request == 'd':
            delete_value = input("Enter the name of the item to delete: ")
            print(remove_item(inventory, delete_value))
        elif request == 's':
            search_value = input("Enter the category of items to find: ")
            search_by_category(inventory, search_value)
        else:
            print("Invalid input, please try again")


# Set the initial inventory data
inventory = fetch_inventory()

main()
