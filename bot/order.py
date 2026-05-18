from bot.client import send_order

def place_order(symbol, quantity, price, side, order_type):

    return send_order(symbol, side, order_type, quantity, price)