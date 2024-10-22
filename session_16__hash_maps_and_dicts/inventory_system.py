# inventory_system.py
import copy

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    inventory = dict()
    inventory["Electronics"] = {"Laptop" : {'name':"Laptop", 'price': 120, 'quantity': 8}}
    inventory["Groceries"] = {}
    return inventory

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    inventory[category].update({item_name : update_info})

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    # inv1.update(inv2)
    for k_categories,v_categories in inv2.items():
        inv1.setdefault(k_categories,v_categories)
        for k_prod,v_prod in v_categories.items():
            inv1[k_categories].setdefault(k_prod,v_prod)
    return inv1

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory[category]

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    expensive_item = None
    for k_categories,v_categories in inventory.items():
        for k_prod,v_prod in v_categories.items():
            if expensive_item:
                if v_prod["price"] > expensive_item["price"]:
                    expensive_item = v_prod
            else:
                expensive_item = v_prod
    return expensive_item

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for k_categories,v_categories in inventory.items():
        item = v_categories.get(item_name, None)
        if item:
            return item
    return None


def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return inventory.keys()

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    items = []
    for k_categories,v_categories in inventory.items():
        items += list(v_categories.values())
    return items


def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    category_item_pairs = []
    for k_categories,v_categories in inventory.items():
        for k_prod,v_prod in v_categories.items():
            category_item_pairs.append((k_categories,v_prod))
    return category_item_pairs
    

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    if deep:
        return copy.deepcopy(inventory)
    else:
        return copy.copy(inventory)
