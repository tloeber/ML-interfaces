from oo_ml.interface.data.format import FileFormat
from oo_ml.implementation.data.dataset.base_dataset import BaseDataset

class FileDataSet(BaseDataset):
    def from_format(self, format: FileFormat):
        pass

    def to_format(self, format: FileFormat):
        pass
