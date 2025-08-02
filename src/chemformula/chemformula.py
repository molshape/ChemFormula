import re
from collections import defaultdict

import casregnum

from . import elements


# Class for chemical formula strings
class ChemFormulaString:
    def __init__(self, formula, charge=0):
        self.formula = formula  # chemical formula
        self.charge = charge    # charge of chemical formula
        if self.charged:
            self.text_formula = self.formula + " " + self.text_charge
        else:
            self.text_formula = self.formula

    # formula as standard string output
    def __str__(self):
        return self.formula

    # Returns original input formula
    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, input_formula):
        self.__formula = str(input_formula)

    # Returns the charge of the formula object
    @property
    def charge(self):
        return self.__charge

    # Checks, whether the charge is valid
    @charge.setter
    def charge(self, charge):
        if isinstance(charge, int):
            self.__charge = charge
        else:
            raise TypeError(
                f"Invalid Charge Value '{charge}' (expected an integer (<class 'int'>), but found {type(charge)})"
            )

    # Boolean property whether the formula object is charged (True) or not (False)
    @property
    def charged(self):
        return False if self.charge == 0 else True

    # Returns the charge of the formula object as a text string
    @property
    def text_charge(self):
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
    def text_formula(self):
        return self.__text_formula

    @text_formula.setter
    def text_formula(self, text_formula_charge):
        self.__text_formula = text_formula_charge

    # Formats formula (ChemFormulaString object) as a customized strings
    def format_formula(self,
                       formula_prefix="",
                       element_prefix="", element_suffix="",
                       freq_prefix="", freq_suffix="",
                       formula_suffix="",
                       bracket_prefix="", bracket_suffix="",
                       multiply_symbol="",
                       charge_prefix="", charge_suffix="",
                       charge_positive="+", charge_negative="-"
                       ):
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
    def latex(self):
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
    def html(self):
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
    def unicode(self):
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


