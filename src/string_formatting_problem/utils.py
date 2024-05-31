def string_format(number):
    width = len(bin(number)[2:])
    final_out = ""
    for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width+2)
        hexa = hex(i)[2:].upper().rjust(width+2)
        binary = bin(i)[2:].rjust(width+2)
        row = f"{dec} {octal} {hexa} {binary}\n"
        final_out += row.lstrip()
    return final_out.strip()