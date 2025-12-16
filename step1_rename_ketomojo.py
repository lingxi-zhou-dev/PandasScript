# Modify the BASE to the folder that is containing all the ketomojo readings
# 1. Walk through every person’s folder
# 2. Take readings.xlsx
# 3. Remove the first 3 rows
# 4. Add first_name and last_name columns
# 5. Rename the file to {First_Last_readings.xlsx}

import pandas as pd
from pathlib import Path

BASE = Path("/Users/lingxi.zhou/Documents/DRBOZ/KetoMojo2")

for outer in BASE.iterdir():
    if not outer.is_dir():
        continue

    for person_folder in outer.iterdir():
        if not person_folder.is_dir():
            continue

        # Expecting folder: First Last
        name_parts = person_folder.name.strip().split(" ")
        if len(name_parts) < 2:
            print(f"Skipping folder (cannot parse name): {person_folder.name}")
            continue

        first_name = name_parts[0]
        last_name = "_".join(name_parts[1:])

        readings_file = person_folder / "readings.xlsx"
        if not readings_file.exists():
            print(f"No readings file in: {person_folder.name}")
            continue

        print(f"Processing {person_folder.name}")

        df = pd.read_excel(readings_file, header=3)

        df.insert(0, "first_name", first_name)
        df.insert(1, "last_name", last_name.replace("_", " "))

        new_name = f"{first_name}_{last_name}_readings.xlsx"
        new_file = person_folder / new_name

        df.to_excel(new_file, index=False)

        print(f"Saved: {new_file}")
