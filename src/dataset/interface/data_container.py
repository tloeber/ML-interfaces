import abc
from data_set import BaseDataSetInterface

class BaseDataContainerInterface(abc.ABC):
    @abc.abstractmethod
    def from_subsets(self):
        pass

    @abc.abstractmethod
    def from_complete_set(self):
        pass

    @abc.abstractmethod
    def get_train_data(self) -> BaseDataSetInterface:
        pass

    @abc.abstractmethod
    def get_test_data(self) -> BaseDataSetInterface:
        pass

    @abc.abstractmethod
    def get_validation_data(self) -> BaseDataSetInterface:
        pass

    @abc.abstractmethod
    def get_all_data(self) -> BaseDataSetInterface:
        pass
