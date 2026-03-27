num_users = int(input("Enter number of users: "))
user_items_dict = {}

for _ in range(num_users):
    username = input("Enter username: ")
    num_items = int(input("How many items? "))
    items_list = []
    for i in range(num_items):
        item = input(f"Item {i + 1}: ")
        items_list.append(item)
    user_items_dict[username] = items_list

all_items_flat = []
for items in user_items_dict.values():
    temp_unique = []
    for item in items:
        if item not in temp_unique:
            temp_unique.append(item)
    all_items_flat.extend(temp_unique)

item_counts = {}
for item in all_items_flat:
    item_counts[item] = item_counts.get(item, 0) + 1

common_items = []
for item, count in item_counts.items():
    if count > 1:
        common_items.append(item)

unique_items_list = []
for item, count in item_counts.items():
    if count == 1:
        unique_items_list.append(item)

print("\nCOMMON ITEMS:")
for item in common_items:
    print(item)

print("\nUNIQUE ITEMS:")
for item in unique_items_list:
    print(item)

if item_counts:
    max_popularity = 0
    for count in item_counts.values():
        if count > max_popularity:
            max_popularity = count

    print("\nMOST POPULAR ITEM:")
    for item, count in item_counts.items():
        if count == max_popularity:
            print(item)