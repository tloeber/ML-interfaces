from base_splitter import BaseDataSplitter


class SpatialDataSplitter(BaseDataSplitter):
    def __init__(self, coordinate_identifiers):
        self.coordinate_identifiers = coordinate_identifiers
        super().__init__()

    def _split_data(self):
        # split logic for spatial data using self.coordinate_identifiers
        pass

class PreSplitDataSplitter(BaseDataSplitter):
    def __init__(self, training_set, validation_set, test_set):
        self.training_set = training_set
        self.validation_set = validation_set
        self.test_set = test_set
        super().__init__()

    def _split_data(self):
        raise NotImplementedError("Data is already pre-split.")

    def combine_data(self):
        # logic to combine self.training_set, self.validation_set, and self.test_set
        pass
