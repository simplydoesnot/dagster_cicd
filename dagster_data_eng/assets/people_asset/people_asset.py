import pandas as pd
import dagster as dg
from pathlib import Path


@dg.asset
def processed_data():
    df = pd.read_csv(Path(__file__).parent / "../raw_data/sample.csv")

    df["age_group"] = pd.cut(
                df["age"], bins=[0, 20, 40, 100], labels=["Young", "Middle", "Senior"]
    )

    df.to_csv(Path(__file__).parent / "../raw_data/processed_data.csv", index=False)
    return "Data loaded successfully"
