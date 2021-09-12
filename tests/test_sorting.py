from chemformula import ChemFormula

caffeine = ChemFormula("C8H10N4O2", name = "caffeine", cas = 58_08_2)
theine = ChemFormula("(C5N4H)O2(CH3)3", name = "theine", cas = "58-08-2")

l_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "L-lactic acid", cas = 79_33_4)
d_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "D-lactic acid", cas = 10326_41_7)

hydrocarbons = [ChemFormula("C3H5"), ChemFormula("C6H12O6"), ChemFormula("C6H12O5S"), ChemFormula("C3H5O"),
                ChemFormula("C4H5"), ChemFormula("C6H12S6"), ChemFormula("C6H12S2O3")]

print(f"\n--- Comparing {caffeine.name.capitalize()} with {theine.name.capitalize()} and Lactic Acid Isomers ---")
print(f" {caffeine.name.capitalize()} and {theine.name} are", end=" ")
print("identical.") if caffeine == theine else print("not identical.")
print(f" {l_lacticacid.name} and {d_lacticacid.name} are", end=" ")
print("identical.") if l_lacticacid == d_lacticacid else print("not identical.")

print("\n--- Lexical Sorting of Chemical Formulas via Hill Notation ---")
for position, item in enumerate(sorted(hydrocarbons), start = 1):
    print(f"{position:>3}. {item.hill_formula.unicode}")

### OUTPUT:
#
# --- Comparing Caffeine with Theine and Lactic Acid Isomers ---
#  Caffeine and theine are identical.
#  L-lactic acid and D-lactic acid are not identical.
#
# --- Lexical Sorting of Chemical Formulas via Hill Notation ---
#   1. C₃H₅
#   2. C₃H₅O
#   3. C₄H₅
#   4. C₆H₁₂O₃S₂
#   5. C₆H₁₂O₅S
#   6. C₆H₁₂O₆
#   7. C₆H₁₂S₆
#
