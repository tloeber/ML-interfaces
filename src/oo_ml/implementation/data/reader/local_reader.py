import pathlib
import json

import pandas as pd

from oo_ml.implementation.data.reader.base_reader import BaseReader


class CSVReader(BaseReader):
    def read(self, path: pathlib.Path) -> pd.DataFrame:
        return pd.read_csv(path)


class JSONReader(BaseReader):
    def read(self, path: pathlib.Path) -> dict:
        with open(path, 'r') as f:
            data = json.load(f)
        return data
