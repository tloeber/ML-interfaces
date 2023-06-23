from ..interfaces.data_sets import SemiStructuredDataInterface, FileDataInterface
from ..interfaces.data_formats import SemiStructuredDataFormat, FileFormat


class SemiStructuredDataSet(SemiStructuredDataInterface):
    def from_format(self, format: SemiStructuredDataFormat):
        pass

    def to_format(self, format: SemiStructuredDataFormat):
        pass
