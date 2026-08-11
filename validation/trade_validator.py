class TradeValidator:

    def validate(self, context):

        errors = []

        direction = context.trade_plan["direction"]

        entry = context.trade_plan["entry"]
        stop = context.trade_plan["stop_loss"]["price"]
        target = context.trade_plan["take_profit"]["price"]

        # -------------------------
        # BUY Validation
        # -------------------------

        if direction == "Bullish":

            if stop >= entry:

                errors.append(
                    "Stop Loss must be below Entry for BUY trades."
                )

            if target <= entry:

                errors.append(
                    "Take Profit must be above Entry for BUY trades."
                )

        # -------------------------
        # SELL Validation
        # -------------------------

        elif direction == "Bearish":

            if stop <= entry:

                errors.append(
                    "Stop Loss must be above Entry for SELL trades."
                )

            if target >= entry:

                errors.append(
                    "Take Profit must be below Entry for SELL trades."
                )

        # -------------------------
        # Position Size
        # -------------------------

        if context.trade_plan["position_size"] <= 0:

            errors.append(
                "Position Size must be greater than zero."
            )

        # -------------------------
        # Risk / Reward
        # -------------------------

        if context.trade_plan["risk_reward"] < 2:

            errors.append(
                "Risk/Reward is below the minimum threshold."
            )

        return {

            "valid": len(errors) == 0,

            "errors": errors

        }