# Class for chemical formula objects
class ChemFormula(ChemFormulaString):
    def __init__(self, formula, charge=0, name=None, cas=None):
        # Parent information
        ChemFormulaString.__init__(self, formula, charge)
        # Additional input information
        self.name = None if name is None else name
        self.cas = None if cas is None else cas
        # parse chemical formula and test for consistency
        self.__clean_formula = self.__clean_up_formula()
        self.__check_formula(self.__clean_formula)
        self.__resolved_formula = self.__resolve_brackets(self.__clean_formula)

    # Test if two chemical formla objects are identical
    def __eq__(self, other):
        # two chemical formula objects are considered to be equal if they have
        # the same chemical composition (in Hill notation), the same charge,
        # and the same CAS registry number (if provided)
        return (str(self.hill_formula) == str(other.hill_formula) and self.charge == other.charge and self.cas == other.cas)

    # Compares two formulas with respect to their lexical sorting according to Hill's notation
    def __lt__(self, other):
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
    def __clean_up_formula(self):
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
    def __check_formula(self, formula):
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
        for element in re.findall("[A-Z]{1}[a-z]{0,1}", formula):
            if elements.atomic_weight(element) is False:
                raise ValueError(
                    f"Invalid Element Symbol (unknown element symbol '{element}')"
                )
        # no error found
        return True

    # Recursively resolve all brackets in the provided formula
    def __resolve_brackets(self, formula):
        # stop recursion if formula contains no more brackets
        if "(" in formula:
            # find smallest bracket unit, i. e. a bracketed entity that does not contain any other brackets
            most_inner_bracket_unit = re.search(r"\(([A-Za-z0-9]*)\)(\d+)", formula)
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
                element = element_freq.group(1)
                freq = element_freq.group(2)
                if not freq:
                    freq = 1  # if no number is given, use a frequency of 1
                # create a resolved version of the bracketed unit and replace the bracketed unit with this resolved string
                resolved_match += str(element) + str(int(freq) * multiplier_match)
            formula = pre_match + resolved_match + post_match
            # recursively resolve brackets
            formula = self.__resolve_brackets(formula)
        return str(formula)

    # Returns the formula as a dictionary with (key : value) = (element symbol : element frequency)
    @property
    def element(self):
        # find all occurrences of one capital letter, possibly one lower case letter and some multiplier number
        # Note: a multiplier number is always present in resolved formulas
        dict_formula = defaultdict(lambda: 0)  # if element symbol does not exist, set start frequency to 0
        element_freq_list = re.findall(r"[A-Z]{1}[a-z]{0,1}\d+", self.__resolved_formula)
        # separate for each occurrence the letter portion from the number portion (if any)
        for element_freq_item in element_freq_list:
            # separate element symbol from element frequency
            element_freq = re.match(r"(\D+)(\d+)", element_freq_item)
            element = element_freq.group(1)
            freq = element_freq.group(2)
            # create a dictionary with element symbols as keys and element frequencies as values
            dict_formula[element] += int(freq)
        return dict(dict_formula)

    # Return the formula as a dictionalry with (key : value) = (element symbol : element frequency) in Hill sorting
    @property
    def _element_hill_sorted(self):
        dict_sorted_elements = dict(sorted(self.element.items()))
        dict_hill_sorted_elements = {}
        # extract "C" and "H" (if "C" is also present) from the original dictionary
        if "C" in dict_sorted_elements.keys():
            dict_hill_sorted_elements["C"] = dict_sorted_elements["C"]
            del dict_sorted_elements["C"]
            if "H" in dict_sorted_elements.keys():
                dict_hill_sorted_elements["H"] = dict_sorted_elements["H"]
                del dict_sorted_elements["H"]
        # create new Hill dictionary by placing "C" and "H" (if "C" is also present) in front of all other elements
        dict_hill_sorted_elements = dict_hill_sorted_elements | dict_sorted_elements
        return dict(dict_hill_sorted_elements)

    # function to contract formula from a given (element symbol : element frequency) dictionary
    def _contract_formula(dict_element_freq, charge):
        formula_output = ""
        for element, freq in dict_element_freq.items():
            formula_output += element  # element symbol
            if freq > 1:
                formula_output += str(freq)  # add multipliers when they are greater than 1
        return ChemFormulaString(formula_output, charge)

    # Generate sum formula as a string
    @property
    def sum_formula(self):
        return ChemFormula._contract_formula(self.element, self.charge)

    # Generate sum formula as a string
    # Source: Edwin A. Hill, J. Am. Chem. Soc., 1900 (22), 8, 478-494 (https://doi.org/10.1021/ja02046a005)
    @property
    def hill_formula(self):
        return ChemFormula._contract_formula(self._element_hill_sorted, self.charge)

    # Returns the formula weight of the formula object, atomic weights are taken from elements.py
    @property
    def formula_weight(self):
        float_formula_weight = 0.0
        for element, freq in self.element.items():
            float_formula_weight += freq * elements.atomic_weight(element)
        return float(float_formula_weight)

    # Calculate mass fractions for each element in the formula as a dictionary, atomic weights are taken from elements.py
    @property
    def mass_fraction(self):
        dict_mass_fraction = {}
        for element, freq in self.element.items():
            dict_mass_fraction[element] = float((freq * elements.atomic_weight(element)) / self.formula_weight)
        return dict(dict_mass_fraction)

    # Checks, whether an element is classified as radioactive, radioactivitiy data is taken from elements.py
    @property
    def radioactive(self):
        for sElement in self.element.keys():
            if elements.radioactive_element(sElement):
                return True  # element and therefore the formula is radioactive
        return False  # no radioactive elements found and therefore no radioactive formula

    # Returns the name of the formula
    @property
    def name(self):
        return self.__name

    # Makes sure, that the name of the formula is a string
    @name.setter
    def name(self, name):
        self.__name = str(name)

    # Returns the CAS registry number of the formula object
    @property
    def cas(self):
        return None if self.__cas is None else self.__cas

    # Checks, whether the CAS registry number is valid by using the CAS class from CASRegistryNumber.py
    @cas.setter
    def cas(self, cas_rn):
        self.__cas = None if cas_rn is None else casregnum.CAS(cas_rn)
