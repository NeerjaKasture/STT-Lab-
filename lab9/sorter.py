import pandas as pd

df = pd.read_csv("TypeMetrics.csv")

df = df[df["YALCOM"] != -1] # undefined yalcom

sorted_df = df.sort_values(
    by=["YALCOM", "LCOM3", "LCOM5", "LCOM2", "LCOM4", "LCOM1"],
    ascending=[True, False, True, False, False, False]
)

print("Top 10 Classes with Highest LCOM Values:")
print(sorted_df.head(5))

sorted_df.to_csv("sorted_lcom.csv", index=False)
