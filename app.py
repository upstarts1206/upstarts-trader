from core.analyzer import Analyzer
from models.market_context import MarketContext

context = MarketContext()

context.symbol = "SOLUSDT"

analyzer = Analyzer()

context = analyzer.analyze(context)

print()

print("========================================")
print(" UPSTARTS TRADER - TRADE PLAN ")
print("========================================")

plan = context.trade_plan

print(f"Symbol         : {plan['symbol']}")
print(f"Trend          : {plan['trend']}")
print(f"Momentum       : {plan['momentum']}")
print(f"Strength       : {plan['strength']}")

print()

print(f"Signal         : {plan['signal']}")
print(f"Confidence     : {plan['confidence']}%")

print()

print(f"Entry          : {plan['entry']}")
print(f"Stop Loss      : {plan['stop_loss']['price']}")
print(f"Take Profit    : {plan['take_profit']['price']}")

print()

print(f"Risk/Reward    : {plan['risk_reward']}R")
print(f"Position Size  : {plan['position_size']:.4f}")

print()

print(f"Valid Trade    : {plan['valid_trade']}")

plan = context.trade_plan

print()

print("Decision")
print("------------------------")

print("Action :", plan["decision"])

print(f"Confidence : {plan['decision_confidence']}%")

print()

print("Reasons")

for reason in context.decision["reasons"]:
    print(reason)

print()

print("Validation")
print("------------------------")

if context.validation["valid"]:

    print("✅ Trade Passed Validation")

else:

    print("❌ Trade Failed Validation")

    for error in context.validation["errors"]:

        print("-", error)
print("========================================")