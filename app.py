from core.market import Market
from indicators.ema import EMA

# Download market data
market = Market()

df = market.get_candles(
    symbol="BTCUSDT",
    interval="60",
    limit=100
)

# Calculate EMA
ema = EMA()

df = ema.calculate(
    df,
    period=50
)

# Display results
print(df.tail())