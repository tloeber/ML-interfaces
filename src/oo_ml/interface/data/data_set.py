import abc
from typing import Any

from oo_ml.interface.data.format import BaseDataFormat
from oo_ml.interface.data.reader import Reader
from oo_ml.interface.data.data_set_type import DataSetType


class DataSetInterface(abc.ABC):
    @abc.abstractmethod
    def __init__(self, writer):
        pass

    @abc.abstractmethod
    def to_format(self, data_format: BaseDataFormat):
        pass

    @abc.abstractmethod
    def get_internal_format(self) -> BaseDataFormat:
        """
        Tells us which of the valid internal formats is actually used to store
        the data internally.
        """
        pass

    @abc.abstractmethod
    def write(self, target: Any = None) -> None:
        pass
