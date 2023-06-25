from enum import Enum


class BaseDataFormat(Enum):
    """
    The fact that this enum does not have any attributes/members makes it
    abstract, since it is thus not possible to instantiate it.
    While more direct ways of designating this class as an abstractclass, e.g.
    using abc.ABC or abc.abstractmethod would be preferable, this doesn't seem
    easily possible due to some differences between enums and standard classes.
    See for example the following discussion: https://stackoverflow.com/questions/56131308/create-an-abstract-enum-class
    """
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
