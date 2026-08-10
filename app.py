from scanner.scanner import Scanner
from watchlists.default import WATCHLIST

scanner = Scanner()

results = scanner.scan(WATCHLIST)

for context in results:

    plan = context.trade_plan

    print()
    print("=" * 40)
    print(f"UPSTARTS TRADER - {plan['symbol']}")
    print("=" * 40)

    # -------------------------
    # Market
    # -------------------------

    print("Market")
    print("-" * 24)

    print(f"Symbol         : {plan['symbol']}")
    print(f"Trend          : {plan['trend']}")
    print(f"Momentum       : {plan['momentum']}")
    print(f"Strength       : {plan['strength']}")
    print(f"Session        : {plan['session']}")
    print(f"PD Zone        : {plan['pd_zone']}")

    liquidity = plan["liquidity_side"]

    if liquidity is None:
        liquidity = "None"

    print(f"Liquidity      : {liquidity}")

    # -------------------------
    # Signal
    # -------------------------

    print()
    print("Signal")
    print("-" * 24)

    print(f"Signal         : {plan['signal']}")
    print(f"Confidence     : {plan['confidence']}%")

    # -------------------------
    # Trade
    # -------------------------

    print()
    print("Trade")
    print("-" * 24)

    print(f"Entry          : {plan['entry']}")
    print(f"Stop Loss      : {plan['stop_loss']['price']}")
    print(f"Take Profit    : {plan['take_profit']['price']}")

    # -------------------------
    # Risk
    # -------------------------

    print()
    print("Risk")
    print("-" * 24)

    print(f"Risk/Reward    : {plan['risk_reward']}R")
    print(f"Position Size  : {plan['position_size']:.4f}")
    print(f"Valid Trade    : {plan['valid_trade']}")

    # -------------------------
    # Confluence
    # -------------------------

    print()
    print("Confluence")
    print("-" * 24)

    print(f"Strength       : {plan['confluence']['strength']}")
    print(f"Score          : {plan['confluence']['score']}/{plan['confluence']['max_score']}")

    print()

    for reason in plan["confluence"]["reasons"]:
        print(f"✓ {reason}")

    # -------------------------
    # Setup
    # -------------------------

    print()
    print("Setup")
    print("-" * 24)

    print(f"Name           : {plan['setup']['name']}")
    print(f"Quality        : {plan['setup']['quality']}")

    # -------------------------
    # Decision
    # -------------------------

    print()
    print("Decision")
    print("-" * 24)

    print(f"Action         : {plan['decision']}")
    print(f"Score          : {context.decision['score']}/100")
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
    print("-" * 24)

    if context.validation["valid"]:

        print("✅ Trade Passed Validation")

    else:

        print("❌ Trade Failed Validation")

        for error in context.validation["errors"]:

            print(f"- {error}")

    print()
    print("=" * 40)