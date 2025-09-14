import MetaTrader5 as mt5
from datetime import datetime, timedelta

# Initialize MT5 connection
if not mt5.initialize():
    print("Failed to initialize MT5, error code:", mt5.last_error())
    quit()

# Select symbol and timeframe
symbol = "EURUSD.sd"
timeframe = mt5.TIMEFRAME_D1  # Daily bars

# Request last 10 bars from MT5
rates = mt5.copy_rates_from(symbol, timeframe, datetime.now(), 10)

if rates is None:
    print("Failed to get rates")
else:
    print("Last 10 bars for", symbol)
    for bar in rates:
        print(datetime.fromtimestamp(bar[0]), bar[1], bar[2], bar[3], bar[4], bar[5])

# Optional: Place a test market buy order (comment out when not testing real orders)

symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found")
    mt5.shutdown()
    quit()

if not symbol_info.visible:
    if not mt5.symbol_select(symbol, True):
        print("Failed to select symbol", symbol)
        mt5.shutdown()
        quit()

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": 0.01,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "deviation": 10,
    "magic": 234000,
    "comment": "Test order",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,  # changed here
}


result = mt5.order_send(request)
print("Order send result:", result)


mt5.shutdown()
