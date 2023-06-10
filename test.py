def fractal_to_binary(fraction):
    out = ""
    while fraction > 0:
        # Multiply the fraction by 2
        fraction *= 2

        # Append the integer part of the fraction to the binary list
        out += str(int(fraction))

        # Update the fraction to the fractional part
        fraction -= int(fraction)

    return out

print(fractal_to_binary(0.365))

def Frac2Bin(prec):                #Tutaj jest babol
        frac = prec
        binRep = ""
        for i in range(23):
            frac *= 2
            binRep += str(int(frac / 10**prec))
            frac %= 10**prec
        return(binRep)

print(Frac2Bin(0.365))