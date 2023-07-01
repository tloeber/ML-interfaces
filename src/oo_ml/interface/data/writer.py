from abc import ABC, abstractmethod
from typing import Generic, Any

from oo_ml.interface.data.data_set_type import DataSetType
    # StructuredData, SemiStructuredData, ImageData


# Lower-level details
# ===================

class WriterConfig(ABC):
    """
    This class simply provides a container that will hold all information needed
    to write to a datasource, e.g. database url, a way to authenticate, any
    write options options, etc.
    Since this varies greatly between different datasources, this abstract class
    does not provide any specific details for the specific configs. Its purpose
    is rather to provide a supertype.

    Note that the config does not provide the information to write a specific
    dataset instance. This is because each Writer instance will "have a"
    WriteConfig, and we want to be able to write multiple datasets with a given
    writer (e.g., at different stages after applying transforms).
    Instead, the specific disk output is specified in the `write` method by
    the `target` parameter. Note that it is of type `Any`, but concrete
    implementations of the Reader should specify a more precise type. (It may
    either by an inbuilt type such as pathlib.Path, a NewType such as
    NewType(SQLQuery, str), or a custom class to hold more complex information.)
    """


# Generic Reader
# ==============

class WriterInterface(ABC, Generic[DataSetType]):
    @abstractmethod
    def __init__(self, config: WriterConfig):
        pass

    @abstractmethod
    def write(self, target: Any) -> None:
        """
        :param target: Identifier of a concrete write location (given a
            datasource and other options defined in WriteConfig).
        """
        pass
