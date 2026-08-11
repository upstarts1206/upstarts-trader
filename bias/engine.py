class BiasEngine:

    def analyze(self, context):

        score = 0

        reasons = []

        direction = "NEUTRAL"

        return {

            "direction": direction,

            "score": score,

            "confidence": score,

            "reasons": reasons,

        }