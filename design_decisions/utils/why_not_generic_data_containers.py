from abc import abstractmethod, abstractproperty, ABC
from typing import Optional

from pydantic import BaseModel
import torch
from torch.nn import functional as F

from lightning.pytorch import LightningModule


class Backbone(torch.nn.Module):
    """
    >>> Backbone()  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Backbone(
      (l1): Linear(...)
      (l2): Linear(...)
    )
    """

    def __init__(self, hidden_dim=128):
        super().__init__()
        self.l1 = torch.nn.Linear(28 * 28, hidden_dim)
        self.l2 = torch.nn.Linear(hidden_dim, 10)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = torch.relu(self.l1(x))
        return torch.relu(self.l2(x))


class LitClassifier(LightningModule):
    """
    >>> LitClassifier(Backbone())  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    LitClassifier(
      (backbone): ...
    )
    """

    def __init__(
        self, backbone: Optional[Backbone] = None, learning_rate: float = 0.0001
    ):
        super().__init__()
        self.save_hyperparameters(ignore=["backbone"])
        if backbone is None:
            backbone = Backbone()
        self.backbone = backbone

    def forward(self, x):
        # use forward for inference/predictions
        return self.backbone(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y)
        self.log("train_loss", loss, on_epoch=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y)
        self.log("valid_loss", loss, on_step=True)

    def test_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.cross_entropy(y_hat, y)
        self.log("test_loss", loss)

    def predict_step(self, batch, batch_idx, dataloader_idx=None):
        x, y = batch
        return self(x)

    def configure_optimizers(self):
        # self.hparams available because we called self.save_hyperparameters()
        return torch.optim.Adam(self.parameters(), lr=self.hparams.learning_rate)


# OO_ML details
# =============


class DataSetInterface(ABC):
    """
    This serves as the *abstract* type under which all the concrete dataset
    interfaces fall. We can use when we want to depend only on the data set
    abstraction, but not the concrete type of data set.

    At the moment, this interface does not yet defined any shared behavior,
    so it would also be possible to use virtual subclasses (e.g., registering)
    instead. However, we want to keep the option open for the future to define
    shared behavior that all the concrete dataset interfaces must implement.
    """

    pass


class EstimatorInterface(ABC):
    @abstractmethod
    def fit(self):
        pass


class ModelConfig(BaseModel):
    batch_size: int
    fast_dev_run: bool = False
