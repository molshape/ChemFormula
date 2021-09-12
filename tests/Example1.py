from chemformula import ChemFormula

tetraamminecoppersulfate = ChemFormula("[Cu(NH3)4]SO4.H2O")
ethylcinnamate = ChemFormula("(C6H5)CHCHCOOC2H5")
uranophane = ChemFormula("Ca(UO2)2(SiO3OH)2(H2O)5", name = "Uranophane")

print("\n--- Formula Depictions of Tetraamminecopper(II)-sulfate ---")
print(f" Print instance: {tetraamminecoppersulfate.original_formula}")
print(f" Original:       {tetraamminecoppersulfate}")
print(f" Charged:        {tetraamminecoppersulfate.charged}")
print(f" Charge (int):   {tetraamminecoppersulfate.charge}")
print(f" LaTeX:          {tetraamminecoppersulfate.latex}")
print(f" HTML:           {tetraamminecoppersulfate.html}")
print(f" Custom format:  {tetraamminecoppersulfate.format_formula('--> ', '', '', '_<', '>', ' <--', '', '', ' * ')}")
print(f" Sum formula:    {tetraamminecoppersulfate.sum_formula}")
print(f" Hill formula:   {tetraamminecoppersulfate.hill_formula}")

print("\n--- Formula Weights Calculations with Ethyl Cinnamate ---")
print(f" The formula weight of ethyl cinnamate is {ethylcinnamate.formula_weight:.2f} g/mol.")
Mole = 1.4
print(f" {Mole:.1f} mol of ethyl cinnamate weight {Mole * ethylcinnamate.formula_weight:.1f} g.")
Mass = 24
print(f" {Mass:.1f} g of ethyl cinnamate corresponds to {Mass/ethylcinnamate.formula_weight * 1000:.1f} mmol.")
print(" The elemental composition of ethyl cinnamate is as follows:")
for stringElementSymbol, floatElementFraction in ethylcinnamate.mass_fraction.items():
	print(f"   {stringElementSymbol:<2}: {floatElementFraction * 100:>5.2f} %")

print("\n--- Is Uranophane Radioactive and Charged? ---")
print(f" Yes, {uranophane.name} is radioactive.") if uranophane.radioactive else print(f" No, {uranophane.name} is not radioactive.")
print(f" Yes, {uranophane.name} is charged.") if uranophane.charged else print(f" No, {uranophane.name} is not charged.")

print("\n--- Accessing Single Elements through FormulaObject.Element[\'Element_Symbol\'] ---")
print(f" Cupric sulfate contains {tetraamminecoppersulfate.element['N']} nitrogen atoms.\n")

### OUTPUT:
#
# --- Formula Depictions of Tetraamminecopper(II)-sulfate ---
#  Print instance: [Cu(NH3)4]SO4.H2O
#  Original:       [Cu(NH3)4]SO4.H2O
#  Charged:        False
#  Charge (int):   0
#  LaTeX:          \[\textnormal{Cu}\(\textnormal{N}\textnormal{H}_{3}\)_{4}\]\textnormal{S}\textnormal{O}_{4}\cdot\textnormal{H}_{2}\textnormal{O}
#  HTML:           <span class='ChemFormula'>[Cu(NH<sub>3</sub>)<sub>4</sub>]SO<sub>4</sub>&sdot;H<sub>2</sub>O</span>
#  Custom format:  --> [Cu(NH_<3>)_<4>]SO_<4> * H_<2>O <--
#  Sum formula:    CuN4H14SO5
#  Hill formula:   CuH14N4O5S
#
# --- Formula Weights Calculations with Ethyl Cinnamate ---
#  The formula weight of ethyl cinnamate is 176.21 g/mol.
#  1.4 mol of ethyl cinnamate weight 246.7 g.
#  24.0 g of ethyl cinnamate corresponds to 136.2 mmol.
#  The elemental composition of ethyl cinnamate is as follows:
#    C : 74.98 %
#    H :  6.86 %
#    O : 18.16 %
#
# --- Is Uranophane Radioactive and Charged? ---
#  Yes, Uranophane is radioactive.
#  No, Uranophane is not charged.
#
# --- Accessing Single Elements through FormulaObject.Element['Element_Symbol'] ---
#  Cupric sulfate contains 4 nitrogen atoms.
#