from risk.position_size import PositionSizer
from risk.stop_loss import StopLossEngine
from risk.take_profit import TakeProfitEngine


class RiskEngine:

    def __init__(self):

        self.position_sizer = PositionSizer()
        self.stop_loss_engine = StopLossEngine()
        self.take_profit_engine = TakeProfitEngine()

    def analyze(
        self,
        account_balance,
        entry,
        risk_percent,
        df,
    ):

        # -----------------------------
        # Risk Settings
        # -----------------------------

        risk_amount = account_balance * risk_percent

        # -----------------------------
        # Stop Loss
        # -----------------------------

        stop_result = self.stop_loss_engine.calculate(df)

        if stop_result is None:
            return None

        stop_price = stop_result["price"]

        # -----------------------------
        # Take Profit
        # -----------------------------

        take_profit_result = self.take_profit_engine.calculate(df)

        take_profit_price = take_profit_result["price"]

        # -----------------------------
        # Risk / Reward
        # -----------------------------

        risk_per_unit = abs(entry - stop_price)

        reward_per_unit = abs(take_profit_price - entry)

        if risk_per_unit == 0:
            rr = 0
        else:
            rr = reward_per_unit / risk_per_unit

        valid = rr >= 2

        # -----------------------------
        # Position Size
        # -----------------------------

        position_size = self.position_sizer.calculate(
            account_balance,
            risk_percent,
            entry,
            stop_price,
        )

        # -----------------------------
        # Return
        # -----------------------------

        return {
            "risk_amount": round(risk_amount, 2),
            "risk_reward": round(rr, 2),
            "position_size": position_size,
            "valid": valid,
            "stop_loss": stop_result,
            "take_profit": take_profit_result,
        }