from __future__ import annotations
from pathlib import Path
from typing import Optional
import pandas as pd

def load_csv(path: str | Path, nrows: int | None = None) -> pd.DataFrame:
    return pd.read_csv(path, nrows=nrows)
  
assert df.isnull().values.any() == 0
