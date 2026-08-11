from strategies.ema_strategy import EMAStrategy


class Signal:

    def __init__(self):

        strategy = EMAStrategy()

        self.rules = strategy.get_rules()

    def analyze(self, context):

        score = 0
        reasons = []

        for rule in self.rules:

            passed, reason = rule.check(context)

            reasons.append(reason)

            if passed:

                score += 1

        confidence = int(score / len(self.rules) * 100)

        direction = context.bias["direction"]

        if direction == "Neutral":

            signal = "WAIT"

        elif score >= 2:

            signal = "BUY" if direction == "Bullish" else "SELL"

        else:

            signal = "WAIT"

        return {

            "signal": signal,

            "confidence": confidence,

            "reasons": reasons,

            "direction": direction,

        }