import pandas as pd

# Replace these with the values printed by calibrate_one_tether.py
offset = 84321.0
scale = 0.0011160409

df = pd.read_csv("tether_data.csv")

df["T1_N"] = (df["raw1"] - offset) * scale

print(df.head())

df.to_csv("tether_data_calibrated.csv", index=False)