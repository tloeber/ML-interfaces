from oo_ml.implementation.data.splitter.base_splitter import BaseDataSplitter


class ClusteredDataSplitter(BaseDataSplitter):
    def __init__(self, cluster_identifiers):
        self.cluster_identifiers = cluster_identifiers
        super().__init__()

    def _split_data(self):
        # split logic for clustered data using self.cluster_identifiers
        pass
