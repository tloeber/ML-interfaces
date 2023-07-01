import pathlib

import pandas as pd

from oo_ml.implementation.data.reader.structured_data_reader import \
    CSVReadConfig, CSVReader

csv_read_config = CSVReadConfig(
    data_dir=pathlib.Path('examples/data'),
)
csv_reader = CSVReader(config=csv_read_config)
df: pd.DataFrame = csv_reader.read(
    target = pathlib.Path('data.csv')
)
print(df)
