import abc
from typing import TypeAlias


class InternalRepresentation(TypeAlias):
    pass
StructuredDataSetInternalRepresentation(InternalRepresentation) = pd.DataFrame | np.ndarray



class BaseInternalDataRepresentation(Enum):
    pass

class StructuredDataInternalRepresentation(BaseInternalDataRepresentation):
    PD_DATAFRAME = pd.DataFrame
    NP_ARRAY = np.ndarray
