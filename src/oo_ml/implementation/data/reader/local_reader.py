import pathlib
import json

import pandas as pd

from ml_interfaces.interface.reader import base_reader


class CSVReader(base_reader.BaseReader):
    def read(self, path: pathlib.Path) -> pd.DataFrame:
        return pd.read_csv(path)


class JSONReader(base_reader.BaseReader):
    def read(self, path: pathlib.Path) -> dict:
        with open(path, 'r') as f:
            data = json.load(f)
        return data
