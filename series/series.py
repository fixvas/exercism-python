def slices(digits, n):
    res = []
    if n > len(digits) or n == 0:
        raise ValueError
    while len(digits) - n >= 0:
        res.append([int(x) for x in digits[0:n]])
        digits = digits[1:]
    return res
