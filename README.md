# ChemFormula (v1.2.2)

<details>
<summary>Table of Content</summary>

1. [Description](#description)
2. [How to install and uninstall?](#how-to-install-and-uninstall)
3. [How to use?](#how-to-use)
4. [Examples](#examples)
5. [Atomic Weight Data](#atomic-weight-data)
	
</details>

## Description
**ChemFormula** is a Python class for working with chemical formulas. It allows parsing chemical formulas and generating predefined (LaTeX, HTML) or customized formatted output strings, e. g. <span>[Cu(NH<sub>3</sub>)<sub>4</sub>]SO<sub>4</sub>&sdot;H<sub>2</sub>O</span>. **ChemFormula** is also calculating the formula weight and thus enabling stoichiometric calculations with chemical formula objects. Atomic weights are based on IUPAC recommendations (see [Atomic Weight Data](#atomic-weight-data)).


## How to install and uninstall? 
**ChemFormula** can be installed from the [Python Package Index (PyPI)](https://pypi.org/) repository by calling

	pip install ChemFormula

In order to uninstall **ChemFormula** from your local environment use

	pip uninstall ChemFormula


## How to use?
**ChemFormula** provides the `ChemFormula` class for creating a chemical formula object:

```Python
from ChemFormula import ChemFormula

objChemFormula = ChemFormula(strFormula,
                             intCharge = 0,
			     strName = None,
			     CAS = None)
```

*Examples:*

```Python
ethylcinnamate = ChemFormula("(C6H5)CHCHCOOC2H5")
tetraamminecoppersulfate = ChemFormula("[Cu(NH3)4]SO4.H2O")
uranophane = ChemFormula("Ca(UO2)2(SiO3OH)2.(H2O)5")

muscarine = ChemFormula("((CH3)3N)(C6H11O2)", intCharge = 1, "L-(+)-Muscarine")
pyrophosphate = ChemFormula("P2O7", -4)

coffein = ChemFormula("C8H10N4O2", strName = "coffein", CAS = 58_08_2)
teein = ChemFormula("C8H10N4O2", strName = "teein", CAS = "58-08-2")
```

The `ChemFormula` class offers the following attributes/functions

```Python
.OriginalFormula # original chemical formula used to create the chemical formula object

.LaTeX           # formats the formula as a string that can be used in LaTeX

.HTML            # formats the formula as a string that can be used in HTML

.FormatFormula(  # custom formatting of the formula, .FormatFormula uses the following optional keyword arguments
               sFormulaPrefix = "",                        # preceeds the complete formula string
               sElementPrefix = "", sElementSuffix = "",   # encloses every chemical symbol (Prefix + Symbol + Suffix)
               sFreqPrefix = "", sFreqSuffix = "",         # encloses every element frequency (Prefix + Frequency + Suffix)
               sFormulaSuffix = "",                        # closes the complete formula string
               sBracketPrefix = "", sBracketSuffix = "",   # encloses all brackets: {[()]} (Prefix + Bracket + Suffix)
               sMultiplySymbol = "",                       # replacement for '.' or '*'
	       strChargePrefix = "", strChargeSuffix = "", # encloses every charge information (Prefix + Charge + Suffix)
	       strChargePositive = "+",                    # symbol for a positive charge
	       strChargeNegative = "-"                     # symbol for a negative charge
	       )

.SumFormula      # collapsed sum formula of .OriginalFormula with all bracketed units resolved

.HillFormula     # sum formula in Hill notation (first Carbon, then Hydrogen, followed
                 # by all other elements in alphabetical order of their chemical symbol

.FormulaWeight   # formula weight of the chemical formula in g/mol

.MassFractions   # mass fraction of each element for the chemical formula in the form of
                 # key, value = chemical symbol, mass fraction

.Name            # name of the chemical formula object

.Radioactive     # boolean value whether the formula is radioactive (True) or not (False)

.Charged         # boolean value whether the formula is charged (True) or not (False)

.Charge          # integer value carrying the charge of the chemical formula object

.TextCharge      # formatted string of the charge of the chemical formula object (e. g. 3+, 4-, +, ...)

.Element         # is a dictionary representation of the formula composition in the form of
                 # key, value = chemical symbol, frequency of this element
                 # e.g.: .Element["C"] gives the number of carbon atoms in the corresponding formula object

.CAS             # CAS registry number in a formatted way ('_____00-00-0')

.CASint          # CAS registry number as an integer value (all hyphens are ignored)
```


## Examples
The following python sample script

```Python
from ChemFormula import ChemFormula

tetraamminecoppersulfate = ChemFormula("[Cu(NH3)4]SO4.H2O")
ethylcinnamate = ChemFormula("(C6H5)CHCHCOOC2H5", strName="ethyl cinnamate")

uranophane = ChemFormula("Ca(UO2)2(SiO3OH)2.(H2O)5", strName="Uranophane")
muscarine = ChemFormula("((CH3)3N)(C6H11O2)", 1, "L-(+)-Muscarine")

coffein = ChemFormula("C8H10N4O2", strName="coffein", CAS = 58_08_2)

print(f"\n--- Formula Depictions of {muscarine.Name} ---")
print(f" Print instance: {muscarine}")
print(f" Original:       {muscarine.OriginalFormula}")
print(f" HTML:           {muscarine.HTML}")
print(f" LaTeX:          {muscarine.LaTeX}")
print(f" Charge (int):   {muscarine.Charge}")
print(f" Charge (str):   {muscarine.TextCharge}")
print(f" Sum formula:    {muscarine.SumFormula}")
print(f" Hill formula:   {muscarine.HillFormula}")

print(f"\n--- Formula Weights Calculations with {ethylcinnamate.Name.title()} ---")
print(f" The formula weight of {ethylcinnamate.Name} is {ethylcinnamate.FormulaWeight:.2f} g/mol.")
Mole = 1.4
print(f" {Mole:.1f} mol of {ethylcinnamate.Name} weight {Mole * ethylcinnamate.FormulaWeight:.1f} g.")
Mass = 24
print(f" {Mass:.1f} g of {ethylcinnamate.Name} corresponds to {Mass/ethylcinnamate.FormulaWeight * 1000:.1f} mmol.")
print(f" The elemental composition of {ethylcinnamate.Name} is as follows:")
for stringElementSymbol, floatElementFraction in ethylcinnamate.MassFraction.items():
	print(f"   {stringElementSymbol:<2}: {floatElementFraction * 100:>5.2f} %")

print(f"\n--- {uranophane.Name} and {muscarine.Name} ---")
print(f" Yes, {uranophane.Name} is radioactive.") if uranophane.Radioactive else print(f" No, {uranophane.Name} is not radioactive.")
print(f" Yes, {uranophane.Name} is charged.") if uranophane.Charged else print(f" No, {uranophane.Name} is not charged.")
print(f" Yes, {muscarine.Name} is radioactive.") if muscarine.Radioactive else print(f" No, {muscarine.Name} is not radioactive.")
print(f" Yes, {muscarine.Name} is charged.") if muscarine.Charged else print(f" No, {muscarine.Name} is not charged.")

print("\n--- Accessing Single Elements through FormulaObject.Element[\"Element_Symbol\"] ---")
print(f" Tetraamminecopper(II)-sulfate contains {tetraamminecoppersulfate.Element['N']} nitrogen atoms.")

print("\n--- CAS Registry Number ---")
print(f" {coffein.Name.capitalize()} has the CAS RN {coffein.CAS} (or as an integer: {coffein.CASint}).\n")
```

generates the following output

```
--- Formula Depictions of L-(+)-Muscarine ---
 Print instance: ((CH3)3N)(C6H11O2) +
 Original:       ((CH3)3N)(C6H11O2)
 HTML:           <span class='ChemFormula'>((CH<sub>3</sub>)<sub>3</sub>N)(C<sub>6</sub>H<sub>11</sub>O<sub>2</sub>)<sup>+</sup></span>
 LaTeX:          \(\(\textnormal{C}\textnormal{H}_{3}\)_{3}\textnormal{N}\)\(\textnormal{C}_{6}\textnormal{H}_{11}\textnormal{O}_{2}\)^{+}
 Charge (int):   1
 Charge (str):   +
 Sum formula:    C9H20NO2
 Hill formula:   C9H20NO2

--- Formula Weights Calculations with Ethyl Cinnamate ---
 The formula weight of ethyl cinnamate is 176.21 g/mol.
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
 Coffein has the CAS RN 58-08-2 (or as an integer: 58082).
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

The actual data has been downloaded from https://www.qmul.ac.uk/sbcs/iupac/AtWt/ as of August 8th, 2021.

Quoted atomic weights are those suggested for materials where the origin of the sample is unknown. For most radioactive elements the isotope with the longest half-life is quoted as an integer.
