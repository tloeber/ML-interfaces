from ..interfaces.data_sets import SemiStructuredDataInterface, FileDataInterface
from ..interfaces.data_formats import SemiStructuredDataFormat, FileFormat


class FileDataSet(FileDataInterface):
    def from_format(self, format: FileFormat):
        pass

    def to_format(self, format: FileFormat):
        pass
