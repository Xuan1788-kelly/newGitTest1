$(function (){
    var $orders = $('#orders');
    var $name = $('#name');
    var $drink = $('#drink');

    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:5500/git_first_try/newGitTest1/api/orders.json',
        success: function(orders) {
            $.each(orders, function(i, order) {
                var j = i + 1;
                $orders.append('<li>order num ' +  j + '</li>');
                $orders.append('<li>name: ' + order.name + ', drink: ' + order.drink + '</li>');
            });
        },
        error: function() {
            alert("No such api");
        }
    });

    $('#add-orders').on('click', function() {
        var order = {
            name: $name.val(),
            drink: $drink.val(),
        };

        $.ajax({
            type: 'GET',
            // 'POST' shall fail when the destination is a concrete JSON file
            url: 'http://127.0.0.1:5500/git_first_try/newGitTest1/api/orders.json',
            success: function() {
                alert("start saving your order");
                $orders.append('<li>name: ' + order.name + ', drink: ' + order.drink + '</li>');
            },
            error: function() {
                alert("error saving order");
            }
        });
    });
});