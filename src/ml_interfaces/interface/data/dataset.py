import abc
from .data_formats import BaseDataFormat, StructuredDataFormat, \
    SemiStructuredDataFormat, FileFormat

class BaseDataSetInterface(abc.ABC):
    @abc.abstractmethod
    def from_format(self, format: BaseDataFormat):
        pass

    @abc.abstractmethod
    def to_format(self, format: BaseDataFormat):
        pass

    @abc.abstractmethod
    def get_storage_format(self):
        pass

    @abc.abstractmethod
    def persist(self):
        pass

class StructuredDataInterface(BaseDataSetInterface):
    @abc.abstractmethod
    def from_format(self, format: StructuredDataFormat):
        pass

    @abc.abstractmethod
    def to_format(self, format: StructuredDataFormat):
        pass

class SemiStructuredDataInterface(BaseDataSetInterface):
    @abc.abstractmethod
    def from_format(self, format: SemiStructuredDataFormat):
        pass

    @abc.abstractmethod
    def to_format(self, format: SemiStructuredDataFormat):
        pass

class FileDataInterface(BaseDataSetInterface):
    @abc.abstractmethod
    def from_format(self, format: FileFormat):
        pass

    @abc.abstractmethod
    def to_format(self, format: FileFormat):
        pass
