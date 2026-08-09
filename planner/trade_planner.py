class TradePlanner:

    def build(self, context):

        return {

            # -------------------------
            # Market
            # -------------------------

            "symbol": context.symbol,

            "entry": round(context.latest["close"], 2),

            # -------------------------
            # Market Analysis
            # -------------------------

            "trend": context.state["trend"],
            "momentum": context.state["momentum"],
            "strength": context.state["strength"],

            # -------------------------
            # Signal
            # -------------------------

            "signal": context.signal["signal"],
            "confidence": context.signal["confidence"],

            # -------------------------
            # Risk
            # -------------------------

            "stop_loss": context.risk["stop_loss"],
            "take_profit": context.risk["take_profit"],
            "risk_reward": context.risk["risk_reward"],
            "position_size": context.risk["position_size"],
            "valid_trade": context.risk["valid"],

            # -------------------------
            # Decision
            # -------------------------

            "decision": context.decision["decision"],
            "decision_confidence": context.decision["confidence"],

        }