from config.settings import Settings

class TradeRanker:

    def rank(self, results):

        return sorted(

            results,

            key=self.calculate_score,

            reverse=True,

        )

    def calculate_score(self, context):

        plan = context.trade_plan

        score = 0

        score += (

            plan["decision_confidence"]

            * Settings.CONFIDENCE_WEIGHT

        )

        score += (

            plan["confluence"]["score"]

            * Settings.CONFLUENCE_WEIGHT

        )

        score += min(

            plan["risk_reward"]

            * Settings.RISK_REWARD_WEIGHT,

            50,

        )        

        return score