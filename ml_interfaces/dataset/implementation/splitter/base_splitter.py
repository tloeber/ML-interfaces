class BaseDataSplitter:
    def __init__(self, test_proportion=0.2, validation_proportion=0.2):
        self.test_proportion = test_proportion
        self.validation_proportion = validation_proportion

    def _split_data(self):
        pass

    def get_train_data(self):
        pass

    def get_test_data(self):
        pass

    def get_validation_data(self):
        pass
