class BiasEngine:

    def analyze(self, context):

        score = 0

        reasons = []

        latest = context.latest

        # -------------------------
        # Trend
        # -------------------------

        if context.state["trend"] == "Bullish":

            score += 1

            reasons.append("+1 Bullish Trend")

        else:

            score -= 1

            reasons.append("-1 Bearish Trend")

        # -------------------------
        # Break of Structure
        # -------------------------

        if latest["confirmed_bos"]:

            if latest["bos_direction"] == "Bullish":

                score += 2

                reasons.append("+2 Bullish BOS")

            elif latest["bos_direction"] == "Bearish":

                score -= 2

                reasons.append("-2 Bearish BOS")

        # -------------------------
        # Final Bias
        # -------------------------

        if score > 0:

            direction = "BUY"

        elif score < 0:

            direction = "SELL"

        else:

            direction = "NEUTRAL"

        confidence = abs(score)

        return {

            "direction": direction,

            "score": score,

            "confidence": confidence,

            "reasons": reasons,

        }