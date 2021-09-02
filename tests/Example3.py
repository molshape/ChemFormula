from ChemFormula import ChemFormula

coffein = ChemFormula("C8H10N4O2", Charge = 0, Name = "coffein", CAS = 58_08_2)  # or use CAS = "58-08-2"

print("\n--- Formula Depictions of coffein ---")
print(f" Name:           {coffein.Name} ({coffein.SumFormula.Unicode})")
print(f" CAS RN:         {coffein.CAS}")
print(f" CAS RN (int):   {coffein.CASint}")
print(f" Print instance: {coffein.OriginalFormula}")
print(f" Original:       {coffein}")
print(f" Charged:        {coffein.Charged}")
print(f" Charge (int):   {coffein.Charge}")
print(f" LaTeX:          {coffein.LaTeX}")
print(f" HTML:           {coffein.HTML}")
print(f" Custom format:  {coffein.FormatFormula('--> ', '', '', '_<', '>', ' <--', '', '', ' * ')}")
print(f" Sum formula:    {coffein.SumFormula}")
print(f" Hill formula:   {coffein.HillFormula}")
print(f" Formula Weight: {coffein.FormulaWeight:.1f} g/mol\n")

### OUTPUT:
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