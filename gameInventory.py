# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for i, j in inventory.items():
        print(j, i)
    print("Total number of items:", sum(inventory.values()))
display_inventory(inventory)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        if (added_items[i]) in inventory:
            inventory[added_items[i]] += 1
        else:
            inventory[added_items[i]] = 1
    display_inventory(inventory)
add_to_inventory(inventory, added_items)


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
    a_lenght = max([len(a[i]) for i in range(len(a))])
    b_lenght = max([len(b[i]) for i in range(len(b))])
    if a_lenght < len("item name"):
        a_lenght = len("item name")
    if b_lenght < len("count"):
        b_lenght = len("count")
    print("Inventory:")
    print("-" * (b_lenght + a_lenght + 2))
    print(" " * (b_lenght - len("count")) + "count" + " " * (2 + a_lenght - len("item name")) + "item name")
    for i in range(len(a)):
        print(" " * (b_lenght - len(str(b[i]))) + str(b[i]) + " " * (2 + a_lenght - len(a[i])) + a[i])
    print("-" * (b_lenght + a_lenght + 2))
    print("Total number of items:", sum(inventory.values()))
print_table(inventory, order=None)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
