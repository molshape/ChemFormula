# ChemFormula

![PyPI Version](https://img.shields.io/pypi/v/ChemFormula)
![CI](https://github.com/molshape/ChemFormula/actions/workflows/ci.yml/badge.svg)
![Python Versions](https://img.shields.io/pypi/pyversions/ChemFormula)
![License](https://img.shields.io/github/license/molshape/ChemFormula) \
![GitHub stars](https://img.shields.io/github/stars/molshape/ChemFormula)


<details>
<summary>Table of Content</summary>

1. [Description](#description)
2. [How to install and uninstall?](#how-to-install-and-uninstall)
3. [Dependencies](#dependencies)
4. [How to use?](#how-to-use)
5. [Examples](#examples)
6. [Comparing and Sorting](#comparing-and-sorting-of-chemical-formulas)
7. [Atomic Weight Data](#atomic-weight-data)
	
</details>

## Description
**ChemFormula** is a Python class for working with chemical formulas. It allows parsing chemical formulas and generating predefined (LaTeX, HTML) or customized formatted output strings, e. g. <span>[Cu(NH<sub>3</sub>)<sub>4</sub>]SO<sub>4</sub>&sdot;H<sub>2</sub>O</span>. **ChemFormula** is also calculating the formula weight and thus enabling stoichiometric calculations with chemical formula objects. Atomic weights are based on IUPAC recommendations (see [Atomic Weight Data](#atomic-weight-data)).


## How to install and uninstall? 
**ChemFormula** can be installed from the [Python Package Index (PyPI)](https://pypi.org/) repository by calling

	pip install chemformula

In order to uninstall **ChemFormula** from your local environment use

	pip uninstall chemformula


## Dependencies
**ChemFormula** uses the [casregnum package](https://pypi.org/project/casregnum/) to manage CAS Registry Numbers®. The corresponding properties of the `CAS` class are therefore inherited to the ```ChemFormula``` class.


## How to use?
**ChemFormula** provides the `ChemFormula` class for creating a chemical formula object:

```Python
from chemformula import ChemFormula

chemical_formula = ChemFormula(formula,
                               charge = 0,
                               name = None,
                               cas = None)
```

*Examples:*

```Python
ethylcinnamate = ChemFormula("(C6H5)CHCHCOOC2H5")
tetraamminecoppersulfate = ChemFormula("[Cu(NH3)4]SO4.H2O")
uranophane = ChemFormula("Ca(UO2)2(SiO3OH)2.(H2O)5")

muscarine = ChemFormula("((CH3)3N)(C6H11O2)", charge = 1, name = "L-(+)-Muscarine")
pyrophosphate = ChemFormula("P2O7", -4)

caffeine = ChemFormula("C8H10N4O2", name = "caffeine", cas = 58_08_2)
theine = ChemFormula("(C5N4H)O2(CH3)3", name = "theine", cas = "58-08-2")
```

The `ChemFormula` class offers the following attributes/functions

```Python
.formula         # original chemical formula used to create the chemical formula object

.text_formula    # formula including charge as text output

.latex           # formats a formula as a string that can be used in LaTeX

.html            # formats a formula as a string that can be used in HTML

.unicode         # formats a formula with unicode subscript and superscript numbers

.format_formula( # custom formatting of the formula, .FormatFormula uses the following optional keyword arguments
                formula_prefix = "",                      # preceeds the complete formula string
                element_prefix = "", element_suffix = "", # encloses every chemical symbol (Prefix + Symbol + Suffix)
                freq_prefix = "", freq_suffix = "",       # encloses every element frequency (Prefix + Frequency + Suffix)
                formula_suffix = "",                      # closes the complete formula string
                bracket_prefix = "", bracket_suffix = "", # encloses all brackets: {[()]} (Prefix + Bracket + Suffix)
                multiply_symbol = "",                     # replacement for '.' or '*'
                charge_prefix = "", charge_suffix = "",   # encloses every charge information (Prefix + Charge + Suffix)
                charge_positive = "+",                    # symbol for a positive charge
                charge_negative = "-"                     # symbol for a negative charge
	       )

.sum_formula     # collapsed sum formula of .OriginalFormula with all bracketed units resolved as a ChemFormula object,
                 # i.e. use .SumFormula.HTML to retrive an HTML representation of the sum formula

.hill_formula    # sum formula in Hill notation as a ChemFormula object, i.e. use .HillFormula.Unicode to retrive
                 # a Unicode representation of the Hill formula (first Carbon, then Hydrogen (if carbon is present),
                 # followed by all other elements in alphabetical order of their chemical symbol)
                 # Source: Edwin A. Hill, J. Am. Chem. Soc., 1900 (22), 8, 478-494 (https://doi.org/10.1021/ja02046a005)

.formula_weight  # formula weight of the chemical formula in g/mol

.mass_fractions  # mass fraction of each element for the chemical formula in the form of
                 # key, value = chemical symbol, mass fraction

.name            # name of the chemical formula object

.radioactive     # boolean value whether the formula is radioactive (True) or not (False)

.charged         # boolean value whether the formula is charged (True) or not (False)

.charge          # integer value carrying the charge of the chemical formula object

.text_charge     # formatted string of the charge of the chemical formula object (e. g. 3+, 4-, +, ...)

.element         # is a dictionary representation of the formula composition in the form of
                 # key, value = chemical symbol, frequency of this element
                 # e.g.: .element["C"] gives the number of carbon atoms in the corresponding formula object

.cas             # CAS Registry Number® in a formatted way ('_____00-00-0')
                 # .cas is a CAS number object from the casregnum package
.cas.cas_string  # CAS number as a formatted string, inherited property from casregnum.CAS
.cas.cas_integer # CAS number as an integer value, inherited property from casregnum.CAS
.cas.check_digit # CAS number check digit, inherited property from casregnum.CAS
```


## Examples
The following python sample script

```Python
from chemformula import ChemFormula

tetraamminecoppersulfate = ChemFormula("[Cu(NH3)4]SO4.H2O")
ethylcinnamate = ChemFormula("(C6H5)CHCHCOOC2H5", name = "ethyl cinnamate")

uranophane = ChemFormula("Ca(UO2)2(SiO3OH)2.(H2O)5", name = "Uranophane")
muscarine = ChemFormula("((CH3)3N)(C6H11O2)", charge = 1, name = "L-(+)-Muscarine")

caffeine = ChemFormula("C8H10N4O2", name = "caffeine", cas = 58_08_2)

print(f"\n--- Formula Depictions of {muscarine.name} ---")
print(f" Print instance: {muscarine}")
print(f" Original:       {muscarine.formula}")
print(f" Text formula:   {muscarine.text_formula}")
print(f" HTML:           {muscarine.html}")
print(f" LaTeX:          {muscarine.latex}")
print(f" Unicode:        {muscarine.unicode}")
print(f" Charge (int):   {muscarine.charge}")
print(f" Charge (str):   {muscarine.text_charge}")
print(f" Sum formula:    {muscarine.sum_formula}")
print(f" Sum (HTML):     {muscarine.sum_formula.html}")
print(f" Sum (Unicode):  {muscarine.sum_formula.unicode}")
print(f" Hill formula:   {muscarine.hill_formula}")
print(f" Hill formula:   {muscarine.hill_formula.latex}")

print(f"\n--- Formula Weights Calculations with {ethylcinnamate.name.title()} ---")
print(f" The formula weight of {ethylcinnamate.name} ({ethylcinnamate.sum_formula.unicode}) is {ethylcinnamate.formula_weight:.2f} g/mol.")
mole = 1.4
print(f" {mole:.1f} mol of {ethylcinnamate.name} weight {mole * ethylcinnamate.formula_weight:.1f} g.")
mass = 24
print(f" {mass:.1f} g of {ethylcinnamate.name} corresponds to {mass/ethylcinnamate.formula_weight * 1000:.1f} mmol.")
print(f" The elemental composition of {ethylcinnamate.name} is as follows:")
for stringElementSymbol, floatElementFraction in ethylcinnamate.mass_fraction.items():
	print(f"   {stringElementSymbol:<2}: {floatElementFraction * 100:>5.2f} %")

print(f"\n--- {uranophane.name} and {muscarine.name} ---")
print(f" Yes, {uranophane.name} is radioactive.") if uranophane.radioactive else print(f" No, {uranophane.name} is not radioactive.")
print(f" Yes, {uranophane.name} is charged.") if uranophane.charged else print(f" No, {uranophane.name} is not charged.")
print(f" Yes, {muscarine.name} is radioactive.") if muscarine.radioactive else print(f" No, {muscarine.name} is not radioactive.")
print(f" Yes, {muscarine.name} is charged.") if muscarine.charged else print(f" No, {muscarine.name} is not charged.")

print("\n--- Accessing Single Elements through FormulaObject.Element[\"Element_Symbol\"] ---")
print(f" Tetraamminecopper(II)-sulfate contains {tetraamminecoppersulfate.element['N']} nitrogen atoms.")

print("\n--- CAS Registry Number ---")
print(f" {caffeine.name.capitalize()} has the CAS RN {caffeine.cas} (or as an integer: {caffeine.cas.cas_integer}).\n")
```

generates the following output

```
--- Formula Depictions of L-(+)-Muscarine ---
 Print instance: ((CH3)3N)(C6H11O2)
 Original:       ((CH3)3N)(C6H11O2)
 Text formula:   ((CH3)3N)(C6H11O2) +
 HTML:           <span class='ChemFormula'>((CH<sub>3</sub>)<sub>3</sub>N)(C<sub>6</sub>H<sub>11</sub>O<sub>2</sub>)<sup>+</sup></span>
 LaTeX:          \(\(\textnormal{C}\textnormal{H}_{3}\)_{3}\textnormal{N}\)\(\textnormal{C}_{6}\textnormal{H}_{11}\textnormal{O}_{2}\)^{+}
 Unicode:        ((CH₃)₃N)(C₆H₁₁O₂)⁺
 Charge (int):   1
 Charge (str):   +
 Sum formula:    C9H20NO2
 Sum (HTML):     <span class='ChemFormula'>C<sub>9</sub>H<sub>20</sub>NO<sub>2</sub><sup>+</sup></span>
 Sum (Unicode):  C₉H₂₀NO₂⁺
 Hill formula:   C9H20NO2
 Hill formula:   \textnormal{C}_{9}\textnormal{H}_{20}\textnormal{N}\textnormal{O}_{2}^{+}

--- Formula Weights Calculations with Ethyl Cinnamate ---
 The formula weight of ethyl cinnamate (C₁₁H₁₂O₂) is 176.21 g/mol.
 1.4 mol of ethyl cinnamate weight 246.7 g.
 24.0 g of ethyl cinnamate corresponds to 136.2 mmol.
 The elemental composition of ethyl cinnamate is as follows:
   C : 74.98 %
   H :  6.86 %
   O : 18.16 %

--- Uranophane and L-(+)-Muscarine ---
 Yes, Uranophane is radioactive.
 No, Uranophane is not charged.
 No, L-(+)-Muscarine is not radioactive.
 Yes, L-(+)-Muscarine is charged.

--- Accessing Single Elements through FormulaObject.Element["Element_Symbol"] ---
 Tetraamminecopper(II)-sulfate contains 4 nitrogen atoms.

--- CAS Registry Number ---
 Caffeine has the CAS RN 58-08-2 (or as an integer: 58082).
 ```

More examples can be found at [/examples/](https://github.com/molshape/ChemFormula/blob/main/examples/).


## Comparing and Sorting of Chemical Formulas

**ChemFormula** allows comparing and sorting of chemical formula objects. Chemical formula objects can be compared with the `==` operator. Two chemical formula objects are considered equal, if they have the same chemical composition (i.e. the same sum formula) and the same charge. If a CAS number is specified, the CAS number of both objects must also be identical.

Formulas will be sorted into lexicographical order with reference to the Hill notation ([Edwin A. Hill, *J. Am. Chem. Soc.*, **1900**, *22*(8), 478-494](https://doi.org/10.1021/ja02046a005)). All chemical symbols are sorted alphabetically, with carbon and hydrogen moved to the top position, if carbon atoms are present. Elements with different element frequencies are sorted numerically in ascending order.

```python
from chemformula import ChemFormula

caffeine = ChemFormula("C8H10N4O2", name = "caffeine", cas = 58_08_2)
theine = ChemFormula("(C5N4H)O2(CH3)3", name = "theine", cas = "58-08-2")

l_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "L-lactic acid", cas = 79_33_4)
d_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "D-lactic acid", cas = 10326_41_7)

hydrocarbons = [ChemFormula("C3H5"), ChemFormula("C6H12O6"), ChemFormula("C6H12O5S"), ChemFormula("C3H5O"),
                ChemFormula("C4H5"), ChemFormula("C6H12S6"), ChemFormula("C6H12S2O3")]

print(f"\n--- Comparing {caffeine.name.capitalize()} with {theine.name.capitalize()} and Lactic Acid Isomers ---")
print(f" {caffeine.name.capitalize()} and {theine.name} are", end=" ")
print("identical.") if caffeine == theine else print("not identical.")
print(f" {l_lacticacid.name} and {d_lacticacid.name} are", end=" ")
print("identical.") if l_lacticacid == d_lacticacid else print("not identical.")

print("\n--- Lexical Sorting of Chemical Formulas via Hill Notation ---")
for position, item in enumerate(sorted(hydrocarbons), start = 1):
    print(f"{position:>3}. {item.hill_formula.unicode}")
```

generates the following output

```
--- Comparing Caffeine with Theine and Lactic Acid Isomers ---
 Caffeine and theine are identical.
 L-lactic acid and D-lactic acid are not identical.

--- Lexical Sorting of Chemical Formulas via Hill Notation ---
  1. C₃H₅
  2. C₃H₅O
  3. C₄H₅
  4. C₆H₁₂O₃S₂
  5. C₆H₁₂O₅S
  6. C₆H₁₂O₆
  7. C₆H₁₂S₆
 ```


## Atomic Weight Data

All atomic weights are taken from the IUPAC Commission on Isotopic Abundances and Atomic Weights and are based on the following reports and publications:

- [*Pure Appl. Chem.*, **2016**, *88*, 265-291](https://doi.org/10.1515/pac-2015-0305)
- [*Chem. Eng. News*, **2015**, *93*(37), 9](https://doi.org/10.1021/cen-09337-notw9)
- [*Pure Appl. Chem.*, **2016**, *88*, 139-153](https://doi.org/10.1515/pac-2015-0502)
- [*Pure Appl. Chem.*, **2016**, *88*, 155-160](https://doi.org/10.1515/pac-2015-0501)
- [*Pure Appl. Chem.*, **2016**, *88*, 1225-1229](https://doi.org/10.1515/pac-2016-0501)
- [*Chem. Int.*, **2018**, *40*(4), 23-24](https://doi.org/10.1515/ci-2018-0409)
- [*Chem. Int.*, **2020**, *42*(2), 31](https://doi.org/10.1515/ci-2020-0222)
- [*Pure Appl. Chem.*, **2022**, *94*(5), 573-600](https://doi.org/10.1515/pac-2019-0603)
- [*Chem. Int.*, **2025**, *47*(1), 20-20](https://doi.org/10.1515/ci-2025-0105)

The current data has been downloaded from https://iupac.qmul.ac.uk/AtWt/ as of August 2<sup>nd</sup>, 2025. The original data has been mirrored to [AtWt23.html](https://github.com/molshape/ChemFormula/blob/main/misc/AtWt23.html).

Quoted atomic weights are those suggested for materials where the origin of the sample is unknown. For most radioactive elements the isotope with the longest half-life is quoted as an integer.
