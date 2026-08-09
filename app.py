from core.analyzer import Analyzer
from models.market_context import MarketContext

context = MarketContext()

context.symbol = "SOLUSDT"

analyzer = Analyzer()

context = analyzer.analyze(context)

plan = context.trade_plan

print()
print("========================================")
print("     UPSTARTS TRADER - TRADE PLAN")
print("========================================")

# -------------------------
# Market
# -------------------------

print("Market")
print("------------------------")

print(f"Symbol         : {plan['symbol']}")
print(f"Trend          : {plan['trend']}")
print(f"Momentum       : {plan['momentum']}")
print(f"Strength       : {plan['strength']}")
print(f"Session        : {plan['session']}")

# -------------------------
# Signal
# -------------------------

print()
print("Signal")
print("------------------------")

print(f"Signal         : {plan['signal']}")
print(f"Confidence     : {plan['confidence']}%")

# -------------------------
# Trade
# -------------------------

print()
print("Trade")
print("------------------------")

print(f"Entry          : {plan['entry']}")
print(f"Stop Loss      : {plan['stop_loss']['price']}")
print(f"Take Profit    : {plan['take_profit']['price']}")

# -------------------------
# Risk
# -------------------------

print()
print("Risk")
print("------------------------")

print(f"Risk/Reward    : {plan['risk_reward']}R")
print(f"Position Size  : {plan['position_size']:.4f}")
print(f"Valid Trade    : {plan['valid_trade']}")

# -------------------------
# Confluence
# -------------------------

print()
print("Confluence")
print("------------------------")

print(f"Strength       : {plan['confluence']['strength']}")
print(f"Score          : {plan['confluence']['score']}/{plan['confluence']['max_score']}")

print()

for reason in plan["confluence"]["reasons"]:
    print(f"✓ {reason}")

# -------------------------
# Decision
# -------------------------

print()
print("Decision")
print("------------------------")

print(f"Action         : {plan['decision']}")
print(f"Confidence     : {plan['decision_confidence']}%")

print()

print("Reasons")

for reason in context.decision["reasons"]:
    print(reason)

# -------------------------
# Validation
# -------------------------

print()
print("Validation")
print("------------------------")

if context.validation["valid"]:

    print("✅ Trade Passed Validation")

else:

    print("❌ Trade Failed Validation")

    for error in context.validation["errors"]:

        print(f"- {error}")

print()
print("========================================")