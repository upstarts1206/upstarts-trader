from core.analyzer import Analyzer
from models.market_context import MarketContext

context = MarketContext()

context.symbol = "SOLUSDT"

analyzer = Analyzer()

context = analyzer.analyze(context)

print()

print("======================")
print("RISK ANALYSIS")
print("======================")

print(f"Risk Amount   : ${context.risk['risk_amount']}")
print(f"Risk/Reward   : {context.risk['risk_reward']}R")
print(f"Position Size : {context.risk['position_size']:.4f}")
print(f"Trade Valid   : {context.risk['valid']}")

print()
print("Suggested Stop Loss")
print("-------------------")
print(f"Price  : {context.risk['stop_loss']['price']}")
print(f"Reason : {context.risk['stop_loss']['reason']}")