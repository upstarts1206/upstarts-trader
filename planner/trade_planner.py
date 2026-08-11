class TradePlanner:

    def build(self, context):

        return {

            # -------------------------
            # Market
            # -------------------------

            "symbol": context.symbol,
            "direction": context.bias["direction"],
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
            "signal_confidence": context.signal["confidence"],

            # -------------------------
            # Risk
            # -------------------------

            "stop_loss": context.risk["stop_loss"],
            "take_profit": context.risk["take_profit"],
            "risk_reward": context.risk["risk_reward"],
            "position_size": context.risk["position_size"],
            "valid_trade": context.risk["valid"],

            # -------------------------
            # Session
            # -------------------------

            "session": context.session,

            # -------------------------
            # Confluence
            # -------------------------

            "bullish_score": context.confluence["bullish_score"],
            "bearish_score": context.confluence["bearish_score"],
            "confluence_strength": context.confluence["strength"],
            "bullish_reasons": context.confluence["bullish_reasons"],
            "bearish_reasons": context.confluence["bearish_reasons"],

            # -------------------------
            # Setup
            # -------------------------

            "setup": context.setup,

            # -------------------------
            # Decision
            # -------------------------

            "decision": context.decision["decision"],
            "decision_confidence": context.decision["confidence"],

        }