var total = 0;	
$(function() {
	$("#add").click(function(event) {
		var order_id = $('#table-items').data('order-id')
		if (order_id == -1) {
			customer_id = random_customer_id()
			$('h3').text("Customer: " + customer_id)
			$.getJSON('create', {"customer_id" : customer_id} , function(json, textStatus) {
				$('#table-items').data('order-id', json['order_id'])
				$("a").attr("href", "/purchase/submit?order_id=" + json['order_id'])
				add(json['order_id'])
			});
		} else {
			add(order_id)
		}
	})
});

function add(order_id) {
	$.getJSON('get_random', {'order_id' : order_id}, function(json, textStatus) {
		$("#items-placeholder").remove();
		$("tr").removeClass('cur');
		$("<tr class=\"cur\"></tr>").prependTo('table > tbody');
		$("<td>" + json['id'] + "</td>").appendTo('tr.cur');
		$("<td>" + json['name'] + "</td>").appendTo('tr.cur');
		$("<td>" + json['price'] + "</td>").appendTo('tr.cur');
		$("<td>" + json['amount'] + "</td>").appendTo('tr.cur');
		$("<td>" + json['price'] * json['amount'] + "</td>").appendTo('tr.cur');
		
		total += json['price'] * json['amount'];
		delete json['name'];
		delete json['price'];

		$('#total').text("Total: " + total);

		json["order_id"] = order_id;

		$.getJSON('add', json, function(json, textStatus) {
			if (!json['status']) {
				alert("Error");
			}
		});
	});
}

function random_customer_id() {
  var customer_id = "";
  var possible = "X0123456789";

  for (var i = 0; i < 18; i++)
    customer_id += possible.charAt(Math.floor(Math.random() * possible.length));

  return customer_id;
}

