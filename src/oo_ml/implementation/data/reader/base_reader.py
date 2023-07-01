from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from pathlib import Path

from oo_ml.interface.data.data_set import DataSetType, StructuredData


class BaseReader(ABC, Generic[DataSetType]):
    @abstractmethod
    def read(self, path: Path) -> DataSetType.ValidInternalRepresentation:
        pass

StructuredDataReader = BaseReader[StructuredData]
