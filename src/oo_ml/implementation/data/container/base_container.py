from abc import abstractmethod, ABC

from oo_ml.interface.data.format import BaseDataFormat
from oo_ml.interface.data.container import BaseDataContainerInterface
from oo_ml.implementation.data.splitter.base_splitter import BaseDataSplitter
from oo_ml.implementation.data.reader.base_reader import BaseReader
from oo_ml.implementation.data.writer.base_writer import BaseWriter


class BaseDataContainer(BaseDataContainerInterface, ABC):
    def __init__(
            self,
            splitter: BaseDataSplitter,
    ):
        self.splitter = splitter

    @abstractmethod
    def from_format(self, data_format: BaseDataFormat):
        pass

    @abstractmethod
    def to_format(self, data_format: BaseDataFormat):
        pass

    @abstractmethod
    def get_storage_format(self):
        pass
