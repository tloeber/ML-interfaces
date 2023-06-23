import pandas as pd
import json

from ml_interfaces.interface.writer import base_writer

class CSVWriter(base_writer.BaseWriter):
    def write(self, data: pd.DataFrame, path) -> None:
        data.to_csv(path, index=False)


class JSONWriter( base_writer.BaseWriter):
    def write(self, data: pd.DataFrame | dict, path) -> None:
        with open(path, 'w') as f:
            json.dump(data, f)
