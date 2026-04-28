"""Shim sanity test — verify the deprecation re-export works."""
import pytest


def test_shim_imports_with_deprecation_warning():
    with pytest.warns(DeprecationWarning, match="eml-jupyter is deprecated"):
        import eml_jupyter
    assert hasattr(eml_jupyter, "__version__")
    assert eml_jupyter.__version__ == "0.2.0"
