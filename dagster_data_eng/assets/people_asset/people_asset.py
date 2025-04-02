import pandas as pd
import dagster as dg
from pathlib import Path


@dg.asset
def processed_data():
    file_path = Path(__file__).parent / "../raw_data/sample.csv"
    df = pd.read_csv(file_path)

    df["age_group"] = pd.cut(
        df["age"], bins=[0, 20, 40, 100], labels=["Young", "Middle", "Senior"]
    )
    dest_path = Path(__file__).parent / "../raw_data/processed_data.csv"
    df.to_csv(dest_path, index=False)
    return "Data loaded successfully"
