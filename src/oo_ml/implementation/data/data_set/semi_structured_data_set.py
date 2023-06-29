from oo_ml.interface.data.format import SemiStructuredDataFormat
from oo_ml.implementation.data.data_set.base_data_set import BaseDataset


class SemiStructuredDataSet(BaseDataset):
    def from_format(self, format: SemiStructuredDataFormat):
        pass

    def to_format(self, format: SemiStructuredDataFormat):
        pass
