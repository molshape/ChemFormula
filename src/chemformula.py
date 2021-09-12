import re
import elements
import casregnum
from collections import defaultdict

### Class for chemical formula objects 
class ChemFormula:

    def __init__(self, Formula, Charge = 0, Name = None, CAS = None):
        # Input information
        self.OriginalFormula = Formula
        self.Name = None if Name is None else Name
        # Charge information
        self.Charge = Charge
        # CAS information
        self.CAS = None if CAS is None else CAS
        # parse chemical formula and test for consistency
        self.__CleanFormula = self.__CleanUpFormula()
        self.__CheckFormula(self.__CleanFormula)
        self.__ResolvedFormula = self.__ResolveBrackets(self.__CleanFormula)

    ### OriginalFormula as standard string output
    def __str__(self):
        return self.OriginalFormula  # has been changed with v1.2.4

    ### Test if two chemical formla objects are identical
    ### new in v1.2.5
    def __eq__(self, other):
        # two chemical formula objects are considered to be equal if they have the same chemical composition (in Hill notation),
        # the same charge, and the same CAS registry number (if provided)
        return (str(self.HillFormula) == str(other.HillFormula) and self.Charge == other.Charge and self.CAS == other.CAS)

    ### Compares two formulas with respect to their lexical sorting according to Hill's notation
    ### new in v1.2.5
    def __lt__(self, other):
        tupElementsSelf = tuple(self.HillFormula.Element.items())
        tupElementsOther = tuple(other.HillFormula.Element.items())
        # cycle through the elements in Hill notation
        for i in range(0,min(len(tupElementsSelf), len(tupElementsOther))):
            # first check for the alphabetical sorting of the element symbol
            if tupElementsSelf[i][0].lower() < tupElementsOther[i][0].lower(): return True
            if tupElementsSelf[i][0].lower() > tupElementsOther[i][0].lower(): return False
            # if the element symbol is identical, check the frequency of that element
            if tupElementsSelf[i][0] == tupElementsOther[i][0] and tupElementsSelf[i][1] < tupElementsOther[i][1]: return True
            if tupElementsSelf[i][0] == tupElementsOther[i][0] and tupElementsSelf[i][1] > tupElementsOther[i][1]: return False
            # if everything to this point is identical then:
            # the shorter formula (with less elements) is always lesser than the longer formula (with more elements)
            if len(tupElementsSelf)-1 == i and len(tupElementsOther)-1 > i: return True
        # if everything has failed so far then Self > Other
        return False

    ### Clean up chemical formula, i. e. harmonize brackets, add quantifier "1" to bracketed units without quantifier
    def __CleanUpFormula(self):
        sFormula = self.OriginalFormula
        # for simplicity reasons: create a (...)1 around the whole formula
        sFormula = "(" + sFormula + ")1"
        # replace all type of brackets ("{", "[") by round brackets "("
        sFormula = re.sub("[\{\[\(]", "(", sFormula)
        sFormula = re.sub("[\)\]\}]", ")", sFormula)
        # replace all whitespaces, dots and asterisks
        sFormula = re.sub("[\.\s\*]+", "", sFormula)
        # search for brackets without a frequency information (...) and add a frequency of 1 => (...)1
        reBrackets = re.compile("\)(\D)")
        sFormula = reBrackets.sub(")1\g<1>", sFormula)
        return sFormula

    ### Checks whether the formula is valid regarding bracketing
    def __CheckFormula(self, strFormula):
        iBracketCounter = 0
        for sChar in strFormula:
            if sChar == "(": iBracketCounter += 1
            if sChar == ")": iBracketCounter -= 1
            if iBracketCounter < 0:  # there are more closing brackets than opening brackets during parsing formula
                raise ValueError("Invalid Bracket Structure in Formula (expecting an opening bracket, but found a closing bracket)")
                return False
        if not iBracketCounter == 0:  # number of opening brackets is not identical to the number of closing brackets
            raise ValueError("Invalid Bracket Structure in Formula (inconsistent number of opening and closing brackets)")
            return False
        if re.search("[a-z]{2,}", strFormula):  # at least two lowercase letters found in sequence
            raise ValueError("Invalid Element Symbol (two lowercase letters found in sequence)")
            return False
        for sElement in re.findall("[A-Z]{1}[a-z]{0,1}", strFormula):
            if elements.atomic_weight(sElement) == False:
                raise ValueError(f"Invalid Element Symbol (unknown element symbol '{sElement}')")
                return False
        # no error found     
        return True

    ### Recursively resolve all brackets in the provided formula
    def __ResolveBrackets(self, strFormula): 
        # stop recursion if formula contains no more brackets
        if "(" in strFormula:
            # find smallest bracket unit, i. e. a bracketed entity that does not contain any other brackets
            matchSmallestBracketUnit = re.search("\(([A-Za-z0-9]*)\)(\d+)", strFormula)
            # remove smallest bracket unit from original formula string using match.span() and string splicing
            sPreMatch = strFormula[0:matchSmallestBracketUnit.span()[0]:]  # string before the bracketed unit
            sPostMatch = strFormula[matchSmallestBracketUnit.span()[1]::]  # string after the bracketed unit
            sMatch = matchSmallestBracketUnit.group(1)                     # string of the bracketed unit
            iMatchMultiplier = int(matchSmallestBracketUnit.group(2))      # multiplier of the bracketed unit
            # find all element symbols + (optional) element frequency occurrences
            lstElementFreq = re.findall("[A-Z]{1}[a-z]{0,1}\d*", sMatch)
            # separate the element symbol portion from the number portion (if any) for all occurrence
            sMatchResolved = ""
            for sElementFreq in lstElementFreq:
                lstElementFreqSep = re.match("(\D+)(\d*)", sElementFreq)
                sElement = lstElementFreqSep.group(1)
                sFreq = lstElementFreqSep.group(2)
                if not sFreq: sFreq = 1  # if no number is given, use a frequency of 1
                # create a resolved version of the bracketed unit and replace the bracketed unit with this resolved string
                sMatchResolved += str(sElement) + str(int(sFreq) * iMatchMultiplier) 
            strFormula = sPreMatch + sMatchResolved + sPostMatch  
            # recursively resolve brackets
            strFormula = self.__ResolveBrackets(strFormula)
        return str(strFormula)

    ### Returns the formula as a dictionary with (key : value) = (element symbol : element frequency)
    @property 
    def Element(self):
        # find all occurrences of one capital letter, possibly one lower case letter and some multiplier number
        # Note: a multiplier number is always present in resolved formulas
        dictFormula = defaultdict(lambda: 0)  # if element symbol does not exist, set start frequency to 0
        lstElementFreq = re.findall("[A-Z]{1}[a-z]{0,1}\d+", self.__ResolvedFormula)
        # separate for each occurrence the letter portion from the number portion (if any)  
        for sElementFreq in lstElementFreq:
            # separate element symbol from element frequency
            lstElementFreqSep = re.match("(\D+)(\d+)", sElementFreq)
            sElement = lstElementFreqSep.group(1)
            sFreq = lstElementFreqSep.group(2)
            # create a dictionary with element symbols as keys and element frequencies as values
            dictFormula[sElement] += int(sFreq)
        return dict(dictFormula)

    ### Generate sum formula as a string
    @property
    def SumFormula(self):
        sFormula = ""
        for sElement, sFreq in self.Element.items():
            sFormula += sElement  # element symbol
            if sFreq > 1: sFormula += str(sFreq)  # add multipliers when they are greater than 1
        cas_rn = None if self.CAS is None else self.CAS.cas_integer
        return ChemFormula(str(sFormula), self.Charge, self.Name, cas_rn)  # has been changed with v1.2.4

    ### Generate sum formula as a string (include multiplier 1 if bVerbose == True)
    ### Source: Edwin A. Hill, J. Am. Chem. Soc., 1900 (22), 8, 478-494 (https://doi.org/10.1021/ja02046a005)
    @property
    def HillFormula(self):
        # sort dictionary alphabetically
        dictSortedElements = dict(sorted(self.Element.items()))
        dictHill = {}
        sFormula = ""
        # extract "C" and "H" from the original dictionary
        if "C" in dictSortedElements.keys():
            dictHill["C"] = dictSortedElements["C"]
            del dictSortedElements["C"]
            if "H" in dictSortedElements.keys():
                dictHill["H"] = dictSortedElements["H"]
                del dictSortedElements["H"]
        # create Hill dictionary by placing "C" and "H" (if "C" is also present) in front of all other elements
        dictHill = dictHill | dictSortedElements
        # create String output
        for sElement, sFreq in dictHill.items():
            sFormula += sElement  # element symbol
            if sFreq > 1: sFormula += str(sFreq)  # add multipliers when they are greater than 1 
        cas_rn = None if self.CAS is None else self.CAS.cas_integer
        return ChemFormula(str(sFormula), self.Charge, self.Name, cas_rn)  # has been changed with v1.2.4

    ### Returns the formula weight of the formula object, atomic weights are taken from elements.py
    @property
    def FormulaWeight(self):
        fltFormulaWeight = 0.0
        for sElement, sFreq in self.Element.items(): fltFormulaWeight += sFreq * elements.atomic_weight(sElement)
        return float(fltFormulaWeight)

    ### Calculate mass fractions for each element in the formula as a dictionary, atomic weights are taken from elements.py
    @property
    def MassFraction(self):
        dictMassFraction = {}
        for sElement, sFreq in self.Element.items():
            dictMassFraction[sElement] = float((sFreq * elements.atomic_weight(sElement))/self.FormulaWeight)
        return dict(dictMassFraction) 

    ### Checks, whether an element is classified as radioactive, radioactivitiy data is taken from elements.py
    @property
    def Radioactive(self):
        for sElement in self.Element.keys():
            if elements.radioactive_element(sElement): return True  # element and therefore the formula is radioactive
        return False  # no radioactive elements found and therefore no radioactive formula

    ### Returns the original input formula of the formula object
    @property
    def OriginalFormula(self):
        return self.__OriginalFormula

    ### Makes sure, that the name of the formula is a string
    @OriginalFormula.setter
    def OriginalFormula(self, sFormula):
        self.__OriginalFormula = str(sFormula)

    ### Returns the name of the formula
    @property
    def Name(self):
        return self.__Name

    ### Makes sure, that the name of the formula is a string
    @Name.setter
    def Name(self, sName):
        self.__Name = str(sName)

    ### Returns the charge of the formula object
    @property
    def Charge(self):
        return self.__Charge

    ### Checks, whether the charge is valid
    @Charge.setter
    def Charge(self, intCharge):
        if isinstance(intCharge, int): self.__Charge = intCharge
        else: raise TypeError(f"Invalid Charge Value '{intCharge}' (expected an integer (<class 'int'>), but found {type(intCharge)})")

    ### Boolean property whether the formula object is charged (True) or not (False)
    @property
    def Charged(self):
        return False if self.Charge == 0 else True

    ### Returns a text string of the charge
    @property
    def TextCharge(self):
        # a charge of "1+" or "1-" is printed without the number "1"
        sCharge = ""
        if self.Charge == 0: return sCharge
        if not(abs(self.Charge) == 1): sCharge = str(abs(self.Charge))
        sCharge += "+" if self.Charge > 0 else "-"
        return sCharge

    ### Returns the CAS registry number of the formula object
    @property
    def CAS(self):
        return None if self.__CAS is None else self.__CAS

    ### Checks, whether the CAS registry number is valid by using the CAS class from CASRegistryNumber.py
    @CAS.setter
    def CAS(self, cas_rn):
        self.__CAS = None if cas_rn is None else casregnum.CAS(cas_rn)

    ### Formats formula in customized strings
    def FormatFormula(self, strFormulaPrefix = "", strElementPrefix = "", strElementSuffix = "", strFreqPrefix = "", strFreqSuffix = "", strFormulaSuffix = "", strBracketPrefix = "", strBracketSuffix = "", strMultiplySymbol = "", strChargePrefix = "", strChargeSuffix = "", strChargePositive = "+", strChargeNegative = "-"):
        sFormattedFormula = re.sub("([\{\[\(\)\]\}]){1}", strBracketPrefix + "\g<1>" + strBracketSuffix, self.OriginalFormula)
        sFormattedFormula = re.sub("([A-Z]{1}[a-z]{0,1})", strElementPrefix + "\g<1>" + strElementSuffix, sFormattedFormula)
        sFormattedFormula = re.sub(r"(\d+)", strFreqPrefix + "\g<1>" + strFreqSuffix, sFormattedFormula)
        sFormattedFormula = re.sub("[\.\*]", strMultiplySymbol, sFormattedFormula)
        # create charge string, by replacing + and - with the respective charge symbols
        sCharge = self.TextCharge
        sCharge.replace("+", strChargePositive)
        sCharge.replace("-", strChargeNegative)
        if self.Charged: return strFormulaPrefix + sFormattedFormula + strChargePrefix + sCharge + strChargeSuffix + strFormulaSuffix
        else: return strFormulaPrefix + sFormattedFormula + strFormulaSuffix

    ### returns a LaTeX representation of the formula object 
    @property
    def LaTeX(self):
        return self.FormatFormula("", r"\\textnormal{","}","_{","}","", r"\\", strMultiplySymbol=r"\\cdot", strChargePrefix="^{", strChargeSuffix="}")

    ### returns an HTML representation of the formula object 
    @property
    def HTML(self):
        return self.FormatFormula("<span class='ChemFormula'>","","","<sub>","</sub>","</span>", strMultiplySymbol="&sdot;", strChargeNegative="&ndash;", strChargePrefix="<sup>", strChargeSuffix="</sup>")

    ### returns formula with unicode sub- and superscripts (₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻)
    ### new in v1.2.3
    @property
    def Unicode(self):
        sSubscriptNumbers = u"₀₁₂₃₄₅₆₇₈₉"
        sSuperscriptNumbers = u"⁰¹²³⁴⁵⁶⁷⁸⁹"
        sUnicodeFormula = self.OriginalFormula
        sUnicodeCharge = self.TextCharge
        # replace all numbers (0 - 9) by subscript numbers (for elemental frequencies) and superscript numbers (for charge information)
        for iNumber in range(0,10):
            sUnicodeFormula = sUnicodeFormula.replace(str(iNumber), sSubscriptNumbers[iNumber])
            sUnicodeCharge = sUnicodeCharge.replace(str(iNumber), sSuperscriptNumbers[iNumber])
        sUnicodeCharge = sUnicodeCharge.replace("+", u"⁺")
        sUnicodeCharge = sUnicodeCharge.replace("-", u"⁻")
        return sUnicodeFormula + sUnicodeCharge
