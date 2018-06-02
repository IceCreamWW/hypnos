from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from purchase.models import *


def purchase(request):
	return render(request, "main/index.html", None)
# Create your views here.

@csrf_exempt
def create_order(request):
	if request.method == 'POST':
		customer_id = request.POST['customer_id']

		cur = connection.cursor()
		cur.callproc('CreateOrder', [customer_id, 0])
		cur.execute(sql='SELECT @_CreateOrder_1');
		order_id = cur.fetchall()[0][0]
		cur.close()

		return JsonResponse({"order_id" : order_id}, safe=False)

@csrf_exempt
def add_item_to_order(request):
	if request.method == 'POST':
		item = Item.objects.get(id=request.POST['item_id'])
		context = {
			"item" : item,
			"amount": request.POST['amount']
		}
		cur = connection.cursor()
		ret = cur.callproc('AddItemToOrder', [request.POST["order_id"], item.id, request.POST['amount']]) 
		cur.close();

		if ret is None:
			print("ret = None")
		else:
			print(ret)

		cur.close()
		return JsonResponse(context, safe=False);


