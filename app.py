from core.pipeline import Pipeline

pipeline = Pipeline()

df = pipeline.run("SOLUSDT")

print(df.tail())