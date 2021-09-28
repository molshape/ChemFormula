from chemformula import ChemFormula

coffein = ChemFormula("C8H10N4O2", charge=0, name="coffein", cas=58_08_2)  # or use CAS = "58-08-2"

print("\n--- Formula Depictions of coffein ---")
print(f" Name:           {coffein.name} ({coffein.sum_formula.unicode})")
print(f" CAS RN:         {coffein.cas}")
print(f" CAS RN (int):   {coffein.cas.cas_integer}")
print(f" Formula:        {coffein.formula}")
print(f" Original:       {coffein}")
print(f" Charged:        {coffein.charged}")
print(f" Charge (int):   {coffein.charge}")
print(f" LaTeX:          {coffein.latex}")
print(f" HTML:           {coffein.html}")
print(f" Custom format:  {coffein.format_formula('--> ', '', '', '_<', '>', ' <--', '', '', ' * ')}")
print(f" Sum formula:    {coffein.sum_formula}")
print(f" Hill formula:   {coffein.hill_formula}")
print(f" Formula Weight: {coffein.formula_weight:.1f} g/mol\n")

# OUTPUT:
#
# --- Formula Depictions of coffein ---
#  Name:           coffein (C₈H₁₀N₄O₂)
#  CAS RN:         58-08-2
#  CAS RN (int):   58082
#  Print instance: C8H10N4O2
#  Original:       C8H10N4O2
#  Charged:        False
#  Charge (int):   0
#  LaTeX:          \textnormal{C}_{8}\textnormal{H}_{10}\textnormal{N}_{4}\textnormal{O}_{2}
#  HTML:           <span class='ChemFormula'>C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub></span>
#  Custom format:  --> C_<8>H_<10>N_<4>O_<2> <--
#  Sum formula:    C8H10N4O2
#  Hill formula:   C8H10N4O2
#  Formula Weight: 194.2 g/mol
#
