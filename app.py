from core.pipeline import Pipeline
from services.summary import Summary
from services.signal import Signal

pipeline = Pipeline()
summary = Summary()
signal = Signal()


df = pipeline.run("SOLUSDT")

latest = df.iloc[-1]

market = summary.generate(latest)
analysis = signal.analyze(market)

summary.display(latest)

print()

print(df.tail(20))
print("==========================")
print(" SIGNAL ANALYSIS")
print("==========================")

print("Signal:", analysis["signal"])

print("Confidence:", f"{analysis['confidence']}%")

print()

print("Reasons:")

for reason in analysis["reasons"]:
    print(reason)
