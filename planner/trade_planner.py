class TradePlanner:

    def build(self, context):

        return {

            "symbol": context.symbol,

            "signal": context.signal["signal"],

            "confidence": context.signal["confidence"],

            "entry": round(context.latest["close"], 2),

            "trend": context.state["trend"],

            "momentum": context.state["momentum"],

            "strength": context.state["strength"],

            "stop_loss": context.risk["stop_loss"],

            "take_profit": context.risk["take_profit"],

            "risk_reward": context.risk["risk_reward"],

            "position_size": context.risk["position_size"],

            "valid_trade": context.risk["valid"],

        }