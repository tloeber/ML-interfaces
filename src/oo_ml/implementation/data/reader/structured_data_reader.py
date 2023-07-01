
import pathlib
import json
from typing import Any

import pandas as pd

from oo_ml.interface.data.reader import ReadConfig, ReaderInterface
from oo_ml.interface.data.data_set_type import StructuredData

class CSVReadConfig(ReadConfig):
    def __init__(self, data_dir: pathlib.Path, options: dict[str, Any] = {}):
        self.data_dir = data_dir
        self.options = options
        # self.sep = sep

class CSVReader(ReaderInterface[StructuredData]):
    def __init__(self, config: CSVReadConfig):
        self.config = config

    def read(self, target: pathlib.Path) -> pd.DataFrame:
        file_path: pathlib.Path = self.config.data_dir / target
        return pd.read_csv(file_path, **self.config.options)
