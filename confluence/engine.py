from config.settings import Settings


class ConfluenceEngine:

    def analyze(self, context):

        latest = context.latest

        bullish_score = 0
        bearish_score = 0

        bullish_reasons = []
        bearish_reasons = []

        # -------------------------
        # Trend
        # -------------------------

        if context.state["trend"] == "Bullish":

            bullish_score, bullish_reasons = self.add_evidence(
                bullish_score,
                bullish_reasons,
                Settings.TREND_WEIGHT,
                "Bullish Trend",
            )

        else:

            bearish_score, bearish_reasons = self.add_evidence(
                bearish_score,
                bearish_reasons,
                Settings.TREND_WEIGHT,
                "Bearish Trend",
            )

        # -------------------------
        # BOS
        # -------------------------

        if latest["confirmed_bos"]:

            if latest["bos_direction"] == "Bullish":

                bullish_score, bullish_reasons = self.add_evidence(
                    bullish_score,
                    bullish_reasons,
                    Settings.BOS_WEIGHT,
                    "Bullish BOS",
                )

            elif latest["bos_direction"] == "Bearish":

                bearish_score, bearish_reasons = self.add_evidence(
                    bearish_score,
                    bearish_reasons,
                    Settings.BOS_WEIGHT,
                    "Bearish BOS",
                )

        # -------------------------
        # CHOCH
        # -------------------------

        if latest["choch"]:

            if latest["choch_direction"] == "Bullish":

                bullish_score, bullish_reasons = self.add_evidence(
                    bullish_score,
                    bullish_reasons,
                    Settings.CHOCH_WEIGHT,
                    "Bullish CHOCH",
                )

            elif latest["choch_direction"] == "Bearish":

                bearish_score, bearish_reasons = self.add_evidence(
                    bearish_score,
                    bearish_reasons,
                    Settings.CHOCH_WEIGHT,
                    "Bearish CHOCH",
                )

        # -------------------------
        # Fair Value Gap
        # -------------------------

        if latest["fvg"] == "Bullish":

            bullish_score, bullish_reasons = self.add_evidence(
                bullish_score,
                bullish_reasons,
                Settings.FVG_WEIGHT,
                "Bullish FVG",
            )

        elif latest["fvg"] == "Bearish":

            bearish_score, bearish_reasons = self.add_evidence(
                bearish_score,
                bearish_reasons,
                Settings.FVG_WEIGHT,
                "Bearish FVG",
            )

        # -------------------------
        # Premium / Discount
        # -------------------------

        if latest["pd_zone"] == "Discount":

            bullish_score, bullish_reasons = self.add_evidence(
                bullish_score,
                bullish_reasons,
                Settings.PREMIUM_DISCOUNT_WEIGHT,
                "Discount Zone",
            )

        elif latest["pd_zone"] == "Premium":

            bearish_score, bearish_reasons = self.add_evidence(
                bearish_score,
                bearish_reasons,
                Settings.PREMIUM_DISCOUNT_WEIGHT,
                "Premium Zone",
            )

        # -------------------------
        # Liquidity Sweep
        # -------------------------

        if latest["liquidity_sweep"]:

            if latest["liquidity_side"] == "Sell Side":

                bullish_score, bullish_reasons = self.add_evidence(
                    bullish_score,
                    bullish_reasons,
                    Settings.LIQUIDITY_WEIGHT,
                    "Sell Side Liquidity Sweep",
                )

            elif latest["liquidity_side"] == "Buy Side":

                bearish_score, bearish_reasons = self.add_evidence(
                    bearish_score,
                    bearish_reasons,
                    Settings.LIQUIDITY_WEIGHT,
                    "Buy Side Liquidity Sweep",
                )

        score = max(bullish_score, bearish_score)

        reasons = (
            bullish_reasons
            if bullish_score >= bearish_score
            else bearish_reasons
        )

        return {

            # Legacy

            "score": score,

            "max_score": (
                Settings.TREND_WEIGHT
                + Settings.BOS_WEIGHT
                + Settings.CHOCH_WEIGHT
                + Settings.FVG_WEIGHT
                + Settings.PREMIUM_DISCOUNT_WEIGHT
                + Settings.LIQUIDITY_WEIGHT
            ),

            "strength": self.get_strength(score),

            "reasons": reasons,

            # New

            "bullish_score": bullish_score,
            "bearish_score": bearish_score,

            "bullish_reasons": bullish_reasons,
            "bearish_reasons": bearish_reasons,

        }

    def add_evidence(
        self,
        score,
        reasons,
        weight,
        reason,
    ):

        score += weight
        reasons.append(reason)

        return score, reasons

    def get_strength(self, score):

        if score >= 10:
            return "Excellent"

        elif score >= 7:
            return "Strong"

        elif score >= 5:
            return "Moderate"

        elif score >= 3:
            return "Weak"

        return "Poor"