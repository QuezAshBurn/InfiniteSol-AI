def count_pending(orders):
    return sum(order['status'] == 'pending' for order in orders)
