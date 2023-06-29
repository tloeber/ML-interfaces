from abc import ABC

from oo_ml.interface.data.data_set import BaseDataSetInterface
from oo_ml.implementation.data.reader.base_reader import BaseReader
from oo_ml.implementation.data.writer.base_writer import BaseWriter


class BaseDataset(BaseDataSetInterface, ABC):
    def __init__(
            self,
            reader,
            writer,
    ):
        self.reader: BaseReader = reader
        self.writer: BaseWriter = writer
