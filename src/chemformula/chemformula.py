"""
ChemFormula: A Python class for working with chemical formulas. It allows parsing chemical formulas, generating formatted output strings and calculating formula weights.
"""

from __future__ import annotations

import re
import warnings
from collections import defaultdict

import casregnum

from . import elements


# Class for chemical formula strings
class ChemFormulaString:
    """
    ChemFormulaString class for chemical formula strings with charge information

    Attributes:
    -----------
        formula : str
            Chemical (input) formula as a string
        charge : int
            Charge of the chemical formula
        charged : bool
            Boolean property whether the formula object is charged (True) or not (False)
        text_charge : str
            Text representation of the charge as a text string
        text_formula : str
            Text representation of the chemical formula including charge information
        latex : str
            LaTeX representation of the chemical formula including charge information
        html : str
            HTML representation of the chemical formula including charge information
        unicode : str
            Unicode representation of the chemical formula including charge information

    Methods:
    --------
        format_formula() : str
            Formats formula (ChemFormulaString object) as a customized strings
    """

    def __init__(self, formula: str, charge: int = 0) -> None:
        self.formula = formula
        self.charge = charge

    # formula as standard string output
    def __str__(self) -> str:
        return self.formula

    # formula as detailed string output
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(formula='{self.formula}', charge={self.charge})"

    # Returns original input formula
    @property
    def formula(self) -> str:
        """Returns the original input formula as a string."""
        return self._formula

    @formula.setter
    def formula(self, input_formula: str) -> None:
        self._formula = str(input_formula)

    # Returns the charge of the formula object
    @property
    def charge(self) -> int:
        """Returns the charge of the formula object as an integer."""
        return self._charge

    # Checks, whether the charge is valid
    @charge.setter
    def charge(self, charge: int) -> None:
        if isinstance(charge, int):
            self._charge = charge
        else:
            raise TypeError(
                f"Invalid Charge Value '{charge}' (expected an integer (<class 'int'>), but found {type(charge)})"
            )

    # Boolean property whether the formula object is charged (True) or not (False)
    @property
    def charged(self) -> bool:
        """Returns whether the formula object is charged (True) or not (False)"""
        return False if self.charge == 0 else True

    # Returns the charge of the formula object as a text string
    @property
    def text_charge(self) -> str:
        """Returns the charge of the formula object as a text string, without the number "1" for charges of ±1."""
        # a charge of "1+" or "1-" is printed without the number "1"
        charge_output = ""
        if self.charge == 0:
            return charge_output
        if not(abs(self.charge) == 1):
            charge_output = str(abs(self.charge))
        charge_output += "+" if self.charge > 0 else "-"
        return charge_output

    # Returns formula and charge as a text string
    @property
    def text_formula(self) -> str:
        """Returns the chemical formula including charge information as a text string."""
        if self.charged:
            return f"{self.formula} {self.text_charge}"
        return self.formula

    # Formats formula (ChemFormulaString object) as a customized strings
    def format_formula(self,
                       formula_prefix: str = "",
                       element_prefix: str = "", element_suffix: str = "",
                       freq_prefix: str = "", freq_suffix: str = "",
                       formula_suffix: str = "",
                       bracket_prefix: str = "", bracket_suffix: str = "",
                       multiply_symbol: str = "",
                       charge_prefix: str = "", charge_suffix: str = "",
                       charge_positive: str = "+", charge_negative: str = "-"
                       ) -> str:
        """Formats the chemical formula (ChemFormulaString object) as a customized string with user-defined prefixes and suffixes:
        Parameters:
            - formula_prefix (str): Prefix for the entire formula
            - element_prefix (str): Prefix for each element
            - element_suffix (str): Suffix for each element
            - freq_prefix (str): Prefix for each frequency
            - freq_suffix (str): Suffix for each frequency
            - formula_suffix (str): Suffix for the entire formula
            - bracket_prefix (str): Prefix for each bracket
            - bracket_suffix (str): Suffix for each bracket
            - multiply_symbol (str): Symbol for multiplication
            - charge_prefix (str): Prefix for the charge
            - charge_suffix (str): Suffix for the charge
            - charge_positive (str): Symbol for positive charge
            - charge_negative (str): Symbol for negative charge
        """
        formatted_formula = re.sub(r"([\{\[\(\)\]\}]){1}", bracket_prefix + r"\g<1>" + bracket_suffix, self.formula)
        formatted_formula = re.sub(r"([A-Z]{1}[a-z]{0,1})", element_prefix + r"\g<1>" + element_suffix, formatted_formula)
        formatted_formula = re.sub(r"(\d+)", freq_prefix + r"\g<1>" + freq_suffix, formatted_formula)
        formatted_formula = re.sub(r"[\.\*]", multiply_symbol, formatted_formula)
        # create charge string, by replacing + and - with the respective charge symbols
        charge = self.text_charge
        charge.replace("+", charge_positive)
        charge.replace("-", charge_negative)
        if self.charged:
            return formula_prefix + formatted_formula + charge_prefix + charge + charge_suffix + formula_suffix
        else:
            return formula_prefix + formatted_formula + formula_suffix

    # Returns a LaTeX representation of a formula (ChemFormulaString object)
    @property
    def latex(self) -> str:
        """Returns a LaTeX representation of the chemical formula (including charge information) as a string."""
        return self.format_formula("",
                                   r"\\textnormal{", "}",
                                   "_{", "}",
                                   "",
                                   r"\\",
                                   multiply_symbol=r"\\cdot",
                                   charge_prefix="^{", charge_suffix="}"
                                   )

    # Returns an HTML representation of a formula (ChemFormulaString object)
    @property
    def html(self) -> str:
        """Returns an HTML representation of the chemical formula (including charge information) as a string.
        Specifies the class 'ChemFormula' for custom CSS."""
        return self.format_formula("<span class='ChemFormula'>",
                                   "", "",
                                   "<sub>", "</sub>",
                                   "</span>",
                                   multiply_symbol="&sdot;",
                                   charge_prefix="<sup>", charge_suffix="</sup>",
                                   charge_negative="&ndash;"
                                   )

    # Returns formula with unicode sub- and superscripts (₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻)
    @property
    def unicode(self) -> str:
        """Returns a Unicode representation of the chemical formula (including charge information) as a string."""
        subscript_num = "₀₁₂₃₄₅₆₇₈₉"
        superscript_num = "⁰¹²³⁴⁵⁶⁷⁸⁹"
        unicode_formula = self.formula     # start with original formula
        unicode_charge = self.text_charge  # start with original text_charge
        # replace all numbers (0 - 9) by subscript numbers (for elemental frequencies)
        # and superscript numbers (for charge information)
        for number in range(0, 10):
            unicode_formula = unicode_formula.replace(str(number), subscript_num[number])
            unicode_charge = unicode_charge.replace(str(number), superscript_num[number])
        unicode_charge = unicode_charge.replace("+", "⁺")
        unicode_charge = unicode_charge.replace("-", "⁻")
        return unicode_formula + unicode_charge


