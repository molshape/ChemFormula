__all__ = ["ChemFormula"]
from .chemformula import ChemFormula

try:
    from importlib.metadata import version
    __version__ = version("chemformula")
except ImportError:  # pragma: no cover
    __version__ = "unknown"  # pragma: no cover
