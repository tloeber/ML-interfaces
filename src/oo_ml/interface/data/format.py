from enum import Enum
from typing import Generic, TypeAlias

import pandas as pd
import numpy as np


# class BaseDataFormat(Enum):
#     """
#     The fact that this enum does not have any attributes/members makes it
#     abstract, since it is thus not possible to instantiate it.
#     While more direct ways of designating this class as an abstractclass, e.g.
#     using abc.ABC or abc.abstractmethod would be preferable, this doesn't seem
#     easily possible due to some differences between enums and standard classes.
#     See for example the following discussion: https://stackoverflow.com/questions/56131308/create-an-abstract-enum-class
#     """
#     pass

# class StructuredDataFormat(BaseDataFormat):
#     PD_DATAFRAME = pd.DataFrame
#     NP_ARRAY = np.ndarray
#     # PARQUET = "parquet"
#     # JSONL = "jsonl"

# class SemiStructuredDataFormat(BaseDataFormat):
#     JSONL = "jsonl"

# class FileFormat(BaseDataFormat):
#     PATH = "path"
#     PATH_LIST = "path_list"

# StructuredDataFormat: TypeAlias = pd.DataFrame | np.ndarray
# SemiStructuredDataFormat: TypeAlias = list[dict]


from oo_ml.interface.data.data_set_type import DataSetType, StructuredData

class DataFormat(Generic[DataSetType]):
    pass

StructuredDataFormat = DataFormat[StructuredData]
