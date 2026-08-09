class ConfidenceEngine:

    def calculate(self, context):

        score = 0

        reasons = []

        # -------------------------
        # Trend
        # -------------------------

        if context.state["trend"] == "Bullish":

            score += 40

            reasons.append("+40 Trend is Bullish")

        # -------------------------
        # Signal
        # -------------------------

        if context.signal["signal"] == "BUY":

            score += 35

            reasons.append("+35 BUY Signal")

        # -------------------------
        # Risk
        # -------------------------

        if context.risk["valid"]:

            score += 25

            reasons.append("+25 Risk Accepted")

        return {

            "confidence": score,

            "reasons": reasons

        }