def sum_of_multiples(limit, vector):
    multiples = set()
    for number in vector:
        m = limit / number
        stop = int(m if m.is_integer() else m+1)
        for factor in range(1, stop):
            multiples.add(number * factor)
    return sum(multiples)
