from core.market import Market
from indicators.ema import EMA
from indicators.rsi import RSI

# Download market data
market = Market()

df = market.get_candles(
    symbol="BTCUSDT",
    interval="60",
    limit=200
)

# Calculate indicators
ema = EMA()
rsi = RSI()

df = ema.calculate(df, period=20)
df = ema.calculate(df, period=50)
df = rsi.calculate(df, period=14)

# Display latest rows
print(df.tail())