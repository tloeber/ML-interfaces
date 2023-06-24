from oo_ml.interface.data.format import SemiStructuredDataFormat
from oo_ml.interface.data.dataset import SemiStructuredDataInterface


class SemiStructuredDataSet(SemiStructuredDataInterface):
    def from_format(self, format: SemiStructuredDataFormat):
        pass

    def to_format(self, format: SemiStructuredDataFormat):
        pass
