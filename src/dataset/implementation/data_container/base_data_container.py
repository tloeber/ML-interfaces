from ..interfaces.data_container import BaseDataContainerInterface
from ..interfaces.data_formats import BaseDataFormat
from .utils.data_splitter import BaseDataSplitter
from .utils.data_reader import BaseDataReader
from .utils.data_writer import BaseDataWriter

class BaseDataContainer(BaseDataContainerInterface):
    def __init__(self, splitter: BaseDataSplitter, reader: BaseDataReader, writer: BaseDataWriter):
        self.splitter = splitter
        self.reader = reader
        self.writer = writer

    def from_format(self, format: BaseDataFormat):
        pass

    def to_format(self, format: BaseDataFormat):
        pass

    def get_storage_format(self):
        pass

    def persist(self):
        pass
