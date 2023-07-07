from pathlib import Path

import pandas as pd

from oo_ml.implementation.data.reader.structured_data_reader import \
    CSVReadConfig, CSVReader


csv_read_config = CSVReadConfig(
    data_dir=Path('examples/data'),
)
csv_reader = CSVReader(config=csv_read_config)
df: pd.DataFrame = csv_reader.read(
    target = Path('data.csv')
)
print(df)
