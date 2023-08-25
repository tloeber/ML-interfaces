from abc import ABC
from enum import Enum

import pandas as pd
import numpy as np


# Common supertype for all data formats
# =====================================
class BaseDataFormat(ABC):
    """
    This class provides a supertype for all the concrete data formats. We don't
    use any direct inheritance since they don't need to share any attributes or
    methods. Instead, we simply register each concrete data formats (implemented
    as Enums) after creation.
    """

    pass


# Structured data
# ===============
class StructuredDataFormat(Enum):
    PD_DATAFRAME = pd.DataFrame
    NP_ARRAY = np.ndarray
    # PARQUET = "parquet"
    # JSONL = "jsonl"


BaseDataFormat.register(StructuredDataFormat)


# Semi-structured data
# ====================
class SemiStructuredDataFormat(Enum):
    JSONL = "jsonl"


BaseDataFormat.register(SemiStructuredDataFormat)


# File data
# =========
class FileFormat(Enum):
    PATH = "path"
    PATH_LIST = "path_list"


BaseDataFormat.register(FileFormat)
