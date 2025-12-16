import pandas as pd
import re

# 1. Load the CSV
df = pd.read_csv("KetoMojo_MASTER_DEDUPED.csv")

# 2. Strip timezone and milliseconds
def strip_timezone(ts):
    if pd.isna(ts):
        return ts
    # Remove timezone and milliseconds using regex
    ts = re.sub(r'\.\d+.*', '', ts)   # remove .000-05:00 or .123Z etc
    ts = ts.replace("T", " ")         # replace T with space
    return ts

df["clean_timestamp"] = df["reading_timestamp"].astype(str).apply(strip_timezone)

# 3. Convert to datetime (now naive/local)
df["clean_timestamp"] = pd.to_datetime(df["clean_timestamp"], errors="coerce")

# 4. Extract local hour
df["local_hour"] = df["clean_timestamp"].dt.hour

# 5. Filter for before 11 AM
df_before_11 = df[df["local_hour"] < 11]

# 6. Keep only target types
target_types = ["ketone", "dbr", "glucose"]
df_before_11 = df_before_11[df_before_11["reading_type"].isin(target_types)]

# 7. Select columns
columns = ["first_name", "last_name", "clean_timestamp", "reading_value"]
df_before_11 = df_before_11[columns + ["reading_type"]]

# 8. Export per type
for reading in target_types:
    filtered = df_before_11[df_before_11["reading_type"] == reading]
    filtered = filtered.drop(columns=["reading_type"])
    filtered.to_csv(f"{reading}_before_11am.csv", index=False)
