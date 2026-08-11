class BiasAggregator:

    def analyze(self, context):

        macro = context.timeframes["macro"]
        structure = context.timeframes["structure"]
        entry = context.timeframes["entry"]

        macro_trend = macro.state["trend"]
        structure_trend = structure.state["trend"]
        entry_trend = entry.state["trend"]

        reasons = []

        bullish = 0
        bearish = 0

        # ----------------------------------------
        # Macro Bias
        # ----------------------------------------

        if macro_trend == "Bullish":

            bullish += 1
            reasons.append("4H Bullish")

        else:

            bearish += 1
            reasons.append("4H Bearish")

        # ----------------------------------------
        # Structure Bias
        # ----------------------------------------

        if structure_trend == "Bullish":

            bullish += 1
            reasons.append("1H Bullish")

        else:

            bearish += 1
            reasons.append("1H Bearish")

        # ----------------------------------------
        # Entry Bias
        # ----------------------------------------

        if entry_trend == "Bullish":

            bullish += 1
            reasons.append("15M Bullish")

        else:

            bearish += 1
            reasons.append("15M Bearish")

        # ----------------------------------------
        # Overall Direction
        # ----------------------------------------

        if bullish > bearish:

            direction = "BUY"

        elif bearish > bullish:

            direction = "SELL"

        else:

            direction = "WAIT"

        alignment = bullish == 3 or bearish == 3

        confidence = max(bullish, bearish) / 3 * 100

        return {

            "direction": direction,

            "alignment": alignment,

            "bullish": bullish,

            "bearish": bearish,

            "confidence": int(confidence),

            "reasons": reasons,

        }