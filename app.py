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

print(f"Risk Amount : ${context.risk['risk_amount']}")
print(f"Risk/Reward : {context.risk['risk_reward']}R")
print(f"Trade Valid : {context.risk['valid']}")