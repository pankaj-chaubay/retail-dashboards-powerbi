"""
Turns the two source files used in the Tableau assignments into clean UTF-8 CSVs
with ISO dates, so Power Query reads them the same way on any machine and locale.

  raw/Retail_Customer_Behavior1.csv  -> data/retail_customer_behavior.csv
  raw/Sample - Superstore.csv        -> data/superstore_sales.csv

Run from the repository root:  python prep/prepare_data.py raw_folder
"""
import sys
from pathlib import Path

import pandas as pd

raw = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("raw")
out = Path(__file__).resolve().parents[1] / "data"
out.mkdir(exist_ok=True)

r = pd.read_csv(raw / "Retail_Customer_Behavior1.csv")
r["Purchase_Date"] = pd.to_datetime(r["Purchase_Date"], format="%d-%m-%Y").dt.strftime("%Y-%m-%d")
r.to_csv(out / "retail_customer_behavior.csv", index=False, encoding="utf-8")

s = pd.read_csv(raw / "Sample - Superstore.csv", encoding="latin-1")
for c in ["Order Date", "Ship Date"]:
    s[c] = pd.to_datetime(s[c], format="%m/%d/%Y").dt.strftime("%Y-%m-%d")
s.to_csv(out / "superstore_sales.csv", index=False, encoding="utf-8")

print(f"retail: {len(r):,} rows, superstore: {len(s):,} rows")
