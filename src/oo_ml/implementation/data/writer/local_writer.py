import pandas as pd
import json

from oo_ml.implementation.data.writer.base_writer import BaseWriter


class CSVWriter(BaseWriter):
    def write(self, data: pd.DataFrame, path) -> None:
        data.to_csv(path, index=False)


class JSONWriter(BaseWriter):
    def write(self, data: pd.DataFrame | dict, path) -> None:
        with open(path, 'w') as f:
            json.dump(data, f)
