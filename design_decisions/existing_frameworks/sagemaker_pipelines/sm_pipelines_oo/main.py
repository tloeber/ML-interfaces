from loguru import logger
from typing import Literal
from pydantic_settings import BaseSettings
from pathlib import Path

from sagemaker.workflow.pipeline import Pipeline
from sagemaker.sklearn.processing import SKLearnProcessor

from sm_pipelines_oo.pipeline_config import SharedConfig
from sm_pipelines_oo.steps.pre_processing import StepFactory, ProcessingStepFactory
from sm_pipelines_oo.steps.model_training import train_step
# from sm_pipelines_oo.steps.model_evaluation import eval_step
# from sm_pipelines_oo.steps.model_registration import condition_step

from sm_pipelines_oo.utils import load_pydantic_config_from_file
from sm_pipelines_oo.pipeline_config import BootstrapConfig, SharedConfig, Environment
from sm_pipelines_oo.pipeline_wrapper import AWSConnector, PipelineWrapper


# Load configs
# ============
# Todo: Pipeline (Wrapper?) object should take config directory as an init argument and be able to
# load config itself, so that we don't have to do this here.
ENVIRONMENT: Environment = BootstrapConfig().ENVIRONMENT  # type: ignore

config_path_shared = f"configs/{ENVIRONMENT}/.env_shared"
config_path_pre_processing = Path(f"configs/{ENVIRONMENT}/.env_pre_process")

# todo: fixed type problem by making load_p... generic. Potentially think about making it a decorator instead?
shared_config: SharedConfig = load_pydantic_config_from_file(  # type: ignore
    config_cls=SharedConfig,
    config_path=config_path_shared,
)

# Create AWS Connector
# ====================
aws_connector = AWSConnector(
    environment=ENVIRONMENT,
    shared_config=shared_config,
)

# Create Step Factories
# =====================
pre_processing_step_factory = ProcessingStepFactory(
    processor_cls=SKLearnProcessor,
    step_config_path=config_path_pre_processing,
    aws_connector=aws_connector,
)


# Create Pipeline
# ===============
pipeline = PipelineWrapper(
    step_factories=[
        pre_processing_step_factory,
    ],
    environment=ENVIRONMENT,
    shared_config=shared_config,
    aws_connector=aws_connector,
)
