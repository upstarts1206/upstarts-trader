class PositionSizer:

    def calculate(
        self,
        account_balance,
        risk_percent,
        entry,
        stop_loss,
    ):

        risk_amount = account_balance * risk_percent

        stop_distance = abs(entry - stop_loss)

        if stop_distance == 0:
            return 0

        position_size = risk_amount / stop_distance

        return round(position_size, 4)