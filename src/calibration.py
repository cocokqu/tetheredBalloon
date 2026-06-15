import pandas as pd


# calibrates a dataset
# Replace these with the values printed by calibrate_one_tether.py
offset = 84321.0
scale = 0.0011160409


FILENAME = ""
df = pd.read_csv(f"{FILENAME}.csv")

df["T1_N"] = (df["raw1"] - offset) * scale

print(df.head())

df.to_csv("tether_data_calibrated.csv", index=False)