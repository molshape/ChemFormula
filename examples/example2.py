from chemformula import ChemFormula

muscarine = ChemFormula("((CH3)3N)(C6H11O2)", 1, "L-(+)-Muscarine")
pyrophosphate = ChemFormula("P2O7", -4)

print("\n--- Formula Depictions of the L-(+)-Muscarine Ion ---")
print(f" Print instance: {muscarine}")
print(f" Formula:        {muscarine.formula}")
print(f" Charged:        {muscarine.charged}")
print(f" Charge (int):   {muscarine.charge}")
print(f" Charge (str):   {muscarine.text_charge}")
print(f" LaTeX:          {muscarine.latex}")
print(f" HTML:           {muscarine.html}")
print(f" Unicode:        {muscarine.unicode}")
print(f" Custom format:  {muscarine.format_formula('--> ', '', '', '_<', '>', ' <--', '', '', ' * ', '^^', '^^', '(+)', '(-)')}")
print(f" Sum formula:    {muscarine.sum_formula}")
print(f" Hill formula:   {muscarine.hill_formula}")

print("\n--- Formula Depictions of Pyrophosphate ---")
print(f" Print instance: {pyrophosphate}")
print(f" Formula:        {pyrophosphate.formula}")
print(f" Charged:        {pyrophosphate.charged}")
print(f" Charge (int):   {pyrophosphate.charge}")
print(f" Charge (str):   {pyrophosphate.text_charge}")
print(f" LaTeX:          {pyrophosphate.latex}")
print(f" HTML:           {pyrophosphate.html}")
print(f" Unicode:        {pyrophosphate.unicode}")
print(f" Custom format:  {pyrophosphate.format_formula('--> ', '', '', '_<', '>', ' <--', '', '', ' * ', '^^', '^^', '(+)', '(-)')}")
print(f" Sum formula:    {pyrophosphate.sum_formula}")
print(f" Hill formula:   {pyrophosphate.hill_formula}")

print("\n--- Formula Weights Calculations with Muscarine ---")
print(f" The formula weight of Muscarine is {muscarine.formula_weight:.2f} g/mol.")
Mole = 1.4
print(f" {Mole:.1f} mol of Muscarine weight {Mole * muscarine.formula_weight:.1f} g.")
Mass = 24
print(f" {Mass:.1f} g of Muscarine corresponds to {Mass/muscarine.formula_weight * 1000:.1f} mmol.")
print(f" The elemental composition of Muscarine is as follows:")
for stringElementSymbol, floatElementFraction in muscarine.mass_fraction.items():
	print(f"   {stringElementSymbol:<2}: {floatElementFraction * 100:>5.2f} %")

print("\n--- Is L-(+)-Muscarine Radioactive and Charged? ---")
print(f" Yes, {muscarine.name} is radioactive.") if muscarine.radioactive else print(f" No, {muscarine.name} is not radioactive.")
print(f" Yes, {muscarine.name} is charged.") if muscarine.charged else print(f" No, {muscarine.name} is not charged.")

print("\n--- Accessing Single Elements through FormulaObject.Element[\'Element_Symbol\'] ---")
print(f" Muscarine contains {muscarine.element['O']} oxygen atoms.\n")

### OUTPUT:
#
# --- Formula Depictions of the L-(+)-Muscarine Ion ---
#  Print instance: ((CH3)3N)(C6H11O2)
#  Formula:        ((CH3)3N)(C6H11O2)
#  Charged:        True
#  Charge (int):   1
#  Charge (str):   +
#  LaTeX:          \(\(\textnormal{C}\textnormal{H}_{3}\)_{3}\textnormal{N}\)\(\textnormal{C}_{6}\textnormal{H}_{11}\textnormal{O}_{2}\)^{+}
#  HTML:           <span class='ChemFormula'>((CH<sub>3</sub>)<sub>3</sub>N)(C<sub>6</sub>H<sub>11</sub>O<sub>2</sub>)<sup>+</sup></span>   
#  Unicode:        ((CH₃)₃N)(C₆H₁₁O₂)⁺
#  Custom format:  --> ((CH_<3>)_<3>N)(C_<6>H_<11>O_<2>)^^+^^ <--
#  Sum formula:    C9H20NO2
#  Hill formula:   C9H20NO2
#
# --- Formula Depictions of Pyrophosphate ---
#  Print instance: P2O7
#  Formula:        P2O7
#  Charged:        True
#  Charge (int):   -4
#  Charge (str):   4-
#  LaTeX:          \textnormal{P}_{2}\textnormal{O}_{7}^{4-}
#  HTML:           <span class='ChemFormula'>P<sub>2</sub>O<sub>7</sub><sup>4-</sup></span>
#  Unicode:        P₂O₇⁴⁻
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
