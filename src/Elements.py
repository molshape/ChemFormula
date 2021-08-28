'''
ATOMIC WEIGHTS OF THE ELEMENTS (2019)
from the IUPAC Commission on Isotopic Abundances and Atomic Weights

Based on the following reports:
	- Pure Appl. Chem., 2016, 88, 265-291	(https://doi.org/10.1515/pac-2015-0305)
	- Chem. Eng. News, 2015, 93(37), 9		(https://doi.org/10.1021/cen-09337-notw9)
	- Pure Appl. Chem., 2016, 88, 139-153	(https://doi.org/10.1515/pac-2015-0502)
	- Pure Appl. Chem., 2016, 88, 155-160	(https://doi.org/10.1515/pac-2015-0501)
	- Pure Appl. Chem., 2016, 88, 1225-1229	(https://doi.org/10.1515/pac-2016-0501)
	- Chem. Int., 2018, 40(4), 23-24		(https://doi.org/10.1515/ci-2018-0409)
	- Chem. Int., 2020, 42(2), 31			(https://doi.org/10.1515/ci-2020-0222)

Data taken from: https://www.qmul.ac.uk/sbcs/iupac/AtWt/

Quoted atomic weights are those suggested for materials where the origin of the sample is unknown.
For radioactive elements the isotope with the longest half-life is quoted as an integer.
'''

def AtomicWeight(strElement):
	dictAtomicWeightTable = {
	"H":    1.008,
	"He":   4.002602,
	"Li":   6.94,
	"Be":   9.0121831,
	"B":   10.81,
	"C":   12.011,
	"N":   14.007,
	"O":   15.999,
	"F":   18.998403163,
	"Ne":  20.1797,
	"Na":  22.98976928,
	"Mg":  24.305,
	"Al":  26.9815384,
	"Si":  28.085,
	"P":   30.973761998,
	"S":   32.06,
	"Cl":  35.45,
	"Ar":  39.948,
	"K":   39.0983,
	"Ca":  40.078,
	"Sc":  44.955908,
	"Ti":  47.867,
	"V":   50.9415,
	"Cr":  51.9961,
	"Mn":  54.938043,
	"Fe":  55.845,
	"Co":  58.933194,
	"Ni":  58.6934,
	"Cu":  63.546,
	"Zn":  65.38,
	"Ga":  69.723,
	"Ge":  72.630,
	"As":  74.921595,
	"Se":  78.971,
	"Br":  79.904,
	"Kr":  83.798,
	"Rb":  85.4678,
	"Sr":  87.62,
	"Y":   88.90584,
	"Zr":  91.224,
	"Nb":  92.90637,
	"Mo":  95.95,
	"Tc":  97,
	"Ru": 101.07,
	"Rh": 102.90549,
	"Pd": 106.42,
	"Ag": 107.8682,
	"Cd": 112.414,
	"In": 114.818,
	"Sn": 118.710,
	"Sb": 121.760,
	"Te": 127.60,
	"I":  126.90447,
	"Xe": 131.293,
	"Cs": 132.90545196,
	"Ba": 137.327,
	"La": 138.90547,
	"Ce": 140.116,
	"Pr": 140.90766,
	"Nd": 144.242,
	"Pm": 145,
	"Sm": 150.36,
	"Eu": 151.964,
	"Gd": 157.25,
	"Tb": 158.925354,
	"Dy": 162.500,
	"Ho": 164.930328,
	"Er": 167.259,
	"Tm": 168.934218,
	"Yb": 173.045,
	"Lu": 174.9668,
	"Hf": 178.486,
	"Ta": 180.94788,
	"W":  183.84,
	"Re": 186.207,
	"Os": 190.23,
	"Ir": 192.217,
	"Pt": 195.084,
	"Au": 196.966570,
	"Hg": 200.592,
	"Tl": 204.38,
	"Pb": 207.2,
	"Bi": 208.98040,
	"Po": 209,
	"At": 210,
	"Rn": 222,
	"Fr": 223,
	"Ra": 226,
	"Ac": 227,
	"Th": 232.0377,
	"Pa": 231.03588,
	"U":  238.02891,
	"Np": 237,
	"Pu": 244,
	"Am": 243,
	"Cm": 247,
	"Bk": 247,
	"Cf": 251,
	"Es": 252,
	"Fm": 257,
	"Md": 258,
	"No": 259,
	"Lr": 262,
	"Rf": 267,
	"Db": 270,
	"Sg": 269,
	"Bh": 270,
	"Hs": 270,
	"Mt": 278,
	"Ds": 281,
	"Rg": 281,
	"Cn": 285,
	"Nh": 286,
	"Fl": 289,
	"Mc": 289,
	"Lv": 293,
	"Ts": 293,
	"Og": 294
	}
	# return atomic weight of the element symbol passed to the function, False if element symbol does not exist
	return float(dictAtomicWeightTable[strElement]) if strElement in dictAtomicWeightTable else False

def RadioactiveElement(strElement):
	lstRadioactiveElements = [
		"Tc",
		"Po", "At", "Rn",
		"Fr", "Ra", "Pm", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",
		"Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"
	]
	# element is in the list of radioactive elements => True else False
	return True if strElement in lstRadioactiveElements else False