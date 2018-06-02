from django.db import models

# Create your models here.

ORDER_STATUS = (
    (0, 'unpaid'),
    (1, 'paid'),
    (2, 'dropped')
)

class Item(models.Model):
    id = models.CharField(primary_key=True, max_length=18)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.PositiveIntegerField()

class Order(models.Model):
	id = models.BigAutoField(primary_key=True)
	time = models.DateTimeField(null=True)
	status = models.IntegerField(choices=ORDER_STATUS)
	customer_id = models.CharField(max_length=18)


class ItemsInOrder(models.Model):
	order_id = models.ForeignKey(Order)
	item_id = models.ForeignKey(Item)
	amount = models.PositiveIntegerField()

	class Meta:
		unique_together = (('order_id', 'item_id'), )
