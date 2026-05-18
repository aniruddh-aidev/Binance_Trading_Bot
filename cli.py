import argparse
from bot.order import place_order
from bot.log_config import logger
from bot.validator import validator
from colorama import Fore, Style, init



def parse_args():

    parse = argparse.ArgumentParser(description = "Place your Order")
    parse.add_argument("--symbol", type = str, required = True, help = "Order's Symbol")
    parse.add_argument("--side", type = str, required = True, help = "Order side")
    parse.add_argument("--order_type", type = str, required = True, help = "Type of Order")
    parse.add_argument("--quantity", type = float, required = True, help = "Quantity of Order")
    parse.add_argument("--price", type = float, required = False, default = None, help = "Order price")

    return parse.parse_args()

def main():

    arg = parse_args()
    
    try:
        validator(arg.symbol, arg.side, arg.order_type, arg.quantity, arg.price)

        print(Fore.CYAN + "\n--- Order Request ---")
        print(f"Symbol: {arg.symbol}")
        print(f"Side: {arg.side}")
        print(f"Type: {arg.order_type}")
        print(f"Quantity: {arg.quantity}")
        if arg.price:
            print(f"Price: {arg.price}")
        print(f"---------------------\n")

        confirm = input("Confirm Your Order? (Yes/No): ")
        if confirm.lower() == "yes":
           pass
        elif confirm.lower() == "no":
           print(Fore.YELLOW + "Order cancelled.")
           return
        else:
           print(Fore.RED + "Invalid input. Please enter Yes or No.")
           return

        response = place_order(arg.symbol, arg.quantity, arg.price, arg.side, arg.order_type)
        
        if "orderId" in response:
            print(Fore.CYAN + "\n--- Order Response ---")
            print(f"Order ID: {response['orderId']}")
            print(f"Status: {response['status']}")
            print(f"Executed Qty: {response['executedQty']}")
            print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
            print(Fore.GREEN + "Success: Order placed successfully")
            print(f"----------------------\n")
        else:
            print(Fore.RED + f"Order failed: {response['msg']}")

    except Exception as e:
        logger.error(f"Error in Placing Order: {str(e)}")
        print(Fore.RED + f"Error in Placing Order: {str(e)}")

if __name__ == "__main__":

    main()