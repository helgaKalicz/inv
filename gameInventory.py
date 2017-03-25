# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

inventory = {}
added_items = []

# Displays the inventory.
def display_inventory(inventory):
    print("\nInventory:")
    for i, j in inventory.items():
        print(j, i)
    print("Total number of items:", sum(inventory.values()), "\n")


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        if (added_items[i]) in inventory:
            inventory[added_items[i]] += 1
        else:
            inventory[added_items[i]] = 1
    display_inventory(inventory)


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    import operator
    inv = list(reversed(sorted(inventory.items(), key=operator.itemgetter(1))))
    a = []
    b = []
    for i in range(len(inv)):
        a.append(inv[i][0])
        b.append(str(inv[i][1]))
    # Counts the strings lenght in a list.
    a1 = [len(a[i]) for i in range(len(a))]
    b1 = [len(b[i]) for i in range(len(b))]
    a2 = "item name"
    b2 = "count"
    # This code is for in case of an empty inventory.
    if a1 and (max(a1) >= len(a2)):
        a_lenght = max(a1)
    else:
        a_lenght = len(a2)
    if b1 and (max(b1) >= len(b2)):
        b_lenght = max(b1)
    else:
        b_lenght = len(b2)
    # Printing
    print("Inventory:")
    print(" " * (b_lenght - len(b2)) + b2 + " " * (2 + a_lenght - len(a2)) + a2)
    print("-" * (b_lenght + a_lenght + 2))
    for i in range(len(a)):
        print(" " * (b_lenght - len(str(b[i]))) + str(b[i]) + " " * (2 + a_lenght - len(a[i])) + a[i])
    print("-" * (b_lenght + a_lenght + 2))
    print("Total number of items:", sum(inventory.values()), "\n")


# Imports new inventory items from a fileprint(inventory
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as f:
        loot = list(f.read().split(','))
    add_to_inventory(inventory, loot)
    print_table(inventory, order=None)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, "w") as f:
        for i in inventory:
            loot = f.write((i + ",") * inventory[i])
print_table(inventory, order=None)