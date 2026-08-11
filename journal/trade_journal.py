import csv
import os


class TradeJournal:

    FILE_NAME = "trade_journal.csv"

    def save(self, context):

        file_exists = os.path.exists(self.FILE_NAME)

        with open(
            self.FILE_NAME,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow([
                    "Timestamp",
                    "Symbol",
                    "Direction",
                    "Signal",
                    "Decision",
                    "Confidence",
                    "Bullish Score",
                    "Bearish Score",
                    "Risk Reward",
                    "Passed Validation",
                ])

            writer.writerow([
                context.review.get("timestamp", ""),
                context.review["symbol"],
                context.review["direction"],
                context.review["signal"],
                context.review["decision"],
                context.review["confidence"],
                context.review["bullish_score"],
                context.review["bearish_score"],
                context.review["risk_reward"],
                context.review["passed_validation"],
            ])