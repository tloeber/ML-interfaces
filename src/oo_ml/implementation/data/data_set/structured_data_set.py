from oo_ml.interface.data.format import StructuredDataFormat
from oo_ml.implementation.data.data_set.base_data_set import BaseDataset


class StructuredDataSet(BaseDataset):
    def __init__(self, reader, writer):
        super().__init__(reader, writer)

    def from_format(self, format: StructuredDataFormat):
        ds = self.reader.read()

    def to_format(self, format: StructuredDataFormat):
        pass
