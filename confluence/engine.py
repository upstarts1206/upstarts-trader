class ConfluenceEngine:

    def analyze(self, context):

        score = 0

        reasons = []

        latest = context.latest

        bias = context.bias["direction"]

        # -------------------------
        # Trend
        # -------------------------

        if (
            bias == "BUY"
            and context.state["trend"] == "Bullish"
        ):

            score += 1

            reasons.append("Trend Supports BUY Bias")

        elif (
            bias == "SELL"
            and context.state["trend"] == "Bearish"
        ):

            score += 1

            reasons.append("Trend Supports SELL Bias")

        # -------------------------
        # Signal
        # -------------------------

        if context.signal["signal"] == "BUY":

            score += 1

            reasons.append("Signal Confirmed")

        # -------------------------
        # Risk
        # -------------------------

        if context.risk["valid"]:

            score += 1

            reasons.append("Risk Approved")

        # -------------------------
        # BOS
        # -------------------------

        if latest["confirmed_bos"]:

            if latest["bos_direction"] == "Bullish" and bias == "BUY":

                score += 1

                reasons.append("Bullish BOS")

            elif latest["bos_direction"] == "Bearish" and bias == "SELL":

                score += 1

                reasons.append("Bearish BOS")

        # -------------------------
        # FVG
        # -------------------------

        if latest["fvg"] == "Bullish" and bias == "BUY":

            score += 1

            reasons.append("Bullish FVG")

        elif latest["fvg"] == "Bearish" and bias == "SELL":

            score += 1

            reasons.append("Bearish FVG")

        # -------------------------
        # Premium / Discount
        # -------------------------

        if (
            context.summary["pd_zone"] == "Discount"
            and bias == "BUY"
        ):

            score += 1

            reasons.append("Discount Zone")

        elif (
            context.summary["pd_zone"] == "Premium"
            and bias == "SELL"
        ):

            score += 1

            reasons.append("Premium Zone")

        # -------------------------
        # Liquidity Sweep
        # -------------------------

        if context.summary["liquidity_sweep"]:

            if (
                context.summary["liquidity_side"] == "Sell Side"
                and bias == "BUY"
            ):

                score += 1

                reasons.append("Sell Side Liquidity Sweep")

            elif (
                context.summary["liquidity_side"] == "Buy Side"
                and bias == "SELL"
            ):

                score += 1

                reasons.append("Buy Side Liquidity Sweep")

        return {

            "score": score,

            "max_score": 7,

            "strength": self.get_strength(score),

            "reasons": reasons,

        }

    def get_strength(self, score):

        if score >= 5:

            return "Excellent"

        elif score >= 4:

            return "Strong"

        elif score >= 3:

            return "Moderate"

        elif score >= 2:

            return "Weak"

        return "Poor"