from config.settings import Settings

class ConsoleView:

    def display(self, results, summary, errors):

        if Settings.SHOW_SCAN_SUMMARY:

            self.display_summary(summary)

        if errors:

            self.display_errors(errors)    

        if not results:

            self.display_no_trades()

            return

        if results:

            self.display_top_trade(results[0])

        for context in results:

            self.display_trade_plan(context)

    def display_trade_plan(self, context):

        print()
        print("=" * 40)
        print(f"UPSTARTS TRADER - {context.symbol}")
        print("=" * 40)

        self.display_market(context)
        self.display_signal(context)
        self.display_trade(context)
        self.display_risk(context)
        self.display_confluence(context)
        self.display_setup(context)
        self.display_decision(context)
        self.display_validation(context)

    # -------------------------
    # Market
    # -------------------------

    def display_market(self, context):

        plan = context.trade_plan

        print("Market")
        print("-" * 24)

        print(f"Symbol         : {plan['symbol']}")
        print(f"Trend          : {plan['trend']}")
        print(f"Momentum       : {plan['momentum']}")
        print(f"Strength       : {plan['strength']}")
        print(f"Session        : {plan['session']}")
        print(f"PD Zone        : {plan['pd_zone']}")

        liquidity = plan["liquidity_side"] or "None"

        print(f"Liquidity      : {liquidity}")

    # -------------------------
    # Signal
    # -------------------------

    def display_signal(self, context):

        plan = context.trade_plan

        print()
        print("Signal")
        print("-" * 24)

        print(f"Signal         : {plan['signal']}")
        print(f"Confidence     : {plan['confidence']}%")

    # -------------------------
    # Trade
    # -------------------------

    def display_trade(self, context):

        plan = context.trade_plan

        print()
        print("Trade")
        print("-" * 24)

        print(f"Entry          : {plan['entry']}")
        print(f"Stop Loss      : {plan['stop_loss']['price']}")
        print(f"Take Profit    : {plan['take_profit']['price']}")

    # -------------------------
    # Risk
    # -------------------------

    def display_risk(self, context):

        plan = context.trade_plan

        print()
        print("Risk")
        print("-" * 24)

        print(f"Risk/Reward    : {plan['risk_reward']}R")
        print(f"Position Size  : {plan['position_size']:.4f}")
        print(f"Valid Trade    : {plan['valid_trade']}")

    # -------------------------
    # Confluence
    # -------------------------

    def display_confluence(self, context):

        plan = context.trade_plan

        print()
        print("Market Thesis")
        print("-" * 24)

        print(f"Bullish Score  : {plan['bullish_score']}")
        print(f"Bearish Score  : {plan['bearish_score']}")
        print(f"Strength       : {plan['confluence_strength']}")

        print()
        print("Bullish Evidence")

        if plan["bullish_reasons"]:

            for reason in plan["bullish_reasons"]:
                print(f"✓ {reason}")

        else:

            print("- None")

        print()
        print("Bearish Evidence")

        if plan["bearish_reasons"]:

            for reason in plan["bearish_reasons"]:
                print(f"✓ {reason}")

        else:

            print("- None")

    # -------------------------
    # Setup
    # -------------------------

    def display_setup(self, context):

        plan = context.trade_plan

        print()
        print("Setup")
        print("-" * 24)

        print(f"Name           : {plan['setup']['name']}")
        print(f"Quality        : {plan['setup']['quality']}")

    # -------------------------
    # Decision
    # -------------------------

    def display_decision(self, context):

        plan = context.trade_plan

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

    def display_validation(self, context):

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

    # -------------------------
    # Summary
    # -------------------------

    def display_no_trades(self):

        print()
        print("=" * 50)
        print("        UPSTARTS TRADER")
        print("=" * 50)
        print()
        print("No trade opportunities found.")
        print()
        print("The scanner analyzed all symbols")
        print("but none passed the current filters.")
        print()
        print("Try again on the next candle.")
        print()
        print("=" * 50)

    def display_summary(self, summary):

        print()
        print("=" * 50)
        print("SCAN SUMMARY")
        print("=" * 50)

        print(f"Symbols Scanned     : {summary['symbols_scanned']}")
        print(f"Failed Symbols      : {summary['failed_symbols']}")
        print(f"BUY                 : {summary['buy']}")
        print(f"WAIT                : {summary['wait']}")
        print(f"SKIP                : {summary['skip']}")

        print()

        print(f"Highest Confidence  : {summary['highest_confidence']}%")
        print(f"Average Confidence  : {summary['average_confidence']}%")

        print()
        print(f"Next Scan           : {summary['next_scan']}")

        print("=" * 50)

    def display_top_trade(self, context):

        plan = context.trade_plan

        print()
        print("=" * 50)
        print("TOP TRADE TODAY")
        print("=" * 50)

        print(f"Symbol      : {plan['symbol']}")
        print(f"Decision    : {plan['decision']}")
        print(f"Confidence  : {plan['decision_confidence']}%")
        print(f"Confluence  : {plan['confluence']['score']}/{plan['confluence']['max_score']}")
        print(f"Risk/Reward : {plan['risk_reward']}R")

        print("=" * 50)

    # -------------------------
    # Errors
    # -------------------------

    def display_errors(self, errors):

        print()
        print("=" * 50)
        print("SCAN ERRORS")
        print("=" * 50)

        for error in errors:

            print(f"{error['symbol']}")
            print(f"Reason: {error['error']}")
            print("-" * 50)        