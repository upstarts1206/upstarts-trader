from models.market_context import MarketContext
from core.multi_timeframe_analyzer import MultiTimeframeAnalyzer
from decision.mtf_decision_engine import MTFDecisionEngine

context = MarketContext()
context.symbol = "BTCUSDT"

mtf = MultiTimeframeAnalyzer()
decision_engine = MTFDecisionEngine()

context = mtf.analyze(context)

decision = decision_engine.analyze(context)

print()

print("=" * 60)
print("MULTI TIMEFRAME ANALYSIS")
print("=" * 60)

for name, tf in context.timeframes.items():

    print()

    print(name.upper())

    print("-" * 30)

    print(tf.state)

print()

print("=" * 60)
print("MARKET THESIS")
print("=" * 60)

print(context.bias)

print()

print("=" * 60)
print("DECISION")
print("=" * 60)

print(decision)