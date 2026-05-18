import os
import hmac
import time
import hashlib
import requests
import urllib.parse
from dotenv import load_dotenv
from bot.log_config import logger

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("SECRET_KEY")
base_url =  os.getenv("URL")

def gen_sign(string):
    
    return hmac.new(api_secret.encode('utf-8'), string.encode('utf-8'), hashlib.sha256).hexdigest()

def get_header():

    return {"X-MBX-APIKEY" : api_key}

def send_order(symbol, side, order_type, quantity, price):

    timestamp =  int(time.time() * 1000)
    params = {
        "symbol" : symbol,
        "side" : side,
        "type" : order_type,
        "quantity": quantity,
        "timestamp" : timestamp
    }
    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    query = urllib.parse.urlencode(params)
    sign = gen_sign(query)
    params["signature"] = sign
    header = get_header()
    logger.info(f"Sending order: {params}")
    resp = requests.post(base_url + "/fapi/v1/order", params=params, headers=header)
    logger.info(f"Response received: {resp.json()}")

    return resp.json()