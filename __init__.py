from .is_number import is_number
from ._version import get_version
from .is_float import is_float

__version__ = _version.get_versions()["version"]
del get_versions
