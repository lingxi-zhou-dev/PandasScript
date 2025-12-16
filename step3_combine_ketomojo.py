# Combine all the processed readings.xlsx files into one big csv
# We want to prep it to import it into keto_readings_raw table

import pandas as pd
from pathlib import Path

BASE = Path("/Users/lingxi.zhou/Documents/DRBOZ/KetoMojo2")

all_dfs = []

for outer in BASE.iterdir():
    if not outer.is_dir():
        continue

    for person_folder in outer.iterdir():
        if not person_folder.is_dir():
            continue

        # Look for renamed file: First_Last_readings.xlsx
        for file in person_folder.glob("*_readings.xlsx"):

            print(f"Adding: {file}")

            try:
                df = pd.read_excel(file)
                all_dfs.append(df)
            except Exception as e:
                print(f"⚠️ Skipping {file.name}: {e}")

# Combine everything
if all_dfs:
    master_df = pd.concat(all_dfs, ignore_index=True)

    output_file = BASE / "KetoMojo_MASTER.csv"
    master_df.to_csv(output_file, index=False)

    print(output_file)
    print(f"Rows: {len(master_df)}")

