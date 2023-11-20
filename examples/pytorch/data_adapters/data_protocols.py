from abc import abstractmethod, ABC
import typing
from typing import Callable, Iterator, Any, Protocol, TypeAlias
import torch

from torch.utils.data import Dataset as TorchDataset


class DataSetProtocol(Protocol):
    pass


class TorchMapDatasetProtocol(typing.Iterable, typing.Sized, Protocol):
    """
    Implements protocol for PyTorch's map-style dataset as described here:
    https://pytorch.org/docs/stable/data.html#map-style-datasets
    """

    def __len__(self) -> int:
        ...

    def __getitem__(self, index) -> tuple[torch.Tensor, Any]:
        ...


class TorchIterableDatasetProtocol(typing.Protocol):
    """
    Implements protocol for PyTorch's iterable-style dataset as described here:
    https://pytorch.org/docs/stable/data.html#iterable-style-datasets
    """

    def __iter__(self) -> tuple[torch.Tensor, Any]:
        ...


TorchDatasetType: TypeAlias = TorchMapDatasetProtocol | TorchIterableDatasetProtocol
