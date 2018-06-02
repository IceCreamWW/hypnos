import random
from purchase.utils.data import item_list
item_id_list = [entry[0] for entry in item_list]

def script1(order_id: int) -> dict:
    entry = random.choice(item_list)
    amount = random.randint(1, entry[3])
    return {"order_id": order_id, "id": entry[0], "amount": amount}
