import pytest

from chemformula import ChemFormula

# pytest fixtures


@pytest.fixture
def caffeine():
    return ChemFormula("C8H10N4O2", name="caffeine", cas=58_08_2)


@pytest.fixture
def theine():
    return ChemFormula("(C5N4H)O2(CH3)3", name="theine", cas="58-08-2")


@pytest.fixture
def l_lacticacid():
    return ChemFormula("CH3(CHOH)COOH", 0, "L-lactic acid", cas=79_33_4)


@pytest.fixture
def d_lacticacid():
    return ChemFormula("CH3(CHOH)COOH", 0, "D-lactic acid", cas=10326_41_7)


@pytest.fixture
def hydrocarbons():
    return [
        ChemFormula("C3H5"),
        ChemFormula("C6H12O6"),
        ChemFormula("C6H12O5S"),
        ChemFormula("C3H5O"),
        ChemFormula("C4H5"),
        ChemFormula("C6H12S6"),
        ChemFormula("C6H12S2O3"),
    ]


@pytest.fixture
def hydrocarbons_sorted():
    return [
        ChemFormula("C3H5"),
        ChemFormula("C3H5O"),
        ChemFormula("C4H5"),
        ChemFormula("C6H12S2O3"),
        ChemFormula("C6H12O5S"),
        ChemFormula("C6H12O6"),
        ChemFormula("C6H12S6"),
    ]


# Tests for comparing functionality


def test_for_equal(caffeine, theine):
    assert caffeine == theine


def test_for_unequal(l_lacticacid, d_lacticacid):
    assert l_lacticacid != d_lacticacid


@pytest.mark.parametrize(
    "testinput_left, testinput_right",
    [
        (ChemFormula("Al2O3"), ChemFormula("CO2")),
        (ChemFormula("C2H4"), ChemFormula("C3H4")),
        (ChemFormula("C2H4"), ChemFormula("C2H4O")),
    ],
)
def test_for_lesser_than(testinput_left, testinput_right):
    assert testinput_left < testinput_right


# Test for sorting functionality


def test_for_sorting(hydrocarbons, hydrocarbons_sorted):
    assert sorted(hydrocarbons) == hydrocarbons_sorted
