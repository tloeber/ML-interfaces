from ..interfaces.data_sets import StructuredDataInterface
from ..interfaces.data_formats import StructuredDataFormat

class StructuredDataSet(StructuredDataInterface):
    def from_format(self, format: StructuredDataFormat):
        pass

    def to_format(self, format: StructuredDataFormat):
        pass
