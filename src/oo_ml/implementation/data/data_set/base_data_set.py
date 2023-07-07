from abc import ABC

from oo_ml.interface.data.data_set import DataSetType
from oo_ml.implementation.data.reader.base_reader import BaseReader
from oo_ml.implementation.data.writer.base_writer import BaseWriter


class BaseDataset(DataSetType, ABC):
    def __init__(
            self,
            reader,
            writer,
    ):
        self.reader: BaseReader = reader
        self.writer: BaseWriter = writer
