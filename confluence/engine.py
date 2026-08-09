class ConfluenceEngine:

    def analyze(self, context):

        score = 0

        reasons = []

        # -------------------------
        # Trend
        # -------------------------

        if context.state["trend"] == "Bullish":

            score += 1

            reasons.append("Bullish Trend")

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

        latest = context.latest

        if latest["confirmed_bos"]:

            score += 1

            reasons.append("Confirmed BOS")

        # -------------------------
        # FVG
        # -------------------------

        if latest["fvg"] == "Bullish":

            score += 1

            reasons.append("Bullish FVG")

        #-------------------------
        # Premium/Discount Zone
        #-------------------------

        if context.summary["pd_zone"] == "Discount":

            score += 1

            reasons.append("Discount Zone")    

        return {

            "score": score,

            "max_score": 6,

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