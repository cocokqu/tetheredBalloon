import pandas as pd

g = 9.81  

# Known calibration mass
known_mass_g = 100  # change this for mass used
known_force_N = (known_mass_g / 1000) * g


# Read calibration files
weight = "10g"
FILENAME = f"tether_{weight}.csv"
zero_df = pd.read_csv("tether_0g.csv", names=["time_ms", "raw1"])
loaded_df = pd.read_csv(FILENAME, names=["time_ms", "raw1"])

# Get average raw readings
raw_zero = zero_df["raw1"].mean()
raw_loaded = loaded_df["raw1"].mean()

# Compute calibration
offset = raw_zero
scale = known_force_N / (raw_loaded - raw_zero)

print("Calibration results for tether 1")
print("--------------------------------")
print(f"Known mass: {known_mass_g} g")
print(f"Known force: {known_force_N:.4f} N")
print(f"Raw zero average: {raw_zero:.2f}")
print(f"Raw loaded average: {raw_loaded:.2f}")
print(f"Raw difference: {raw_loaded - raw_zero:.2f}")
print(f"Offset: {offset:.2f}")
print(f"Scale: {scale:.10f} N/count")

print()
print("Use this equation:")
print("T1_N = (raw1 - offset) * scale")