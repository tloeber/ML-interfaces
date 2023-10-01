from abc import ABC, abstractmethod
from typing import TypeVar, Generic, NewType, Any

from oo_ml.interface.data.data_set_type import DataSetType, StructuredData


T = TypeVar("T")


class InMemoryFormat(ABC):
    pass


class StructuredInMemoryFormat(InMemoryFormat):
    pass

# class InMemoryFormatName(Generic[DataSetType]):
#     pass

# # StructuredInMemoryRepresenation = InMemoryFormat[StructuredData]
# class StructuredInMemoryFormat(InMemoryFormat[StructuredData]):
#     pass
