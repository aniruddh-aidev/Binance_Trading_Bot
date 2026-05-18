def validator(symbol, side, order_type, quantity, price):

    if symbol == ""  or not symbol.upper().endswith("USDT"):
        raise ValueError("Invalid symbol")
    
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")
    
    if order_type not in ["LIMIT", "MARKET"]:
        raise ValueError("Invalid type")
    
    if quantity <= 0:
        raise ValueError("Invalid quantity")    
    
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Invalid price [Price required for LIMIT orders]")