from risk.position_size import PositionSizer
from risk.stop_loss import StopLossEngine

class RiskEngine:

    def __init__(self):

        self.position_sizer = PositionSizer()
        self.stop_loss_engine = StopLossEngine()

    def analyze(
        self,
        account_balance,
        entry,
        take_profit,
        risk_percent,
        df,
    ):

        risk_amount = account_balance * risk_percent

        stop = self.stop_loss_engine.calculate(df)

        if stop is None:
            return None

        stop_loss = stop["price"]

        risk_per_unit = abs(entry - stop_loss)

        reward_per_unit = abs(take_profit - entry)

        if risk_per_unit == 0:
            rr = 0
        else:
            rr = reward_per_unit / risk_per_unit

        valid = rr >= 2

        position_size = self.position_sizer.calculate(
            account_balance,
            risk_percent,
            entry,
            stop_loss,
        )

        return {
            "risk_amount": round(risk_amount, 2),
            "risk_reward": round(rr, 2),
            "position_size": position_size,
            "valid": valid,
            "stop_loss": stop,
        }