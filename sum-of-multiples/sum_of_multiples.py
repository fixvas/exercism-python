def sum_of_multiples(limit, vector):
    multiples = set()
    for number in vector:
        multiples.update(range(0, limit, number))
    return sum(multiples)
