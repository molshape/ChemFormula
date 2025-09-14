import chemformula.config
from chemformula import ChemFormula

chemformula.config.AllowHydrogenIsotopes = True  # Enable usage of hydrogen isotopes like Deuterium ("D") and Tritium ("T")

water = ChemFormula("H2O")
heavy_water = ChemFormula("D2O")

print("\n--- Isotopes in ChemFormula Objects ---")
print(f" Yes, {water.unicode} contains specific isotopes.") if water.contains_isotopes else print(f" No, {water.unicode} contains no specific isotopes.")  # noqa: E501
print(f" Yes, {heavy_water.unicode} contains specific isotopes.\n") if heavy_water.contains_isotopes else print(f" No, {heavy_water.unicode} contains no specific isotopes.\n")  # noqa: E501

# OUTPUT:
#
# --- Isotopes in ChemFormula Objects ---
#  No, H₂O contains no specific isotopes.
#  Yes, D₂O contains specific isotopes.
#
