class TakeProfitEngine:

    def calculate(self, df):

        latest = df.iloc[-1]

        future_swings = df[
            (df["swing_high"] == True)
            & (df["high"] > latest["close"])
        ]

        if future_swings.empty:

            return {
                "price": round(latest["close"] * 1.03, 2),
                "reason": "Default 3% Target"
            }

        target = future_swings.iloc[0]

        return {
            "price": round(target["high"], 2),
            "reason": "Nearest Swing High"
        }