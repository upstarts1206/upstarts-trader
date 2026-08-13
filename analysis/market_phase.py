class MarketPhase:

    def analyze(self, latest):

        trend = (
            "Bullish"
            if latest["EMA_20"] > latest["EMA_50"]
            else "Bearish"
        )

        bos = latest["bos_direction"] if latest["bos"] else None
        choch = latest["choch_direction"] if latest["choch"] else None

        return self.determine_phase(

            trend,

            bos,

            choch,

        )

    def determine_phase(

        self,

        trend,

        bos,

        choch,

    ):

        # ----------------------------------------
        # Bullish Trend
        # ----------------------------------------

        if trend == "Bullish":

            if choch == "Bearish":

                return "Bullish Reversal"

            if bos == "Bullish":

                return "Bullish Continuation"

            return "Bullish Pullback"

        # ----------------------------------------
        # Bearish Trend
        # ----------------------------------------

        if choch == "Bullish":

            return "Bearish Reversal"

        if bos == "Bearish":

            return "Bearish Continuation"

        return "Bearish Pullback"