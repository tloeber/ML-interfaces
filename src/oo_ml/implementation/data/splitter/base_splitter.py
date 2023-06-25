from abc import abstractmethod, ABC


class BaseDataSplitter(ABC):
    def __init__(self, test_proportion=0.2, validation_proportion=0.2):
        self.test_proportion = test_proportion
        self.validation_proportion = validation_proportion

    @abstractmethod
    def _split_data(self):
        pass

    @abstractmethod
    def get_train_data(self):
        pass

    @abstractmethod
    def get_test_data(self):
        pass

    @abstractmethod
    def get_validation_data(self):
        pass
