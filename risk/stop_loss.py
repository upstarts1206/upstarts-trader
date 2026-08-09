class StopLossEngine:

    def calculate(self, df):

        latest = df.iloc[-1]

        previous_swings = df[
            (df["swing_low"] == True)
            & (df["low"] < latest["close"])
        ]

        if previous_swings.empty:
            return None

        latest_swing = previous_swings.iloc[-1]

        buffer = 0.10

        stop = latest_swing["low"] - buffer

        return {
            "price": round(stop, 2),
            "reason": "Below latest Swing Low"
        }