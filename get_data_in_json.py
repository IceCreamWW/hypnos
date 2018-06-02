from data import item_list

print("item_list = [")
for entry in item_list:
    print("{{id: {}, name: '{}', price:{}, stock:{}}}".format(*entry))
print("]")
