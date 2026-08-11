class BiasEngine:

    def analyze(self, context):

        score = 0

        reasons = []

        direction = "NEUTRAL"

        # -------------------------
        # Trend
        # -------------------------

        if context.state["trend"] == "Bullish":

            score += 1

            reasons.append("Bullish Trend")

        else:

            score -= 1

            reasons.append("Bearish Trend")

        # -------------------------
        # Final Bias
        # -------------------------

        if score > 0:

            direction = "BUY"

        elif score < 0:

            direction = "SELL"

        return {

            "direction": direction,

            "score": score,

            "confidence": abs(score),

            "reasons": reasons,

        }