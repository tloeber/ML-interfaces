from abc import ABC, abstractmethod
from typing import Generic, Any

from oo_ml.interface.data.data_set_type import DataSetType
from oo_ml.interface.data.in_memory_format import InMemoryFormat
    # StructuredData, SemiStructuredData, ImageData


# Lower-level details
# ===================

class ReadConfig(ABC):
    """
    This class simply provides a container that will hold all information needed
    to read from a datasource, e.g. database url, a way to authenticate, data
    schema, any read options options, etc.
    Since this varies greatly between different datasources, this abstract class
    does not provide any specific details for the specific configs. Its purpose
    is rather to provide a supertype.

    Note that the config does not provide the information to read a specific
    dataset instance. This is because each Reader instance will "have a"
    ReadConfig, and we want to be able to read multiple datasets with a given
    reader (e.g., if we create a DataContainer from pre-split data, and thus
    have to read each subset separately).
    Instead, the specific dataset to read is specified in the `read` method by
    the `target` parameter. Note that it is of type `Any`, but concrete
    implementations of the Reader should specify a more precise type. (It may
    either by an inbuilt type such as pathlib.Path, a NewType such as
    NewType(SQLQuery, str), or a custom class to hold more complex information.)
    """


# Generic Reader
# ==============

class ReaderInterface(ABC, Generic[DataSetType]):
    @abstractmethod
    def __init__(self, config: ReadConfig):
        pass

    @abstractmethod
    def read(self, target: Any) -> InMemoryFormat[DataSetType]:
        """
        :param target: Identifier of a concrete dataset (given a datasource and
            other options defined in ReadConfig).
        """
        pass


# Readers for a specific kind of data. These are what the user will implement.
# ============================================================================

# StructuredDataReader = Reader[StructuredData]
# SemiStructuredDataReader = Reader[SemiStructuredData]
# ImageDataReader = Reader[ImageData]
