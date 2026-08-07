from rules.ema_rule import EMARule
from rules.rsi_rule import RSIRule
from rules.macd_rule import MACDRule


class EMAStrategy:

    def get_rules(self):

        return [

            EMARule(),

            RSIRule(),

            MACDRule()

        ]