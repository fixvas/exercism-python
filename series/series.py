def slices(digits, n):
    res = []
    if n > len(digits) or n == 0:
        raise ValueError
    for i in range(len(digits) - n + 1):
        res.append([int(char) for char in digits[i:i+n]])
    return res
