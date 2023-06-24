from oo_ml.interface.data.format import StructuredDataFormat
from oo_ml.interface.data.dataset import StructuredDataInterface


class StructuredDataSet(StructuredDataInterface):
    def from_format(self, format: StructuredDataFormat):
        pass

    def to_format(self, format: StructuredDataFormat):
        pass
