import pytest
from chemformula import ChemFormula


### pytest fixtures

@pytest.fixture
def muscarine():
    return ChemFormula("((CH3)3N)(C6H11O2)", charge = 1, name = u"ʟ-(+)-Muscarine", cas = 300_54_9)


### Tests for functionality

@pytest.mark.parametrize(
    "testinput, expected", [
        (ChemFormula("H2O", 0, "Water"),
        "Water"),
        (ChemFormula("((CH3)3N)(C6H11O2)", charge = 1, name = u"ʟ-(+)-Muscarine"),
        u"ʟ-(+)-Muscarine"),
        ],
)
def test_name(testinput, expected):
    assert testinput.name == expected

@pytest.mark.parametrize(
    "testinput, expected", [
        (ChemFormula("H2O", 0),
        0),
        (ChemFormula("SO4", charge = -2),
        -2),
        (ChemFormula("Al", charge = 3),
        3)
        ],
)
def test_charge(testinput, expected):
    assert testinput.charge == expected

@pytest.mark.parametrize(
    "testinput, expected", [
        (ChemFormula("H2O"),
        False),
        (ChemFormula("H3O", charge = 1),
        True),
        (ChemFormula("OH", charge = -1),
        True)
        ],
)
def test_charged(testinput, expected):
    assert testinput.charged is expected

@pytest.mark.parametrize(
    "testinput, expected", [
        (ChemFormula("UO2"),
        True),
        (ChemFormula("SO2"),
        False)
        ],
)
def test_radioactive(testinput, expected):
    assert testinput.radioactive is expected

@pytest.mark.parametrize(
    "testinput, expected", [
        (ChemFormula("((CH3)3N)(C6H11O2)", 1, "L-(+)-Muscarine", 300_54_9),
        "300-54-9"),
        (ChemFormula("C8H10N4O2", 0, "coffein", "58-08-2"),
        "58-08-2"),
        (ChemFormula("(C5N4H)O2(CH3)3", name = "theine", cas = 58082),
        "58-08-2")
        ],
)
def test_cas(testinput, expected):
    assert str(testinput.cas) == expected

@pytest.mark.parametrize(
    "testinput, expected", [
        (ChemFormula("((CH3)3N)(C6H11O2)"),
        174.26),
        (ChemFormula("C8H10N4O2"),
        194.19),
        (ChemFormula("H3O", 1),
        19.02)
        ],
)
def test_formula_weight(testinput, expected):
    assert round(testinput.formula_weight, 2) == expected

@pytest.mark.parametrize(
    "testinput, testelement, expected", [
        (ChemFormula("((CH3)3N)(C6H11O2)"), "C",
        62.03),
        (ChemFormula("C8H10N4O2"), "N",
        28.85),
        (ChemFormula("SO4", -2), "S",
        33.38)
        ],
)
def test_weight_fraction(testinput, testelement, expected):
    assert round(testinput.mass_fraction[testelement]*100, 2) == expected

@pytest.mark.parametrize(
    "testinput, testelement, expected", [
        (ChemFormula("((CH3)3N)(C6H11O2)"), "H",
        20),
        (ChemFormula("C8H10N4O2"), "N",
        4),
        (ChemFormula("SO4", -2), "O",
        4)
        ],
)
def test_element_dictionary(testinput, testelement, expected):
    assert testinput.element[testelement] == expected


### Tests for output functionality

def test_html(muscarine):
    assert muscarine.html == "<span class='ChemFormula'>((CH<sub>3</sub>)<sub>3</sub>N)(C<sub>6</sub>H<sub>11</sub>O<sub>2</sub>)<sup>+</sup></span>"

def test_latex(muscarine):
    assert muscarine.latex == r"\(\(\textnormal{C}\textnormal{H}_{3}\)_{3}\textnormal{N}\)\(\textnormal{C}_{6}\textnormal{H}_{11}\textnormal{O}_{2}\)^{+}"

def test_sum_formula_unicode(muscarine):
    assert muscarine.sum_formula.unicode == u"C₉H₂₀NO₂⁺"

def test_hill_formula_text_formula(muscarine):
    assert muscarine.hill_formula.text_formula == "C9H20NO2 +"


### Tests for error handling

@pytest.mark.xfail(raises=TypeError)
def test_charge_failed():
    test = ChemFormula("H3O", "+")

@pytest.mark.xfail(raises=ValueError)
def test_brackets_closing():
    test = ChemFormula("H2)O")

@pytest.mark.xfail(raises=ValueError)
def test_brackets():
    test = ChemFormula("(H2)(O")

@pytest.mark.xfail(raises=ValueError)
def test_element():
    test = ChemFormula("caO")

@pytest.mark.xfail(raises=ValueError)
def test_unknown_element():
    test = ChemFormula("XyO")
