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
            "pd_zone": context.summary["pd_zone"],
            "liquidity_sweep": context.summary["liquidity_sweep"],
            "liquidity_side": context.summary["liquidity_side"],

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

            #-------------------------
            # Session
            # -------------------------

            "session": context.session,

            # -------------------------
            # Decision
            # -------------------------

            "decision": context.decision["decision"],
            "decision_confidence": context.decision["confidence"],

            # -------------------------
            # Confluence
            # -------------------------

            "confluence": context.confluence,

        }