from decision.confidence import ConfidenceEngine


class DecisionEngine:

    def __init__(self):

        self.confidence_engine = ConfidenceEngine()

    def decide(self, context):

        score = 0

        reasons = []

        # -------------------------
        # Trend
        # -------------------------

        if context.state["trend"] == "Bullish":

            score += 30

            reasons.append("+30 Trend is Bullish")

        # -------------------------
        # Signal
        # -------------------------

        if context.signal["signal"] == "BUY":

            score += 25

            reasons.append("+25 BUY Signal")

        # -------------------------
        # Risk
        # -------------------------

        if context.risk["valid"]:

            score += 25

            reasons.append("+25 Risk Accepted")

        # -------------------------
        # Confluence
        # -------------------------

        if context.confluence["score"] >= 4:

            score += 10

            reasons.append("+10 Strong Confluence")

        # -------------------------
        # Session
        # -------------------------

        if context.session in ["London", "New York"]:

            score += 10

            reasons.append("+10 Active Session")

        confidence = self.confidence_engine.calculate(score)

        if score >= 80:

            decision = "BUY"

        elif score >= 60:

            decision = "WAIT"

        else:

            decision = "SKIP"

        return {

            "decision": decision,

            "score": score,

            "confidence": confidence,

            "reasons": reasons,

        }