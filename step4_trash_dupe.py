import pandas as pd

print("\n--- Removing duplicate rows from KetoMojo MASTER file ---\n")

# File paths
INPUT_FILE = "/Users/lingxi.zhou/Documents/DRBOZ/KetoMojo2/KetoMojo_MASTER.csv"
OUTPUT_FILE = "/Users/lingxi.zhou/Documents/DRBOZ/KetoMojo2/KetoMojo_MASTER_DEDUPED.csv"

# Load CSV
df = pd.read_csv(INPUT_FILE)


# Columns to use for duplicate detection
dupe_cols = [
    "first_name",
    "last_name",
    "reading_type",
    "reading_timestamp"
]

# Check required columns exist
missing_cols = [c for c in dupe_cols if c not in df.columns]
if missing_cols:
    raise Exception(f"Missing required columns: {missing_cols}")

# Drop duplicates (keep first)
df_deduped = df.drop_duplicates(subset=dupe_cols, keep="first")


# Save cleaned file
df_deduped.to_csv(OUTPUT_FILE, index=False)
