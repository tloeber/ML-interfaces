from typing import Protocol


class PipelineInterface(Protocol):
    def run(self) -> None:
        ...

    @property
    def pre_processor(self):
        ...

    @property
    def estimator(self):
        ...
