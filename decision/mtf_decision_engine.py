class MTFDecisionEngine:

    def analyze(self, context):

        bias = context.bias

        macro = context.timeframes["macro"].state["trend"]
        structure = context.timeframes["structure"].state["trend"]
        entry = context.timeframes["entry"].state["trend"]

        reasons = []

        # ----------------------------------------
        # Perfect Alignment
        # ----------------------------------------

        if macro == "Bullish":

            if structure == "Bullish":

                if entry == "Bullish":

                    reasons.append("All timeframes are bullish.")

                    return {

                        "decision": "BUY",

                        "confidence": 100,

                        "reasons": reasons,

                    }

        if macro == "Bearish":

            if structure == "Bearish":

                if entry == "Bearish":

                    reasons.append("All timeframes are bearish.")

                    return {

                        "decision": "SELL",

                        "confidence": 100,

                        "reasons": reasons,

                    }

        # ----------------------------------------
        # Partial Alignment
        # ----------------------------------------

        if bias["alignment"]:

            reasons.append("Higher timeframe alignment detected.")

            return {

                "decision": bias["direction"],

                "confidence": bias["confidence"],

                "reasons": reasons,

            }

        # ----------------------------------------
        # Mixed Market
        # ----------------------------------------

        reasons.append("Timeframes are not aligned.")

        return {

            "decision": "WAIT",

            "confidence": bias["confidence"],

            "reasons": reasons,

        }