import pytest
from chemformula import ChemFormula


### pytest fixtures

@pytest.fixture
def muscarine():
    return ChemFormula("((CH3)3N)(C6H11O2)", charge = 1, name = "L-(+)-Muscarine", cas = 300_54_9)

@pytest.fixture
def uranophane():
    return ChemFormula("Ca(UO2)2(SiO3OH)2.(H2O)5")

@pytest.fixture
def ethylcinnamate():
    return ChemFormula("(C6H5)CHCHCOOC2H5")


### Tests for functionality

def test_name(muscarine):
    assert muscarine.name == "L-(+)-Muscarine"

def test_charge(muscarine):
    assert muscarine.charge == 1

def test_charged_true(muscarine):
    assert muscarine.charged is True

def test_charged_false(uranophane):
    assert uranophane.charged is False

def test_radioactive_true(uranophane):
    assert uranophane.radioactive is True

def test_radioactive_false(muscarine):
    assert muscarine.radioactive is False

def test_cas(muscarine):
    assert str(muscarine.cas) == "300-54-9"

def test_formula_weight(ethylcinnamate):
    assert round(ethylcinnamate.formula_weight, 3) == 176.215

def test_weight_fraction(uranophane):
    assert round(uranophane.mass_fraction["Si"]*1000, 3) == 65.59

def test_html(muscarine):
    assert muscarine.html == "<span class='ChemFormula'>((CH<sub>3</sub>)<sub>3</sub>N)(C<sub>6</sub>H<sub>11</sub>O<sub>2</sub>)<sup>+</sup></span>"

def test_latex(muscarine):
    assert muscarine.latex == r"\(\(\textnormal{C}\textnormal{H}_{3}\)_{3}\textnormal{N}\)\(\textnormal{C}_{6}\textnormal{H}_{11}\textnormal{O}_{2}\)^{+}"

def test_sum_formula_unicode(muscarine):
    assert muscarine.sum_formula.unicode == u"C₉H₂₀NO₂⁺"

def test_hill_formula_text_formula(muscarine):
    assert muscarine.hill_formula.text_formula == "C9H20NO2 +"

def test_element_dictionary(muscarine):
    assert muscarine.element["O"] == 2


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
