from core.market import Market

market = Market()

candles = market.get_candles(
    symbol="BTCUSDT",
    interval="60",
    limit=10
)

print(candles)