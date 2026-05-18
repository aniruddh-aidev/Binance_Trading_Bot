# Binance Trading Bot

A small Python CLI tool that executes Market and Limit orders on Binance Futures Testnet. Written in a well-structured layered architecture that separates API communication, order execution, validation of user input, and CLI.

---

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/aniruddh-aidev/trading_bot.git
   cd trading_bot
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:
   ```
   API_KEY=your_testnet_api_key
   SECRET_KEY=your_testnet_secret_key
   ```
   Generate your API keys from: https://testnet.binancefuture.com

---

## How to Run

**Market Order:**
```
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.01
```

**Limit Order:**
```
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.01 --price 75000
```

After running, you will be prompted to confirm the order before it is placed.

---

## Project Structure

```
trading_bot/
  bot/
    __init__.py
    client.py         # Binance API communication and request signing
    order.py          # Order placement logic
    validator.py      # Input validation
    log_config.py     # Logging configuration
  cli.py              # CLI entry point
  README.md
  requirements.txt
  .env                # Not included — create manually
```

---

## Assumptions

Trders will be executed on the Binance Futures Testnet (USDT-M), NOT on regular Binance platform.

Limit orders set their timeInForce to GTC (Good Till Cancelled).
Currently supporting USDT-M futures markets (BTCUSDT, ETHUSDT and more).

Price field is mandatory when placing LIMIT order but Price field is mandatory when placing a LIMIT order but not required for MARKET orders.