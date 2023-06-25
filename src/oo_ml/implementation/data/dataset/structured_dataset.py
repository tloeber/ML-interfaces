from oo_ml.interface.data.format import StructuredDataFormat
from oo_ml.implementation.data.dataset.base_dataset import BaseDataset


class StructuredDataSet(BaseDataset):
    def from_format(self, format: StructuredDataFormat):
        pass

    def to_format(self, format: StructuredDataFormat):
        pass
