import MetaTrader5 as mt5

# Initialize connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("Initialize() failed, error code =", mt5.last_error())
else:
    print("MT5 initialized successfully")

# Shut down connection
mt5.shutdown()
