from collections import OrderedDict
orders = OrderedDict()
for i in range(int(input("Enter the items you want to buy (Banana 5) :" ))):
    name, _, price = input().rpartition(' ')
    orders[name] = orders.get(name, 0) + int(price)
[print(*item) for item in orders.items()]


# Sample input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30



# Sample output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20