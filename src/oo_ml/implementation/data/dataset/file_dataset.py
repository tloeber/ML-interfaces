from oo_ml.interface.data.format import FileFormat
from oo_ml.interface.data.dataset import FileDataInterface

class FileDataSet(FileDataInterface):
    def from_format(self, format: FileFormat):
        pass

    def to_format(self, format: FileFormat):
        pass
