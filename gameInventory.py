# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

inventory = {}
added_items = []
# Making some solours
c0 = '\033[0m'
c1 = '\033[34m'
c2 = '\033[35m'
c3 = '\033[94m'
c4 = '\033[95m'

# Displays the inventory.
def display_inventory(inventory):
    print(c2 + "\nInventory:")
    for i, j in inventory.items():
        print(c3 + str(j), i)
    print(c2 + "Total number of items:" + c1, sum(inventory.values()), c0 + "\n")


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
    # Making two list from a sorted inventory.
    import operator
    inv = list(reversed(sorted(inventory.items(), key=operator.itemgetter(1))))
    a = []
    b = []
    for i in range(len(inv)):
        a.append(inv[i][0])
        b.append(str(inv[i][1]))
    # Counts the strings' lenght in the lists, and making new lists of them.
    a1 = [len(a[i]) for i in range(len(a))]
    b1 = [len(b[i]) for i in range(len(b))]
    a2 = "item name"
    b2 = "count"
    # This code is for in case of an empty inventory, and also to handle any lenght.
    if a1 and (max(a1) >= len(a2)):
        a_lenght = max(a1)
    else:
        a_lenght = len(a2)
    if b1 and (max(b1) >= len(b2)):
        b_lenght = max(b1)
    else:
        b_lenght = len(b2)
    # Printing
    print(c2 + "\nInventory:")
    print(c1 + " " * (b_lenght - len(b2)) + b2 + " " * (2 + a_lenght - len(a2)) + a2)
    print(c2 + "-" * (b_lenght + a_lenght + 2))
    for i in range(len(a)):
        print(c3 + " " * (b_lenght - len(str(b[i]))) + str(b[i]) + " " * (2 + a_lenght - len(a[i])) + a[i])
    print(c2 + "-" * (b_lenght + a_lenght + 2))
    print(c2 + "Total number of items:" + c1, sum(inventory.values()), c0 + "\n")


# Imports new inventory items from a fileprint(inventory
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as f:
        added_items = list(f.read().split(','))
    add_to_inventory(inventory, added_items)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    import operator
    inv = list(sorted(inventory.items(), key=operator.itemgetter(0)))
    a = []
    b = []
    for i in range(len(inv)):
        a.append(inv[i][0])
        b.append(str(inv[i][1]))
    loot = []
    for i in range(len(a)):
        for j in range(int(b[i])):
            loot.append(a[i])
    with open(filename, "w") as f:
        for i in range(len(loot)-1):
            f.write((loot[i] + ","))
        f.write(loot[len(loot)-1])
    print_table(inventory, order=None)