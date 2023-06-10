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

print(fractal_to_binary(0.3))