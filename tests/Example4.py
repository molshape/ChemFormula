from ChemFormula import ChemFormula

coffein = ChemFormula("C8H10N4O2", intCharge = 0, strName = "coffein", CAS = 58_08_2)
theine = ChemFormula("(C5N4H)O2(CH3)3", strName = "theine", CAS = "58-08-2")
guaranine = ChemFormula("C5N4HO2(CH3)3", strName = "guaranine")
methyltheobromine = ChemFormula("C7H7N4O2(CH3)", strName="methyltheobromine")
theobromine = ChemFormula("C7H8N4O2", strName="theobromine")

l_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "L-lactic acid", CAS = 79_33_4)
d_lacticacid = ChemFormula("CH3(CHOH)COOH", 0, "D-lactic acid", CAS = 10326_41_7)

hydrocarbon1 = ChemFormula("C3H5")
hydrocarbon2 = ChemFormula("C3H5O")
hydrocarbon3 = ChemFormula("C4H5")
hydrocarbon4 = ChemFormula("C6H12O6")
hydrocarbon5 = ChemFormula("C6H12O5S")
hydrocarbon6 = ChemFormula("C6H12S6")
hydrocarbon7 = ChemFormula("C6H12S2O3")

hydrocarbons = [hydrocarbon1, hydrocarbon2, hydrocarbon3, hydrocarbon4, hydrocarbon5, hydrocarbon6, hydrocarbon7, ChemFormula("CaCO3"), ChemFormula("Na3PO4"), ChemFormula("Al(OH)3")]

print(f"{coffein.Name.capitalize()} and {theine.Name} are", end=" ")
print("identical.") if coffein == theine else print("not identical.")

print(f"{guaranine.Name.capitalize()} and {methyltheobromine.Name} are", end=" ")
print("identical.") if guaranine == methyltheobromine else print("not identical.")

print(f"{methyltheobromine.Name.capitalize()} and {theobromine.Name} are", end=" ")
print("identical.") if methyltheobromine == theobromine else print("not identical.")

print(f"{l_lacticacid.Name} and {d_lacticacid.Name} are", end=" ")
print("identical.") if l_lacticacid == d_lacticacid else print("not identical.")

print(f"\n{hydrocarbon1.Unicode:>10} > {hydrocarbon2.Unicode:<10} = {hydrocarbon1 > hydrocarbon2}")
print(f"{hydrocarbon2.Unicode:>10} > {hydrocarbon1.Unicode:<10} = {hydrocarbon2 > hydrocarbon1}")

print(f"{hydrocarbon1.Unicode:>10} < {hydrocarbon3.Unicode:<10} = {hydrocarbon1 < hydrocarbon3}")
print(f"{hydrocarbon3.Unicode:>10} < {hydrocarbon1.Unicode:<10} = {hydrocarbon3 < hydrocarbon1}")

print(f"{hydrocarbon4.Unicode:>10} > {hydrocarbon5.Unicode:<10} = {hydrocarbon4 > hydrocarbon5}")
print(f"{hydrocarbon4.Unicode:>10} > {hydrocarbon6.Unicode:<10} = {hydrocarbon4 > hydrocarbon6}")
print(f"{hydrocarbon5.Unicode:>10} > {hydrocarbon7.HillFormula.Unicode:<10} = {hydrocarbon5 > hydrocarbon7}\n")

for position, item in enumerate(sorted(hydrocarbons), start = 1):
    print(f"{position:>3}. {item.HillFormula.Unicode}")