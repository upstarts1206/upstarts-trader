class ScanSummary:

    def generate(self, results, errors):

        summary = {

            "symbols_scanned": len(results),

            "failed_symbols": len(errors),

            "buy": 0,

            "wait": 0,

            "skip": 0,

            "highest_confidence": 0,

            "average_confidence": 0,

        }

        total_confidence = 0

        for context in results:

            decision = context.trade_plan["decision"]

            confidence = context.trade_plan["decision_confidence"]

            total_confidence += confidence

            if confidence > summary["highest_confidence"]:

                summary["highest_confidence"] = confidence

            if decision == "BUY":

                summary["buy"] += 1

            elif decision == "WAIT":

                summary["wait"] += 1

            else:

                summary["skip"] += 1

        if results:

            summary["average_confidence"] = round(

                total_confidence / len(results),

                1

            )

        return summary