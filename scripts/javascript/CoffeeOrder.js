$(function () {
    var $orders = $('#orders');

    $.ajax({
        type: 'GET',
        url: '/api/order',
        success: function(orders) {
            $.each(orders, function(i, order) {
                $orders.append('<li>my order</li>');
                //$orders.append('<li>name: ' + order.name + ', drink' + order.drink + '</li>');
            });
        }
    });
});