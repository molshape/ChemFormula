import pytest

import chemformula.config
from chemformula import ChemFormula, elements

# Tests for functionality

@pytest.fixture(autouse=True, scope="module")
def enable_hydrogen_isotopes():
    chemformula.config.AllowHydrogenIsotopes = True


def test_get_valid_element_symbols_with_hydrogen_isotopes():
    allowed_symbols = elements.get_valid_element_symbols()
    assert "D" in allowed_symbols and "T" in allowed_symbols


@pytest.mark.parametrize(
    "testinput, expected",
    [
        ("H2O", False),
        ("D2O", True),
        ("NH4ClO4", False),
        ("NH4TcO4", True),
    ],
)
def test_contains_isotopes(testinput, expected):
    assert ChemFormula(testinput).contains_isotopes is expected


@pytest.mark.parametrize(
    "testinput, expected",
    [
        ("H2O", 18.02),
        ("D2O", 20.03),
    ],
)
def test_formula_weight_hydrogen_isotopes(testinput, expected):
    assert round(ChemFormula(testinput).formula_weight, 2) == expected


@pytest.mark.parametrize(
    "testinput, expected",
    [
        ("H2O", False),
        ("D2O", False),
        ("T2O", True),
    ],
)
def test_is_radioactive_isotopes(testinput, expected):
    assert ChemFormula(testinput).is_radioactive is expected
    assert ChemFormula(testinput).radioactive is expected  # `radioactive` is deprecated, use `is_radioactive` instead
