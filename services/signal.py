from strategies.ema_strategy import EMAStrategy


class Signal:

    def __init__(self):

        strategy = EMAStrategy()

        self.rules = strategy.get_rules()

    def analyze(self, market):

        score = 0
        reasons = []

        for rule in self.rules:

            passed, reason = rule.check(market)

            reasons.append(reason)

            if passed:
                score += 1

        confidence = int(score / len(self.rules) * 100)

        signal = "BUY" if score >= 2 else "WAIT"

        return {
            "signal": signal,
            "confidence": confidence,
            "reasons": reasons,
        }