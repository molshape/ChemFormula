from ChemFormula import ChemFormula

muscarine = ChemFormula("((CH3)3N)(C6H11O2)", 1, "L-(+)-Muscarine")
pyrophosphate = ChemFormula("P2O7", -4)

print("\n--- Formula Depictions of the L-(+)-Muscarine Ion ---")
print(f" Print instance: {muscarine}")
print(f" Original:       {muscarine.OriginalFormula}")
print(f" Charged:        {muscarine.Charged}")
print(f" Charge (int):   {muscarine.Charge}")
print(f" Charge (str):   {muscarine.TextCharge}")
print(f" LaTeX:          {muscarine.LaTeX}")
print(f" HTML:           {muscarine.HTML}")
print(f" Custom format:  {muscarine.FormatFormula('--> ', '', '', '_<', '>', ' <--', '', '', ' * ', '^^', '^^', '(+)', '(-)')}")
print(f" Sum formula:    {muscarine.SumFormula}")
print(f" Hill formula:   {muscarine.HillFormula}")

print("\n--- Formula Depictions of Pyrophosphate ---")
print(f" Print instance: {pyrophosphate}")
print(f" Original:       {pyrophosphate.OriginalFormula}")
print(f" Charged:        {pyrophosphate.Charged}")
print(f" Charge (int):   {pyrophosphate.Charge}")
print(f" Charge (str):   {pyrophosphate.TextCharge}")
print(f" LaTeX:          {pyrophosphate.LaTeX}")
print(f" HTML:           {pyrophosphate.HTML}")
print(f" Custom format:  {pyrophosphate.FormatFormula('--> ', '', '', '_<', '>', ' <--', '', '', ' * ', '^^', '^^', '(+)', '(-)')}")
print(f" Sum formula:    {pyrophosphate.SumFormula}")
print(f" Hill formula:   {pyrophosphate.HillFormula}")

print("\n--- Formula Weights Calculations with Muscarine ---")
print(f" The formula weight of Muscarine is {muscarine.FormulaWeight:.2f} g/mol.")
Mole = 1.4
print(f" {Mole:.1f} mol of Muscarine weight {Mole * muscarine.FormulaWeight:.1f} g.")
Mass = 24
print(f" {Mass:.1f} g of Muscarine corresponds to {Mass/muscarine.FormulaWeight * 1000:.1f} mmol.")
print(f" The elemental composition of Muscarine is as follows:")
for stringElementSymbol, floatElementFraction in muscarine.MassFraction.items():
	print(f"   {stringElementSymbol:<2}: {floatElementFraction * 100:>5.2f} %")

print("\n--- Is L-(+)-Muscarine Radioactive and Charged? ---")
print(f" Yes, {muscarine.Name} is radioactive.") if muscarine.Radioactive else print(f" No, {muscarine.Name} is not radioactive.")
print(f" Yes, {muscarine.Name} is charged.") if muscarine.Charged else print(f" No, {muscarine.Name} is not charged.")

print("\n--- Accessing Single Elements through FormulaObject.Element[\'Element_Symbol\'] ---")
print(f" Muscarine contains {muscarine.Element['O']} oxygen atoms.\n")

### OUTPUT:
#
# --- Formula Depictions of the L-(+)-Muscarine Ion ---
#  Print instance: ((CH3)3N)(C6H11O2) +
#  Original:       ((CH3)3N)(C6H11O2)
#  Charged:        True
#  Charge (int):   1
#  Charge (str):   +
#  LaTeX:          \(\(\textnormal{C}\textnormal{H}_{3}\)_{3}\textnormal{N}\)\(\textnormal{C}_{6}\textnormal{H}_{11}\textnormal{O}_{2}\)^{+}
#  HTML:           <span class='ChemFormula'>((CH<sub>3</sub>)<sub>3</sub>N)(C<sub>6</sub>H<sub>11</sub>O<sub>2</sub>)<sup>+</sup></span>
#  Custom format:  --> ((CH_<3>)_<3>N)(C_<6>H_<11>O_<2>)^^+^^ <--
#  Sum formula:    C9H20NO2
#  Hill formula:   C9H20NO2
# 
# --- Formula Depictions of Pyrophosphate ---
#  Print instance: P2O7 4-
#  Original:       P2O7
#  Charged:        True
#  Charge (int):   -4
#  Charge (str):   4-
#  LaTeX:          \textnormal{P}_{2}\textnormal{O}_{7}^{4-}
#  HTML:           <span class='ChemFormula'>P<sub>2</sub>O<sub>7</sub><sup>4-</sup></span>
#  Custom format:  --> P_<2>O_<7>^^4-^^ <--
#  Sum formula:    P2O7
#  Hill formula:   O7P2
# 
# --- Formula Weights Calculations with Muscarine ---
#  The formula weight of Muscarine is 174.26 g/mol.
#  1.4 mol of Muscarine weight 244.0 g.
#  24.0 g of Muscarine corresponds to 137.7 mmol.
#  The elemental composition of Muscarine is as follows:
#    C : 62.03 %
#    H : 11.57 %
#    N :  8.04 %
#    O : 18.36 %
# 
# --- Is L-(+)-Muscarine Radioactive and Charged? ---
#  No, L-(+)-Muscarine is not radioactive.
#  Yes, L-(+)-Muscarine is charged.
# 
# --- Accessing Single Elements through FormulaObject.Element['Element_Symbol'] ---
#  Muscarine contains 2 oxygen atoms.
#