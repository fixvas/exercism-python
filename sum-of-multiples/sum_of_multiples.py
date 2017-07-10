import math


def sum_of_multiples(limit, factor):
    multiples = set()
    for number in factor:
        for multiplier in range(1, math.floor(limit / number)+1):
            res = number * multiplier
            if res < limit:
                multiples.add(res)
    return sum(multiples)
