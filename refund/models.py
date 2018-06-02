from django.db import models
from purchase.models import *

# Create your models here.

REFUND_REQUEST_STATUS = (
	(0, 'unchecked'),
	(1, 'user_dropped'),
	(2, 'accepted'),
	(3, 'declined')
)


class RefundRequest(models.Model):
	id = models.AutoField(primary_key=True)
	status = models.IntegerField(choices=REFUND_REQUEST_STATUS)
	time = models.DateTimeField(null=True)
	order_id = models.ForeignKey(Order)

class ItemsInRefundRequest(models.Model):
	refund_id = models.ForeignKey(RefundRequest)
	item_id = models.ForeignKey(Item)
	amount = models.PositiveIntegerField()




