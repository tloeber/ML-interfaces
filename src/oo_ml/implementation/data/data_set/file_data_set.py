from oo_ml.interface.data.format import FileFormat
from oo_ml.implementation.data.data_set.base_data_set import BaseDataset

class FileDataSet(BaseDataset):
    def from_format(self, format: FileFormat):
        pass

    def to_format(self, format: FileFormat):
        pass
