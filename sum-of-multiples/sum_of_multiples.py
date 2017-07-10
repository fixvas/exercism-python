def sum_of_multiples(limit, vector):
    multiples = set()
    for number in vector:
        for m in range(0, limit, number):
            multiples.add(m)
    return sum(multiples)
