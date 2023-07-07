from abc import abstractmethod, ABC
from typing import Any, TypeAlias, TypeVar, Generic

import pandas as pd
import numpy as np

from oo_ml.interface.data.format import DataFormat
from oo_ml.interface.data.in_memory_format import InMemoryFormat, \
    InMemoryFormatName
# from oo_ml.interface.data.reader import ReaderInterface
from oo_ml.interface.data.data_set_type import DataSetType


class DataSetInterface(ABC, Generic[DataSetType]):
    @abstractmethod
    def __init__(self, in_memory_data: InMemoryFormat[DataSetType]):
        pass

    @abstractmethod
    def to_format(self, data_format: InMemoryFormatName) -> InMemoryFormat[DataSetType]:
        pass

    @abstractmethod
    def get_internal_format(self) -> InMemoryFormatName[DataSetType]:
        """
        Tells us which of the valid internal formats is actually used to store
        the data internally.
        """
        pass

    @abstractmethod
    def write(self, target: Any = None) -> None:
        pass
