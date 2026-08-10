class AlertManager:

    def __init__(self):

        self.active_alerts = {}

    def should_alert(self, context):

        symbol = context.symbol

        decision = context.trade_plan["decision"]

        confidence = context.trade_plan["decision_confidence"]

        previous = self.active_alerts.get(symbol)

        if previous is None:

            self.active_alerts[symbol] = {

                "decision": decision,

                "confidence": confidence,

            }

            return True

        if previous["decision"] != decision:

            self.active_alerts[symbol] = {

                "decision": decision,

                "confidence": confidence,

            }

            return True

        if confidence > previous["confidence"]:

            self.active_alerts[symbol] = {

                "decision": decision,

                "confidence": confidence,

            }

            return True

        return False