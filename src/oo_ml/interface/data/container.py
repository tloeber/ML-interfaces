import abc

from oo_ml.interface.data.dataset import BaseDataSetInterface


class BaseDataContainerInterface(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def from_subsets(
        cls,
        train_data: BaseDataSetInterface,
        test_data: BaseDataSetInterface,
        validation_data: BaseDataSetInterface,
    ):
        pass

    @classmethod
    @abc.abstractmethod
    def from_complete_set(
        cls,
        all_data: BaseDataSetInterface,
    ):
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
