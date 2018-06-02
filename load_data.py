import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hypnos.settings")
django.setup()

from purchase import models
from data import item_list


for id, name, price, stock in item_list:
    search_set = models.Item.objects.filter(id=id)
    if len(search_set) == 0:
        item = models.Item(id=id, name=name, price=price, stock=stock)
        item.save()
