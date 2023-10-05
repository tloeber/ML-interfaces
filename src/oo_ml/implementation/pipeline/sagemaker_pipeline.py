from oo_ml.interface.estimator.estimator import EstimatorInterface
from oo_ml.interface.pipeline.pipeline import PipelineInterface

class SagemakerPipeline(PipelineInterface):
    def __init__(self, pre_processor, estimator):
        self._pre_processor = pre_processor
        self._estimator = estimator

    def run(self):
        self._pre_processor.run()
        self._estimator.run()

    @property
    def pre_processor(self):
        return self._pre_processor

    @property
    def estimator(self):
        return self._estimator
