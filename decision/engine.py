class DecisionEngine:

    def decide(self, context):

        reasons = []

        score = 0

        # Trend
        if context.state["trend"] == "Bullish":
            score += 1
            reasons.append("✓ Higher trend is Bullish")
        else:
            reasons.append("✗ Higher trend is not Bullish")

        # Signal
        if context.signal["signal"] == "BUY":
            score += 1
            reasons.append("✓ Signal is BUY")
        else:
            reasons.append("✗ Signal is WAIT")

        # Risk
        if context.risk["valid"]:
            score += 1
            reasons.append("✓ Risk/Reward is acceptable")
        else:
            reasons.append("✗ Risk/Reward is below minimum")

        if score == 3:
            decision = "BUY"

        elif score == 2:
            decision = "WAIT"

        else:
            decision = "SKIP"

        return {
            "decision": decision,
            "score": score,
            "reasons": reasons,
        }