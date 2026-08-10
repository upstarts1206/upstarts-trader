from config.settings import Settings

class TradeFilter:

    def filter(self, results):

        filtered = []

        for context in results:

            if self.is_candidate(context):

                filtered.append(context)

        return filtered

    def is_candidate(self, context):

        plan = context.trade_plan

        if plan["decision"] == Settings.MIN_DECISION:

            return True

        return False