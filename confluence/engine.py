from config.settings import Settings


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

            score += Settings.TREND_WEIGHT
            reasons.append("Bullish Trend")

            buy_score += Settings.TREND_WEIGHT
            buy_reasons.append("Bullish Trend")

        elif context.state["trend"] == "Bearish":

            sell_score += Settings.TREND_WEIGHT
            sell_reasons.append("Bearish Trend")

        # --------------------------------------------------
        # BOS
        # --------------------------------------------------

        if latest["confirmed_bos"]:

            score += Settings.BOS_WEIGHT
            reasons.append("Confirmed BOS")

            if latest["bos_direction"] == "Bullish":

                buy_score += Settings.BOS_WEIGHT
                buy_reasons.append("Bullish BOS")

            elif latest["bos_direction"] == "Bearish":

                sell_score += Settings.BOS_WEIGHT
                sell_reasons.append("Bearish BOS")

        # --------------------------------------------------
        # CHOCH
        # --------------------------------------------------

        if latest["choch"]:

            if latest["choch_direction"] == "Bullish":

                buy_score += Settings.CHOCH_WEIGHT
                buy_reasons.append("Bullish CHOCH")

            elif latest["choch_direction"] == "Bearish":

                sell_score += Settings.CHOCH_WEIGHT
                sell_reasons.append("Bearish CHOCH")

        # --------------------------------------------------
        # Fair Value Gap
        # --------------------------------------------------

        if latest["fvg"] == "Bullish":

            score += Settings.FVG_WEIGHT
            reasons.append("Bullish FVG")

            buy_score += Settings.FVG_WEIGHT
            buy_reasons.append("Bullish FVG")

        elif latest["fvg"] == "Bearish":

            sell_score += Settings.FVG_WEIGHT
            sell_reasons.append("Bearish FVG")

        # --------------------------------------------------
        # Premium / Discount
        # --------------------------------------------------

        if context.summary["pd_zone"] == "Discount":

            score += Settings.PREMIUM_DISCOUNT_WEIGHT
            reasons.append("Discount Zone")

            buy_score += Settings.PREMIUM_DISCOUNT_WEIGHT
            buy_reasons.append("Discount Zone")

        elif context.summary["pd_zone"] == "Premium":

            sell_score += Settings.PREMIUM_DISCOUNT_WEIGHT
            sell_reasons.append("Premium Zone")

        # --------------------------------------------------
        # Liquidity Sweep
        # --------------------------------------------------

        if context.summary["liquidity_sweep"]:

            if context.summary["liquidity_side"] == "Sell Side":

                score += Settings.LIQUIDITY_WEIGHT
                reasons.append("Sell Side Liquidity Sweep")

                buy_score += Settings.LIQUIDITY_WEIGHT
                buy_reasons.append("Sell Side Liquidity Sweep")

            elif context.summary["liquidity_side"] == "Buy Side":

                sell_score += Settings.LIQUIDITY_WEIGHT
                sell_reasons.append("Buy Side Liquidity Sweep")

        return {

            # Legacy API

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

            # New API

            "buy_score": buy_score,

            "sell_score": sell_score,

            "buy_reasons": buy_reasons,

            "sell_reasons": sell_reasons,

        }

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