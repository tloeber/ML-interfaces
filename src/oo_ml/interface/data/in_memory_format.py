import abc
from typing import TypeVar, Generic

from oo_ml.interface.data.data_set_type import DataSetType, StructuredData


class InMemoryFormat(Generic[DataSetType]):
    pass

class InMemoryFormatName(Generic[DataSetType]):
    pass

StructuredInMemoryRepresenation = InMemoryFormat[StructuredData]
