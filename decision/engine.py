from decision.confidence import ConfidenceEngine


class DecisionEngine:

    def __init__(self):

        self.confidence_engine = ConfidenceEngine()

    def decide(self, context):

        # -------------------------
        # Confidence
        # -------------------------

        confidence_result = self.confidence_engine.calculate(context)

        confidence = confidence_result["confidence"]

        reasons = confidence_result["reasons"]

        # -------------------------
        # Decision
        # -------------------------

        if confidence >= 80:

            decision = "BUY"

        elif confidence >= 60:

            decision = "WAIT"

        else:

            decision = "SKIP"

        # -------------------------
        # Return
        # -------------------------

        return {

            "decision": decision,

            "confidence": confidence,

            "reasons": reasons,

        }