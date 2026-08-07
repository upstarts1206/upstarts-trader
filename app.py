from core.pipeline import Pipeline
from services.summary import Summary

pipeline = Pipeline()
summary = Summary()

df = pipeline.run("SOLUSDT")

latest = df.iloc[-1]

summary.display(latest)