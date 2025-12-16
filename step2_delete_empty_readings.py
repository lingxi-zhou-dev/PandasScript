# Delete all _readings.xlsx files that are less than 5kb

from pathlib import Path

BASE = Path("/Users/lingxi.zhou/Documents/DRBOZ/KetoMojo2")
SIZE_LIMIT = 5 * 1024  # 5 KB in bytes

deleted = 0
skipped = 0

for file in BASE.rglob("*_readings.xlsx"):
    try:
        size = file.stat().st_size

        if size <= SIZE_LIMIT:
            print(f"DELETING ({round(size/1024, 2)} KB): {file}")
            file.unlink()
            deleted += 1
        else:
            skipped += 1

    except Exception as e:
        print(f"ERROR processing {file}: {e}")
