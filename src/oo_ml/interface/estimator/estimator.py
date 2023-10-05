# See design_decisions/sklearn_data_loading.ipynb for first draft

from typing import Protocol


class Estimator(Protocol):
    def optimize_hyperparams(self) -> None:
        ...

    def fit(self):
        ...

    def predict(self):
        ...

    @property
    def scorer(self):
        ...
