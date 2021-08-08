# PyChemFormula (v0.2.0)

<details>
<summary>Table of Content</summary>

1. [Short Description](#short-description)
2. [How to install and uninstall?](#how-to-install-and-uninstall)
3. [How to use?](#how-to-use)
4. [Examples](#examples)
5. [Atomic Weight Data](#atomic-weight-data)
	
</details>

## Short Description
**PyChemFormula** is a Python class for working with chemical formulas. It allows parsing chemical formulas and generating predefined (LaTeX, HTML) or customized formatted output strings, e. g. <span>[Cu(NH<sub>3</sub>)<sub>4</sub>]SO<sub>4</sub>&sdot;H<sub>2</sub>O</span>. **PyChemFormula** is also calculating the formula weight and thus enabling stoichiometric calculations with formula objects. Atomic weights are based on IUPAC recommendations (see [Atomic Weight Data](#atomic-weight-data)).


## How to install and uninstall? 
**PyChemFormula** can be installed from this source by calling

	python setup.py install

<!--or from the [Python Package Index (PyPI)](https://pypi.org/) repository by calling

	pip install PyChemFormula
-->
In order to uninstall **PyChemFormula** from your local environment use

	pip uninstall PyChemFormula


## How to use?
**PyChemFormula**'s class for creating a chemical formula is called `Formula`:

```Python
tetraamminecoppersulfate = Formula("[Cu(NH3)4]SO4.H2O")
ethylcinnamate = Formula("(C6H5)CHCHCOOC2H5")
uranophane = Formula("Ca(UO2)2(SiO3OH)2(H2O)5")
```

The `Formula` class offers the following attributes/functions

```Python
.OriginalFormula # original chemical formula used to create the chemical formula object

.LaTeX           # formats the formula as a string that can be used in LaTeX

.HTML            # formats the formula as a string that can be used in HTML

.FormatFormula(  # custom formatting of the formula, .FormatFormula uses the following optional keyword arguments
               sFormulaPrefix = "",                        # preceeds the complete formula string
               sElementPrefix = "", sElementSuffix = "",   # encloses every element symbol (Prefix + Symbol + Suffix)
               sFreqPrefix = "", sFreqSuffix = "",         # encloses every element frequency (Prefix + Symbol + Suffix)
               sFormulaSuffix = "",                        # closes the complete formula string
               sBracketPrefix = "", sBracketSuffix = "",   # encloses all brackets: {[()]} (Prefix + Bracket + Suffix)
               sMultiplySymbol = "")                       # replacement for "." or "*"

.SumFormula      # collapsed sum formula of .OriginalFormula with all bracketed units resolved

.HillFormula     # sum formula in Hill notation (first Carbon, then Hydrogen, followed
                 # by all other elements in alphabetical order of their chemical symbol

.FormulaWeight   # formula weight of the chemical formula in g/mol

.MassFractions   # mass fraction of each element for the chemical formula in the form of
                 # key, value = elemental symbol, mass fraction

.Radioactive     # boolean value whether the formula is radioactive (True) or not (False)

.Element         # is a dictionary representation of the formula composition in the form of
                 # key, value = elemental symbol, frequency of this element
                 # e.g.: .Element["C"] gives the number of carbon atoms in the corresponding formula object
```


## Examples
The following python sample script

```Python
from PyChemFormula import Formula

tetraamminecoppersulfate = Formula("[Cu(NH3)4]SO4.H2O")
ethylcinnamate = Formula("(C6H5)CHCHCOOC2H5")
uranophane = Formula("Ca(UO2)2(SiO3OH)2(H2O)5")

print("\n--- Formula Depictions of Tetraamminecopper(II)-sulfate ---")
print(" Original:      {0}".format(tetraamminecoppersulfate.OriginalFormula))
print(" LaTeX:         {0}".format(tetraamminecoppersulfate.LaTeX))
print(" HTML:          {0}".format(tetraamminecoppersulfate.HTML))
print(" Custom format: {0}".format(tetraamminecoppersulfate.FormatFormula("--> ", "", "", "_<", ">", " <--", "", "", " * ")))
print(" Sum formula:   {0}".format(tetraamminecoppersulfate.SumFormula))
print(" Hill formula:  {0}".format(tetraamminecoppersulfate.HillFormula))

print("\n--- Formula Weights Calculations with Ethyl Cinnamate ---")
print(" The formula weight of ethyl cinnamate is {:.2f} g/mol.".format(ethylcinnamate.FormulaWeight))
Mole = 1.4
print(" {0:.1f} mol of ethyl cinnamate weight {1:.1f} g.".format(Mole, Mole * ethylcinnamate.FormulaWeight))
Mass = 24
print(" {0:.1f} g of ethyl cinnamate corresponds to {1:.1f} mmol.".format(Mass, Mass/ethylcinnamate.FormulaWeight * 1000))
print(" The elemental composition of ethyl cinnamate is as follows:")
for stringElementSymbol, floatElementFraction in ethylcinnamate.MassFractions.items():
	print("   {0:<2}: {1:>5.2f} %".format(stringElementSymbol, floatElementFraction * 100))

print("\n--- Is Uranophane Radioactive? ---")
print(" Yes") if uranophane.Radioactive else print(" No")

print("\n--- Accessing Single Elements through FormulaObject.Element[\"Element_Symbol\"] ---")
print(" Tetraamminecopper(II)-sulfate contains {0} nitrogen atoms.\n".format(tetraamminecoppersulfate.Element["N"]))
```

generates the following output

```
--- Formula Depictions of tetraamminecopper(II)-sulfate ---
 Original:      [Cu(NH3)4]SO4.H2O
 LaTeX:         \[\textnormal{Cu}\(\textnormal{N}\textnormal{H}_{3}\)_{4}\]\textnormal{S}\textnormal{O}_{4}\cdot\textnormal{H}_{2}\textnormal{O}
 HTML:          <span class='formula'>[Cu(NH<sub>3</sub>)<sub>4</sub>]SO<sub>4</sub>&sdot;H<sub>2</sub>O</span>
 Custom format: --> [Cu(NH_<3>)_<4>]SO_<4> * H_<2>O <--
 Sum formula:   CuN4H14SO5
 Hill formula:  CuH14N4O5S

--- Formula Weights Calculations with Ethyl Cinnamate ---
 The formula weight of ethyl cinnamate is 176.21 g/mol.
 1.4 mol of ethyl cinnamate weight 246.7 g.
 24.0 g of ethyl cinnamate corresponds to 136.2 mmol.
 The elemental composition of ethyl cinnamate is as follows:
   C : 74.98 %
   H :  6.86 %
   O : 18.16 %

--- Is Uranophane Radioactive? ---
 Yes

--- Accessing Single Elements through FormulaObject.Element["Element_Symbol"] ---
 Tetraamminecopper(II)-sulfate contains 4 nitrogen atoms.
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
