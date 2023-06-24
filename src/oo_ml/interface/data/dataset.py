import abc

from oo_ml.interface.data import format as data_formats  # Avoid name clash

class BaseDataSetInterface(abc.ABC):
    @abc.abstractmethod
    def from_format(self, data_format: data_formats.BaseDataFormat):
        pass

    @abc.abstractmethod
    def to_format(self, data_format: data_formats.BaseDataFormat):
        pass

    @abc.abstractmethod
    def get_storage_format(self):
        pass

    @abc.abstractmethod
    def persist(self):
        pass

class StructuredDataInterface(BaseDataSetInterface):
    @abc.abstractmethod
    def from_format(self, data_format: data_formats.StructuredDataFormat):
        pass

    @abc.abstractmethod
    def to_format(self, data_format: data_formats.StructuredDataFormat):
        pass

class SemiStructuredDataInterface(BaseDataSetInterface):
    @abc.abstractmethod
    def from_format(self, data_format: data_formats.SemiStructuredDataFormat):
        pass

    @abc.abstractmethod
    def to_format(self, data_format: data_formats.SemiStructuredDataFormat):
        pass

class FileDataInterface(BaseDataSetInterface):
    @abc.abstractmethod
    def from_format(self, data_format: data_formats.FileFormat):
        pass

    @abc.abstractmethod
    def to_format(self, data_format: data_formats.FileFormat):
        pass
