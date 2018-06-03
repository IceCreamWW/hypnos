from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from purchase.models import *
from purchase.utils.utils import script1


def purchase(request):
	return render(request, "main/index.html", None)
# Create your views here.

@csrf_exempt
def create_order(request):
	if request.method == 'GET':
		
		customer_id = request.GET['customer_id']
		cur = connection.cursor()
		cur.callproc('CreateOrder', [customer_id, 0])
		cur.execute(sql='SELECT @_CreateOrder_1');
		order_id = cur.fetchall()[0][0]
		cur.close()

		return JsonResponse({"order_id" : order_id}, safe=False)

@csrf_exempt
def get_random(request):
	if request.method == 'GET':
		data = script1(request.GET['order_id'])
		item = Item.objects.get(id=data['id'])
		data['name'] = item.name;
		data['price'] = item.price;
		return JsonResponse(data, safe=False)

@csrf_exempt
def add_item_to_order(request):
	if request.method == 'GET':
		item = Item.objects.get(id=request.GET['id'])
		context = {
			"item" : item,
			"amount": request.GET['amount']
		}
		cur = connection.cursor()
		cur.callproc('AddItemToOrder', [request.GET["order_id"], item.id, request.GET['amount']]) 
		cur.close();

		return JsonResponse({"status" : True}, safe=False);

def submit(request):
	if request.method == 'GET':
		cur = connection.cursor()
		cur.callproc('ConfirmOrder', [request.GET["order_id"],]) 
		cur.close();
		return render(request, "main/index.html", None)
