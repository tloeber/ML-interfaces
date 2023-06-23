from  ml_interfaces import interface
from ml_interfaces import implementation
# .interface.data_container import BaseDataContainerInterface
# import ml_interfaces.interface.data_formats
# from ml_interfaces.implementation.splitter.base_splitter import BaseDataSplitter
# from ml_interfaces.data_reader import BaseDataReader
# from ml_interfaces.implementation.data_writer import BaseDataWriter

class BaseDataContainer(BaseDataContainerInterface):
    def __init__(
            self,
            splitter: interface.data_set.splitter.BaseDataSplitter,
            reader: BaseDataReader,
            writer: BaseDataWriter
    ):
        self.splitter = splitter
        self.reader = reader
        self.writer = writer

    def from_format(self, format: data_formats.BaseDataFormat):
        pass

    def to_format(self, format: data_formats.BaseDataFormat):
        pass

    def get_storage_format(self):
        pass

    def persist(self):
        pass
