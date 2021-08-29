import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

with open("VERSION", "r") as fileVersion:
	strVersion = fileVersion.readline().strip()

setuptools.setup(
	name = "ChemFormula",
	version = strVersion,
	description = "ChemFormula is a Python class for working with chemical formulas. It allows parsing chemical formulas, generating formatted output strings and calculating formula weights.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	author = "Axel Müller",
	author_email = "molshape@gmx.net",
	maintainer = "molshape",
	maintainer_email = "molshape@gmx.net",
	url = "https://github.com/molshape/ChemFormula",
	project_urls = {
		"Bug Tracker": "https://github.com/molshape/ChemFormula/issues",
	},
	license = "LICENSE",
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Topic :: Scientific/Engineering :: Chemistry"
	],
	package_dir = {"": "src"},
	py_modules = ["ChemFormula", "Elements", "CASRegistryNumber"],
	include_package_data = True,
	python_requires = ">=3.7"
 )
