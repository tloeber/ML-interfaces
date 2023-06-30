from typing import TypeVar


class StructuredData:
    pass

class SemiStructuredData:
    pass

class ImageData:
    pass


DataSetType = TypeVar(
    'DataSetType',
    StructuredData, SemiStructuredData, ImageData,
    covariant=True
)
