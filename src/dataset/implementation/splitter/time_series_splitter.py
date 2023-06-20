from base_splitter import BaseDataSplitter


class TimeSeriesDataSplitter(BaseDataSplitter):
    def __init__(self, time_identifiers):
        self.time_identifiers = time_identifiers
        super().__init__()

    def _split_data(self):
        # split logic for time series data using self.time_identifiers
        pass
