class TradeReview:

    def build(self, context):

        return {

            "symbol": context.symbol,

            "direction": context.bias["direction"],

            "signal": context.signal["signal"],

            "decision": context.decision["decision"],

            "confidence": context.decision["confidence"],

            "bullish_score": context.confluence["bullish_score"],

            "bearish_score": context.confluence["bearish_score"],

            "bullish_reasons": context.confluence["bullish_reasons"],

            "bearish_reasons": context.confluence["bearish_reasons"],

            "entry": context.trade_plan["entry"],

            "stop_loss": context.trade_plan["stop_loss"]["price"],

            "take_profit": context.trade_plan["take_profit"]["price"],

            "risk_reward": context.trade_plan["risk_reward"],

            "passed_validation": context.validation["valid"],

        }