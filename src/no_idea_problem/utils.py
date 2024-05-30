def no_idea(n, m, arr, A, B):
    hap = 0
    x = set(A)
    y = set(B)
    for digit in arr:
        if digit in x:
            hap += 1
        elif digit in y:
            hap -= 1
    return hap