from risk.position_size import PositionSizer

class RiskEngine:

    def __init__(self):

        self.position_sizer = PositionSizer()

    def analyze(
        self,
        account_balance,
        entry,
        stop_loss,
        take_profit,
        risk_percent,
    ):

        risk_amount = account_balance * risk_percent

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
        }