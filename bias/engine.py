class BiasEngine:

    def analyze(self, context):

        bullish_score = context.confluence["bullish_score"]
        bearish_score = context.confluence["bearish_score"]

        if bullish_score > bearish_score:

            direction = "Bullish"

        elif bearish_score > bullish_score:

            direction = "Bearish"

        else:

            direction = "Neutral"

        return {

            "direction": direction,

            "bullish_score": bullish_score,

            "bearish_score": bearish_score,

            "difference": abs(
                bullish_score - bearish_score
            ),

        }