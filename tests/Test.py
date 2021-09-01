from ChemFormula import ChemFormula

tetraamminecoppersulfate = ChemFormula("[Cu(NH3)4]SO4.H2O")
ethylcinnamate = ChemFormula("(C6H5)CHCHCOOC2H5", strName="ethyl cinnamate")

uranophane = ChemFormula("Ca(UO2)2(SiO3OH)2.(H2O)5", strName="Uranophane")
muscarine = ChemFormula("((CH3)3N)(C6H11O2)", 1, "L-(+)-Muscarine")

coffein = ChemFormula("C8H10N4O2", strName="coffein", CAS = 58_08_2)
theine = ChemFormula("(C5N4H)O2(CH3)3", strName = "theine", CAS = "58-08-2")

l_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "L-lactic acid", CAS = 79_33_4)
d_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "D-lactic acid", CAS = 10326_41_7)

hydrocarbons = [ChemFormula("C3H5"), ChemFormula("C6H12O6"), ChemFormula("C6H12O5S"), ChemFormula("C3H5O"), ChemFormula("C4H5"), ChemFormula("C6H12S6"), ChemFormula("C6H12S2O3")]

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
print(f" {coffein.Name.capitalize()} has the CAS RN {coffein.CAS} (or as an integer: {coffein.CASint}).")

print(f"\n--- Comparing {coffein.Name.capitalize()} with {theine.Name.capitalize()} and Lactic Acid Isomers ---")
print(f" {coffein.Name.capitalize()} and {theine.Name} are", end=" ")
print("identical.") if coffein == theine else print("not identical.")
print(f" {l_lacticacid.Name} and {d_lacticacid.Name} are", end=" ")
print("identical.") if l_lacticacid == d_lacticacid else print("not identical.")

print("\n--- Lexical Sorting of Chemical Formulas via Hill Notation ---")
for position, item in enumerate(sorted(hydrocarbons), start = 1):
    print(f"{position:>3}. {item.HillFormula.Unicode}")