from chemformula import ChemFormula

caffeine = ChemFormula("C8H10N4O2", charge=0, name="caffeine", cas=58_08_2)
theine = ChemFormula("(C5N4H)O2(CH3)3", name="theine", cas="58-08-2")
guaranine = ChemFormula("C5N4HO2(CH3)3", name="guaranine")
methyltheobromine = ChemFormula("C7H7N4O2(CH3)", name="methyltheobromine")
theobromine = ChemFormula("C7H8N4O2", name="theobromine")

l_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "L-lactic acid", cas=79_33_4)
d_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "D-lactic acid", cas=10326_41_7)

hydrocarbon1 = ChemFormula("C3H5")
hydrocarbon2 = ChemFormula("C3H5O")
hydrocarbon3 = ChemFormula("C4H5")
hydrocarbon4 = ChemFormula("C6H12O6")
hydrocarbon5 = ChemFormula("C6H12O5S")
hydrocarbon6 = ChemFormula("C6H12S6")
hydrocarbon7 = ChemFormula("C6H12S2O3")

hydrocarbons = [
    hydrocarbon1,
    hydrocarbon2,
    hydrocarbon3,
    hydrocarbon4,
    hydrocarbon5,
    hydrocarbon6,
    hydrocarbon7,
    ChemFormula("CaCO3"),
    ChemFormula("Na3PO4"),
    ChemFormula("Al(OH)3"),
]

print(f"{caffeine.name.capitalize()} and {theine.name} are", end=" ")
print("identical.") if caffeine == theine else print("not identical.")

print(f"{guaranine.name.capitalize()} and {methyltheobromine.name} are", end=" ")
print("identical.") if guaranine == methyltheobromine else print("not identical.")

print(f"{methyltheobromine.name.capitalize()} and {theobromine.name} are", end=" ")
print("identical.") if methyltheobromine == theobromine else print("not identical.")

print(f"{l_lacticacid.name} and {d_lacticacid.name} are", end=" ")
print("identical.") if l_lacticacid == d_lacticacid else print("not identical.")

print(f"\n{hydrocarbon1.unicode:>10} > {hydrocarbon2.unicode:<10} = {hydrocarbon1 > hydrocarbon2}")
print(f"{hydrocarbon2.unicode:>10} > {hydrocarbon1.unicode:<10} = {hydrocarbon2 > hydrocarbon1}")

print(f"{hydrocarbon1.unicode:>10} < {hydrocarbon3.unicode:<10} = {hydrocarbon1 < hydrocarbon3}")
print(f"{hydrocarbon3.unicode:>10} < {hydrocarbon1.unicode:<10} = {hydrocarbon3 < hydrocarbon1}")

print(f"{hydrocarbon4.unicode:>10} > {hydrocarbon5.unicode:<10} = {hydrocarbon4 > hydrocarbon5}")
print(f"{hydrocarbon4.unicode:>10} > {hydrocarbon6.unicode:<10} = {hydrocarbon4 > hydrocarbon6}")
print(f"{hydrocarbon5.unicode:>10} > {hydrocarbon7.hill_formula.unicode:<10} = {hydrocarbon5 > hydrocarbon7}\n")

for position, item in enumerate(sorted(hydrocarbons), start=1):
    print(f"{position:>3}. {item.hill_formula.unicode}")

# OUTPUT:
#
# Caffeine and theine are identical.
# Guaranine and methyltheobromine are identical.
# Methyltheobromine and theobromine are not identical.
# L-lactic acid and D-lactic acid are not identical.
#
#       C???H??? > C???H???O      = False
#      C???H???O > C???H???       = True
#       C???H??? < C???H???       = True
#       C???H??? < C???H???       = False
#    C???H??????O??? > C???H??????O???S   = True
#    C???H??????O??? > C???H??????S???    = False
#   C???H??????O???S > C???H??????O???S???  = True
#
#   1. AlH???O???
#   2. CCaO???
#   3. C???H???
#   4. C???H???O
#   5. C???H???
#   6. C???H??????O???S???
#   7. C???H??????O???S
#   8. C???H??????O???
#   9. C???H??????S???
#  10. Na???O???P
#