# Class for chemical formula dictionaries
class ChemFormulaDict(defaultdict):
    """
    ChemFormulaDict class for chemical formula dictionaries with element symbols as keys and element frequencies as values
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(int, *args, **kwargs)  # default value for non-existing elements is 0

    def __setitem__(self, key_element: str, value_frequency: int | float) -> None:
        if key_element not in elements.get_valid_element_symbols():
            raise ValueError(
                f"Invalid Element Symbol (unknown element symbol '{key_element}')"
            )
        super().__setitem__(key_element, value_frequency)


# Class for chemical formula objects
class ChemFormula(ChemFormulaString):
    """
    ChemFormula class for chemical formula objects with formula, different representations (LaTeX, HTML, Unicode),
    formula_weight, charge, name, information on radioactivity and specific isotopes, as well as CAS registry number
    information, if provided

    Attributes (inherited from ChemFormulaString):
    ----------------------------------------------
        formula : str
            Chemical (input) formula as a string
        charge : int
            Charge of the chemical formula
        charged : bool
            Boolean property whether the formula object is charged (True) or not (False)
        text_charge : str
            Text representation of the charge as a text string
        text_formula : str
            Text representation of the chemical formula including charge information
        latex : str
            LaTeX representation of the chemical formula including charge information
        html : str
            HTML representation of the chemical formula including charge information
        unicode : str
            Unicode representation of the chemical formula including charge information

    Additional Attributes:
    ----------------------
        name : str or None
            Name of the chemical formula (if provided)
        cas : casregnum.CAS or None
            CAS registry number as a casregnum.CAS object of the chemical formula (if provided)
        element : ChemFormulaDict
            Chemical formula as a ChemFormulaDict object with (key : value) = (element symbol : element frequency)
        sum_formula : ChemFormulaDict
            Chemical formula in Hill notation as a ChemFormulaDict object with (key : value) = (element symbol : element frequency)
        hill_formula : ChemFormulaDict
            Chemical formula in Hill notation as a ChemFormulaDict object with (key : value) = (element symbol : element frequency)
        formula_weight : float
            Formula weight of the chemical formula in g/mol
        mass_fraction : ChemFormulaDict
            Mass fraction of each element as a ChemFormulaDict object with (key : value) = (element symbol : mass fraction)
        contains_isotopes : bool
            Boolean property whether the formula contains an element symbol that is refering to a specific isotope (e.g. D or Tc)
        is_radioactive : bool
            Boolean property whether the formula contains at least one radioactive element (True) or not (False)

    Methods (inherited from ChemFormulaString):
    -------------------------------------------
        format_formula() : str
            Formats formula (ChemFormulaString object) as a customized strings

    Additional Methods:
    -------------------
        __eq__() : bool
            Tests if two chemical formula objects are identical
        __lt__() : bool
            Compares two formulas with respect to their lexical sorting according to Hill's notation
    """

    def __init__(self, formula: str, charge: int = 0, name: str | None = None, cas: str | int | None = None) -> None:
        # Parent information
        ChemFormulaString.__init__(self, formula, charge)
        # Additional input information
        self.name = name
        self.cas = cas
        # parse chemical formula and test for consistency
        self._clean_formula = self._clean_up_formula()
        self._check_formula(self._clean_formula)
        self._resolved_formula = self._resolve_brackets(self._clean_formula)
        _ = self.mass_fraction  # trigger mass_fraction parsing to check for valid element symbols and atomic weights

    # Test if two chemical formla objects are identical
    def __eq__(self, other: object) -> bool:
        """Tests if two chemical formula objects are identical."""
        # two chemical formula objects are considered to be equal if they have
        # the same chemical composition (in Hill notation), the same charge,
        # and the same CAS registry number (if provided)
        if not isinstance(other, ChemFormula):
            raise TypeError("Comparisons can only be made between ChemFormula objects.")
        return (str(self.hill_formula) == str(other.hill_formula) and self.charge == other.charge and self.cas == other.cas)

    # Compares two formulas with respect to their lexical sorting according to Hill's notation
    def __lt__(self, other: object) -> bool:
        """Compares two chemical formula objects with respect to their lexical sorting according to Hill's notation."""
        if not isinstance(other, ChemFormula):
            raise TypeError("Comparisons can only be made between ChemFormula objects.")
        elements_self = tuple(self._element_hill_sorted.items())
        elements_other = tuple(other._element_hill_sorted.items())
        # cycle through the elements in Hill notation
        for i in range(0, min(len(elements_self), len(elements_other))):
            # first check for the alphabetical sorting of the element symbol
            if elements_self[i][0].lower() < elements_other[i][0].lower():
                return True
            if elements_self[i][0].lower() > elements_other[i][0].lower():
                return False
            # if the element symbol is identical, check the frequency of that element
            if elements_self[i][0] == elements_other[i][0] and elements_self[i][1] < elements_other[i][1]:
                return True
            if elements_self[i][0] == elements_other[i][0] and elements_self[i][1] > elements_other[i][1]:
                return False
            # if everything to this point is identical then:
            # the shorter formula (with less elements) is always lesser/smaller than the longer formula (with more elements)
            if len(elements_self) - 1 == i and len(elements_other) - 1 > i:
                return True
        # if everything has failed so far then Self > Other
        return False

    # Clean up chemical formula, i. e. harmonize brackets, add quantifier "1" to bracketed units without quantifier
    def _clean_up_formula(self) -> str:
        """Cleans up the input formula by harmonizing brackets, removing whitespaces, dots and asterisks,
        and adding a quantifier `1` to bracketed units without a quantifier."""
        formula = self.formula
        # for simplicity reasons: create a (...)1 around the whole formula
        formula = "(" + formula + ")1"
        # replace all type of brackets ("{", "[") by round brackets "("
        formula = re.sub(r"[\{\[\(]", "(", formula)
        formula = re.sub(r"[\)\]\}]", ")", formula)
        # replace all whitespaces, dots and asterisks
        formula = re.sub(r"[\.\s\*]+", "", formula)
        # search for brackets without a frequency information (...) and add a frequency of 1 => (...)1
        formula = re.sub(r"\)(\D)", r")1\g<1>", formula)
        return formula

    # Checks whether the formula is valid regarding bracketing
    def _check_formula(self, formula: str) -> bool:
        """Checks whether the formula is valid regarding bracketing and general element symbols conventions.
        Raises a ValueError if the formula is invalid. Element validation is done in the `ChemFormulaDict` class."""
        bracket_counter = 0
        for character in formula:
            if character == "(":
                bracket_counter += 1
            if character == ")":
                bracket_counter -= 1
                if bracket_counter < 0:  # there are more closing brackets than opening brackets during parsing formula
                    raise ValueError(
                        "Invalid Bracket Structure in Formula (expecting an opening bracket, but found a closing bracket)"
                    )
        if not bracket_counter == 0:  # number of opening brackets is not identical to the number of closing brackets
            raise ValueError(
                "Invalid Bracket Structure in Formula (inconsistent number of opening and closing brackets)"
            )
        if re.search("[a-z]{2,}", formula):  # at least two lowercase letters found in sequence
            raise ValueError(
                "Invalid Element Symbol (two lowercase letters found in sequence)"
            )
        # no error found
        return True

    # Recursively resolve all brackets in the provided formula
    def _resolve_brackets(self, formula: str) -> str:
        """Recursively resolves all brackets in the provided formula and returns a formula without any brackets as a string."""
        # stop recursion if formula contains no more brackets
        if "(" in formula:
            # find smallest bracket unit, i. e. a bracketed entity that does not contain any other brackets
            most_inner_bracket_unit = re.search(r"\(([A-Za-z0-9]*)\)(\d+)", formula)
            assert most_inner_bracket_unit is not None  # should never be None, as presence of "(" is checked above
            # remove smallest bracket unit from original formula string using match.span() and string splicing
            pre_match = formula[0:most_inner_bracket_unit.span()[0]:]  # string before the bracketed unit
            post_match = formula[most_inner_bracket_unit.span()[1]::]  # string after the bracketed unit
            inner_match = most_inner_bracket_unit.group(1)             # string of the bracketed unit
            multiplier_match = int(most_inner_bracket_unit.group(2))   # multiplier of the bracketed unit
            # find all element symbols + (optional) element frequency occurrences of inner_match
            element_freq_list = re.findall(r"[A-Z]{1}[a-z]{0,1}\d*", inner_match)
            # separate the element symbol portion from the number portion (if any) for all occurrences
            resolved_match = ""
            for element_freq_item in element_freq_list:
                element_freq = re.match(r"(\D+)(\d*)", element_freq_item)
                assert element_freq is not None  # should never be None, due to the return value of `re.findall()`
                element = element_freq.group(1)
                freq = element_freq.group(2)
                freq = 1 if not freq else freq  # if no frequency is given, set frequency to 1
                # create a resolved version of the bracketed unit and replace the bracketed unit with this resolved string
                resolved_match += str(element) + str(int(freq) * multiplier_match)
            formula = pre_match + resolved_match + post_match
            # recursively resolve brackets
            formula = self._resolve_brackets(formula)
        return str(formula)

    # Returns the formula as a dictionary with (key : value) = (element symbol : element frequency)
    @property
    def element(self) -> ChemFormulaDict:
        """Returns the chemical formula as a `ChemFormulaDict` object with (key : value) = (element symbol : element frequency)."""
        # find all occurrences of one capital letter, possibly one lower case letter and some multiplier number
        # Note: a multiplier number is always present in resolved formulas
        dict_formula = ChemFormulaDict()
        element_freq_list = re.findall(r"[A-Z]{1}[a-z]{0,1}\d+", self._resolved_formula)
        # separate for each occurrence the letter portion from the number portion (if any)
        for element_freq_item in element_freq_list:
            # separate element symbol from element frequency
            element_freq = re.match(r"(\D+)(\d+)", element_freq_item)
            assert element_freq is not None  # should never be None, due to the return value of `_resolve_brackets()`
            element = element_freq.group(1)
            freq = element_freq.group(2)
            # create a dictionary with element symbols as keys and element frequencies as values
            dict_formula[element] += int(freq)
        return ChemFormulaDict(dict_formula)

    # Return the formula as a dictionary with (key : value) = (element symbol : element frequency) in Hill sorting
    @property
    def _element_hill_sorted(self) -> ChemFormulaDict:
        """Returns the chemical formula as a `ChemFormulaDict` object in Hill notation with (key : value) = (element symbol : element frequency)."""
        dict_sorted_elements = dict(sorted(self.element.items()))
        dict_hill_sorted_elements = {}
        # extract "C" and "H" (if "C" is also present) from the original dictionary
        if "C" in dict_sorted_elements:
            dict_hill_sorted_elements["C"] = dict_sorted_elements["C"]
            del dict_sorted_elements["C"]
            if "H" in dict_sorted_elements:
                dict_hill_sorted_elements["H"] = dict_sorted_elements["H"]
                del dict_sorted_elements["H"]
        # create new Hill dictionary by placing "C" and "H" (if "C" is also present) in front of all other elements
        dict_hill_sorted_elements = dict_hill_sorted_elements | dict_sorted_elements
        return ChemFormulaDict(dict_hill_sorted_elements)

    # function to contract formula from a given (element symbol : element frequency) dictionary
    @staticmethod
    def _contract_formula(dict_element_freq: ChemFormulaDict, charge: int) -> ChemFormulaString:
        """Contracts the formula to a sum formula by generating a `ChemFormulaString` object from a given (element symbol : element frequency) dictionary."""
        formula_output = ""
        for element, freq in dict_element_freq.items():
            formula_output += element  # element symbol
            if freq > 1:
                formula_output += str(freq)  # add multipliers when they are greater than 1
        return ChemFormulaString(formula_output, charge)

    # Generate sum formula as a string
    @property
    def sum_formula(self) -> ChemFormulaString:
        """Returns the chemical formula as a `ChemFormulaString` object in sum formula notation."""
        return ChemFormula._contract_formula(self.element, self.charge)

    # Generate sum formula as a string
    # Source: Edwin A. Hill, J. Am. Chem. Soc., 1900 (22), 8, 478-494 (https://doi.org/10.1021/ja02046a005)
    @property
    def hill_formula(self) -> ChemFormulaString:
        """Returns the chemical formula as a `ChemFormulaString` object in Hill notation."""
        return ChemFormula._contract_formula(self._element_hill_sorted, self.charge)

    # Returns the formula weight of the formula object, atomic weights are taken from elements.py
    @property
    def formula_weight(self) -> float:
        """Returns the formula weight of the chemical formula in g/mol as a float."""
        float_formula_weight: float = 0.0
        for element, freq in self.element.items():
            float_formula_weight += freq * elements.atomic_weight(element)
        return float(float_formula_weight)

    # Calculate mass fractions for each element in the formula as a dictionary, atomic weights are taken from elements.py
    @property
    def mass_fraction(self) -> ChemFormulaDict:
        """Returns the mass fraction of each element as a `ChemFormulaDict` object with (key : value) = (element symbol : mass fraction)."""
        dict_mass_fraction: ChemFormulaDict = ChemFormulaDict()
        for element, freq in self.element.items():
            dict_mass_fraction[element] = float((freq * elements.atomic_weight(element)) / self.formula_weight)
        return ChemFormulaDict(dict_mass_fraction)

    # Checks, whether an element is classified as radioactive, radioactivity data is taken from elements.py
    @property
    def is_radioactive(self) -> bool:
        """Returns whether the formula contains at least one radioactive element (True) or not (False) and is therefore classified as radioactive."""
        for element in self.element:
            if elements.isradioactive(element):
                return True  # element and therefore the formula is radioactive
        return False  # no radioactive elements found and therefore no radioactive formula
    # Deprecated: use is_radioactive instead
    @property
    def radioactive(self) -> bool:
        """Deprecated: use `is_radioactive` instead. Returns whether the formula contains at least one radioactive element (True) or not (False) and is therefore classified as radioactive."""
        warnings.warn(
            "The 'radioactive' property is deprecated, use 'is_radioactive' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.is_radioactive

    # Checks, whether a specific isotop of an element is used, isotop data is taken from elements.py
    @property
    def contains_isotopes(self) -> bool:
        """Returns whether the formula contains an element symbol that is refering to a specific isotope (e.g. D or Tc)."""
        for element in self.element:
            if elements.isisotope(element):
                return True  # element is a specific isotope
        return False  # no isotopes of elements found

    # Returns the name of the formula
    @property
    def name(self) -> str | None:
        """Returns the name of the chemical formula (if provided) as a string or None."""
        return self._name

    # Makes sure, that the name of the formula is a string
    @name.setter
    def name(self, name: str | None) -> None:
        self._name = None if name is None else str(name)

    # Returns the CAS registry number of the formula object
    @property
    def cas(self) -> casregnum.CAS | None:
        """Returns the CAS registry number of the chemical formula as a `casregnum.CAS` object (if provided) or None."""
        return None if self._cas is None else self._cas

    # Checks, whether the CAS registry number is valid by using the CAS class from CASRegistryNumber.py
    @cas.setter
    def cas(self, cas_rn: int | str | None) -> None:
        self._cas = None if cas_rn is None else casregnum.CAS(cas_rn)
