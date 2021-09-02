from ChemFormula import ChemFormula

tetraamminecoppersulfate = ChemFormula("[Cu(NH3)4]SO4.H2O")
ethylcinnamate = ChemFormula("(C6H5)CHCHCOOC2H5", Name = "ethyl cinnamate")

uranophane = ChemFormula("Ca(UO2)2(SiO3OH)2.(H2O)5", Name = "Uranophane")
muscarine = ChemFormula("((CH3)3N)(C6H11O2)", Charge = 1, Name = "L-(+)-Muscarine")

caffeine = ChemFormula("C8H10N4O2", Name = "caffeine", CAS = 58_08_2)

print(f"\n--- Formula Depictions of {muscarine.Name} ---")
print(f" Print instance: {muscarine}")
print(f" Original:       {muscarine.OriginalFormula}")
print(f" HTML:           {muscarine.HTML}")
print(f" LaTeX:          {muscarine.LaTeX}")
print(f" Unicode:        {muscarine.Unicode}")
print(f" Charge (int):   {muscarine.Charge}")
print(f" Charge (str):   {muscarine.TextCharge}")
print(f" Sum formula:    {muscarine.SumFormula}")
print(f" Sum (HTML):     {muscarine.SumFormula.HTML}")
print(f" Sum (Unicode):  {muscarine.SumFormula.Unicode}")
print(f" Hill formula:   {muscarine.HillFormula}")
print(f" Hill formula:   {muscarine.HillFormula.LaTeX}")

print(f"\n--- Formula Weights Calculations with {ethylcinnamate.Name.title()} ---")
print(f" The formula weight of {ethylcinnamate.Name} ({ethylcinnamate.SumFormula.Unicode}) is {ethylcinnamate.FormulaWeight:.2f} g/mol.")
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
print(f" {caffeine.Name.capitalize()} has the CAS RN {caffeine.CAS} (or as an integer: {caffeine.CASint}).\n")

### OUTPUT:
#
# --- Formula Depictions of L-(+)-Muscarine ---
#  Print instance: ((CH3)3N)(C6H11O2)
#  Original:       ((CH3)3N)(C6H11O2)
#  HTML:           <span class='ChemFormula'>((CH<sub>3</sub>)<sub>3</sub>N)(C<sub>6</sub>H<sub>11</sub>O<sub>2</sub>)<sup>+</sup></span>   
#  LaTeX:          \(\(\textnormal{C}\textnormal{H}_{3}\)_{3}\textnormal{N}\)\(\textnormal{C}_{6}\textnormal{H}_{11}\textnormal{O}_{2}\)^{+}
#  Unicode:        ((CH₃)₃N)(C₆H₁₁O₂)⁺
#  Charge (int):   1
#  Charge (str):   +
#  Sum formula:    C9H20NO2
#  Sum (HTML):     <span class='ChemFormula'>C<sub>9</sub>H<sub>20</sub>NO<sub>2</sub><sup>+</sup></span>
#  Sum (Unicode):  C₉H₂₀NO₂⁺
#  Hill formula:   C9H20NO2
#  Hill formula:   \textnormal{C}_{9}\textnormal{H}_{20}\textnormal{N}\textnormal{O}_{2}^{+}
#
# --- Formula Weights Calculations with Ethyl Cinnamate ---
#  The formula weight of ethyl cinnamate (C₁₁H₁₂O₂) is 176.21 g/mol.
#  1.4 mol of ethyl cinnamate weight 246.7 g.
#  24.0 g of ethyl cinnamate corresponds to 136.2 mmol.
#  The elemental composition of ethyl cinnamate is as follows:
#    C : 74.98 %
#    H :  6.86 %
#    O : 18.16 %
#
# --- Uranophane and L-(+)-Muscarine ---
#  Yes, Uranophane is radioactive.
#  No, Uranophane is not charged.
#  No, L-(+)-Muscarine is not radioactive.
#  Yes, L-(+)-Muscarine is charged.
#
# --- Accessing Single Elements through FormulaObject.Element["Element_Symbol"] ---
#  Tetraamminecopper(II)-sulfate contains 4 nitrogen atoms.
#
# --- CAS Registry Number ---
#  Caffeine has the CAS RN 58-08-2 (or as an integer: 58082).
#