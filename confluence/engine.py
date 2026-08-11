class ConfluenceEngine:

    def analyze(self, context):

        # --------------------------------------------------
        # Legacy API
        # --------------------------------------------------

        score = 0

        reasons = []

        # --------------------------------------------------
        # New API
        # --------------------------------------------------

        buy_score = 0

        sell_score = 0

        buy_reasons = []

        sell_reasons = []

        latest = context.latest

        # --------------------------------------------------
        # Trend
        # --------------------------------------------------

        if context.state["trend"] == "Bullish":

            # Legacy

            score += 1

            reasons.append("Bullish Trend")

            # New

            buy_score += 1

            buy_reasons.append("Bullish Trend")

        elif context.state["trend"] == "Bearish":

            sell_score += 1

            sell_reasons.append("Bearish Trend")

        # --------------------------------------------------
        # Existing Logic
        # --------------------------------------------------

        #
        # Leave EVERYTHING below exactly as-is.
        # We migrate one concept per lesson.
        #

        # -------------------------
        # Signal
        # -------------------------

        if context.signal["signal"] == "BUY":

            score += 1

            reasons.append("BUY Signal")

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

            score += 1

            reasons.append("Confirmed BOS")

        # -------------------------
        # FVG
        # -------------------------

        if latest["fvg"] == "Bullish":

            score += 1

            reasons.append("Bullish FVG")

        # -------------------------
        # Premium / Discount
        # -------------------------

        if context.summary["pd_zone"] == "Discount":

            score += 1

            reasons.append("Discount Zone")

        # -------------------------
        # Liquidity Sweep
        # -------------------------

        if (
            context.summary["liquidity_sweep"]
            and context.summary["liquidity_side"] == "Sell Side"
        ):

            score += 1

            reasons.append("Sell Side Liquidity Sweep")

        # --------------------------------------------------

        return {

            # Legacy API

            "score": score,

            "max_score": 7,

            "strength": self.get_strength(score),

            "reasons": reasons,

            # New API

            "buy_score": buy_score,

            "sell_score": sell_score,

            "buy_reasons": buy_reasons,

            "sell_reasons": sell_reasons,

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