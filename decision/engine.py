from decision.confidence import ConfidenceEngine


class DecisionEngine:

    def __init__(self):

        self.confidence_engine = ConfidenceEngine()

    def decide(self, context):

        score = 0
        reasons = []

        # -------------------------
        # Signal
        # -------------------------

        signal = context.signal["signal"]

        if signal == "BUY":

            score += 40
            reasons.append("+40 BUY Signal")

        elif signal == "SELL":

            score += 40
            reasons.append("+40 SELL Signal")

        # -------------------------
        # Confluence
        # -------------------------

        if context.confluence["strength"] in ["Strong", "Excellent"]:

            score += 30
            reasons.append("+30 Strong Confluence")

        # -------------------------
        # Risk
        # -------------------------

        if context.risk["valid"]:

            score += 20
            reasons.append("+20 Risk Accepted")

        # -------------------------
        # Session
        # -------------------------

        if context.session in ["London", "New York"]:

            score += 10
            reasons.append("+10 Active Session")

        confidence = self.confidence_engine.calculate(score)

        # -------------------------
        # Final Decision
        # -------------------------

        if signal == "WAIT":

            decision = "WAIT"

        elif score >= 80:

            decision = signal

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