## PyChemFormula (v20210723-1130)

### Short Description
**PyChemFormula** is a Python class for working with chemical formulas.

### How to use?
**PyChemFormula**'s class for creating a chemical formula is called `Formula`:

```Python
cupric_sulfate = Formula("[Cu(NH3)4]SO4")
ethylcinnamate = Formula("(C6H5)CHCHCOOC2H5")
uranophane = Formula("Ca(UO2)2(SiO3OH)2(H2O)5")
```

`Formula` offers the following attributes

```Python
.OriginalFormula # original chemical formula used to create the chemical formula object

.SumFormula      # collapsed sum formula of .OriginalFormula with all bracketed units resolved

.HillFormula     # sum formula in Hill notation (first Carbon, then Hydrogen, followed
                 # by all other elements in alphabetical order of their chemical symbol

.FormulaWeight   # formula weight of the chemical formula in g/mol

.MassFractions   # mass fraction of each element for the chemical formula in the form of
                 # key, value = elemental symbol, mass fraction

.Radioactive     # boolean value whether the formula is radioactive (True) or not (False)

.Element         # is a dictionary representation of the formula composition in the form of
                 # key, value = elemental symbol, frequency of this element
                 # e.g.: .Element["C"] gives the number of carbon atoms in this formula
```

### Examples

The following python sample script

```Python
from PyChemFormula import Formula

ethylcinnamate = Formula("(C6H5)CHCHCOOC2H5")
cupric_sulfate = Formula("[Cu(NH3)4]SO4")
uranophane = Formula("Ca(UO2)2(SiO3OH)2(H2O)5")

print("\n--- Formula Depictions of Cupric Sulfate ---")
print(" Original:     {0}".format(cupric_sulfate.OriginalFormula))
print(" Sum formula:  {0}".format(cupric_sulfate.SumFormula))
print(" Hill formula: {0}".format(cupric_sulfate.HillFormula))

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
print(" Cupric sulfate contains {0} nitrogen atoms.\n".format(cupric_sulfate.Element["N"]))
```

will generate the following output

```
--- Formula Depictions of Cupric Sulfate ---
 Original:     [Cu(NH3)4]SO4
 Sum formula:  CuN4H12SO4
 Hill formula: H12CuN4O4S

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
 Cupric sulfate contains 4 nitrogen atoms.
```
