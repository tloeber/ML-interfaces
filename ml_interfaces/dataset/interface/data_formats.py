import abc
from enum import Enum

class BaseDataFormat(abc.ABCMeta):
    pass

class StructuredDataFormat(BaseDataFormat):
    PARQUET = "parquet"
    CSV = "csv"
    JSONL = "jsonl"
    PD_DATAFRAME = "pd_dataframe"

class SemiStructuredDataFormat(BaseDataFormat):
    JSONL = "jsonl"

class FileFormat(BaseDataFormat):
    PATH = "path"
    PATH_LIST = "path_list"