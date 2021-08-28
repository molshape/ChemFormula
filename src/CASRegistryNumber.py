import re

### Class for CAS Registry Numbers
class CAS:

    def __init__(self, CAS_RN):
        # input CAS_RN is an integer
        if isinstance(CAS_RN, int):
            self.CASint = CAS_RN
            # convert integer into (formatted) CAS string
            reCAS_RN = re.compile("(\d{2,7})(\d{2})(\d{1})")
            self.CAS = reCAS_RN.sub("\g<1>-\g<2>-\g<3>", str(CAS_RN))
        # input CAS_RN is a string
        elif isinstance(CAS_RN, str): self.CAS = CAS_RN
        # input CAS_RN is neither an integer nor a string
        else: raise TypeError(f"Invalid CAS Registry Number format '{CAS_RN}' (expected an integer (<class 'int'>) or a string (<class 'str'>), but found {type(CAS_RN)})")
        # extract check digit = last digit of the CAS number
        self.CheckDigit = int(str(CAS_RN)[-1])

    def __str__(self):
        return self.CAS
    
    ### Returns CAS Registry Number
    @property
    def CAS(self):
        return self.__sCAS
    
    ### Sets CAS Registry Number
    ###    if the passed input value is a string, parse the string according to _____00-00-0
    ###    if the passed input value is an integer, create the string arrocing to _____00-00-0
    @CAS.setter
    def CAS(self, CAS_RN):
        # convert (formatted) CAS string into integer
        reCAS_RN = re.match("(\d{2,7})\-(\d{2})-(\d{1})", CAS_RN) 
        if reCAS_RN: self.CASint = self.__iCAS = int(reCAS_RN.group(1) + reCAS_RN.group(2) + reCAS_RN.group(3))
        # CAS_RN is not following the notation rule for CAS numbers => ValueError
        else: raise ValueError(f"Invalid CAS number format for '{CAS_RN}' (must follow the notation _____00-00-0)")
        self.__sCAS = CAS_RN
    
    ### Returns CAS Registry Number as an integer (without the hyphens)
    @property
    def CASint(self):
        return self.__iCAS

    @CASint.setter
    def CASint(self, CAS_RN):
        # by definition, the lowest theoretical CAS number is 10-00-4,
        # the officially lowest CAS number on record is 35-66-5 (Source: https://twitter.com/CASChemistry/status/1144222698740092929)
        if CAS_RN < 10004: raise TypeError(f"Invalid CAS number '{CAS_RN}' (must be an integer >= 10004)")
        self.__iCAS = CAS_RN

    ### Returns check digit of the CAS Registry Number
    @property
    def CheckDigit(self):
        return self.__iCheckDigit
    
    ### Sets the CAS Registry Number check digit
    @CheckDigit.setter
    def CheckDigit(self, iCheckDigit):
        # check if the check digit fits to the CAS Number
        # Source: https://www.cas.org/support/documentation/chemical-substances/checkdig
        # get the CAS number without the check digit (integer value of CASint/10) => change integer into string => reverse string
        sCASDigits = str(int(self.CASint/10))[::-1]
        # calculate check sum
        iCheckSum = 0
        for iPosition, sSingleDigit in enumerate(sCASDigits, start=1): iCheckSum += iPosition * int(sSingleDigit)
        # test (check sum mod 10) against check digit
        if iCheckSum % 10 != int(iCheckDigit): raise ValueError(f"Invalid CAS number '{self.CAS}' (found check digit '{iCheckDigit}', but expected '{iCheckSum % 10}')")
        self.__iCheckDigit = int(iCheckDigit)