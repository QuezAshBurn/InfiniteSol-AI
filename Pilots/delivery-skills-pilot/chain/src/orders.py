def count_pending(orders):
    return sum(
        order['status'] == 'pending' and order.get('archived') is not True
        for order in orders
    )
