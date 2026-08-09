class SetupEngine:

    def detect(self, context):

        latest = context.latest

        # -------------------------
        # Bullish Continuation
        # -------------------------

        if (
            context.state["trend"] == "Bullish"
            and context.signal["signal"] == "BUY"
            and context.summary["pd_zone"] == "Discount"
            and context.risk["valid"]
        ):

            return {
                "name": "Bullish Continuation",
                "quality": "Good",
            }

        # -------------------------
        # Bullish Pullback
        # -------------------------

        if (
            context.state["trend"] == "Bullish"
            and context.summary["pd_zone"] == "Premium"
        ):

            return {
                "name": "Wait for Pullback",
                "quality": "Low",
            }

        return {
            "name": "No Valid Setup",
            "quality": "Poor",
        }