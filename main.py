import math

class FP_Converter_To_Bin:
    def __init__ (self, number):
        self.number = number
        self.binRepresentation = 0
    
    def SplitDotNum(self):
        if isinstance(self.number, float):
            frac, whole = math.modf(self.number)
            return [whole, frac]
        else:
            return [self.number, 0]

    def ReturnFracWhole(self):
        return self.SplitDotNum()

    def ReturnFrac(self):
        return abs(self.SplitDotNum()[1])
    
    def ReturnFracWithPrec(self):
        i =  str(abs(int(self.ReturnFrac()*(10**10))))
        i2r = 0
        for index, x in enumerate(i[::-1]):
            if int(x) > 0:
                break
            i2r = len(i) - index
        return int(i[0:i2r-1])
    
    def ReturnWhole(self):
        return abs(int(self.SplitDotNum()[0]))
    
    def ReturnMantisa(self):
        return((self.GetExpBits()+self.Frac2Bin(1))[0:23])

    def ReturnExponent(self):
        return(self.Exp2Bin(127 + self.GetExpBitsLen()))

    def Whole2Bin(self):
        whole = self.ReturnWhole()
        binRep = ""
        while whole >= 1:
            binRep += str(whole%2)
            whole = int(whole/2)
        return binRep[::-1]
    
    def Frac2Bin(self, prec):                #Tutaj jest babol
        frac = self.ReturnFracWithPrec()
        binRep = ""
        for i in range(self.GetFracRange()):
            frac *= 2
            binRep += str(int(frac / 10**prec))
            frac %= 10**prec
        return(binRep)
    
    def Exp2Bin(self, _whole):
        whole = _whole
        binRep = ""
        while whole >= 1:
            binRep += str(whole%2)
            whole = int(whole/2)
        return binRep[::-1]

    def GetFracRange(self):
        return 32 - (self.GetExpBitsLen() + 1)
    
    def GetSignBit(self):
        if self.ReturnFracWhole()[0] < 0:
            return "1"
        else:
            return "0"
        
    def GetExpBits(self):
        return self.Whole2Bin()[1:]
        
    def GetExpBitsLen(self):
        return len(self.GetExpBits())
    
    def PrintSimpleBinaryNotation(self):
        print(f"{self.Whole2Bin()}.{self.Frac2Bin(1)}")
    
    def PrintScientificNotation(self):
        print("1."+self.GetExpBits()+self.Frac2Bin(1) + " * 2^"+ str(self.GetExpBitsLen()))
    
    def PrintFinalNumber(self):
        print( '\033[96m' + self.GetSignBit() + '\033[0m\033[92m' +  self.ReturnExponent() + '\033[0m\033[93m' + self.ReturnMantisa() + '\033[0m')

    def PrettyPrint(self):
        print("  " + '\033[96m' + self.GetSignBit()+ '\033[0m\033[92m' + (" "*3) + self.ReturnExponent() + '\033[0m\033[93m' + "  "+ self.ReturnMantisa() + '\033[0m')
        print('\033[96m' + "SIGN" + '\033[0m\033[92m' + "  EXPONENT" + '\033[0m\033[93m' + "         Mantissa" + '\033[0m')


newInst = FP_Converter_To_Bin(263.365)
print(newInst.ReturnFracWhole())
print(newInst.Whole2Bin())
print(newInst.GetFracRange())
print(newInst.Frac2Bin(1))
print("Simple Binary Notation")
newInst.PrintSimpleBinaryNotation()
print("Scientific Notation")
newInst.PrintScientificNotation()
print("Bit sign")
print(newInst.GetSignBit())
print("Exponent")
print(newInst.ReturnExponent())
print("Mantissa")
print(newInst.ReturnMantisa())
print("Final transfer looks like:")
newInst.PrintFinalNumber()
print("Print goes brrrrrrrrrrrrrrrrrrrrrrrrrr\n")
newInst.PrettyPrint()
print(newInst.ReturnFracWithPrec())