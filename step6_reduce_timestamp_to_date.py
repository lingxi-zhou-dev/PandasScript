import pandas as pd

files = [
    "ketone_before_11am.csv",
    "dbr_before_11am.csv",
    "glucose_before_11am.csv"
]

for file in files:
    df = pd.read_csv(file)

    # Convert to datetime row-by-row to avoid timezone issues
    df["reading_date"] = df["reading_timestamp"].apply(
        lambda x: pd.to_datetime(x, errors="coerce").date() if pd.notnull(x) else None
    )

    # Drop old timestamp column
    df = df.drop(columns=["reading_timestamp"])

    # Reorder columns nicely
    df = df[["first_name", "last_name", "reading_date", "reading_value"]]

    # Save back to same file
    df.to_csv(file, index=False)
