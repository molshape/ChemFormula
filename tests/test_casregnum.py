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


# Tests for functionality


def test_cas_check_digit(caffeine):
    assert caffeine.cas.check_digit == 2


def test_cas_equal(caffeine, theine):
    assert caffeine.cas == theine.cas


def test_cas_lesser_than(l_lacticacid, d_lacticacid):
    assert l_lacticacid.cas < d_lacticacid.cas


def test_cas_format_string(caffeine):
    assert f"{caffeine.cas:0>12}"


# Tests for error handling


def test_cas_invalid_input():
    with pytest.raises(TypeError):
        ChemFormula("H2O", 0, "Water", cas=6417.5)


def test_cas_format_unreadable():
    with pytest.raises(ValueError):
        ChemFormula("H2O", 0, "Water", cas="64 - 17 - 5")


def test_cas_range_error():
    with pytest.raises(ValueError):
        ChemFormula("H2O", 0, "Water", cas=100)


def test_cas_check_digit_error():
    with pytest.raises(ValueError):
        ChemFormula("H2O", 0, "Water", cas="64-17-6")
