def mutations(input, pos, char):
    x = list(input)
    x[pos] = char
    input = ''.join(x)
    return input
