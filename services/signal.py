class Signal:

    def analyze(self, market):

        score = 0
        reasons = []

        if market["ema20"] > market["ema50"]:
            score += 1
            reasons.append("✅ EMA20 is above EMA50")
        else:
            reasons.append("❌ EMA20 is below EMA50")

        if 40 <= market["rsi"] <= 70:
            score += 1
            reasons.append("✅ RSI is healthy")
        else:
            reasons.append("❌ RSI is outside the healthy range")

        if market["macd"] > 0:
            score += 1
            reasons.append("✅ MACD is bullish")
        else:
            reasons.append("❌ MACD is bearish")

        confidence = int((score / 3) * 100)

        signal = "BUY" if score >= 2 else "WAIT"

        return {
            "signal": signal,
            "confidence": confidence,
            "reasons": reasons,
        }