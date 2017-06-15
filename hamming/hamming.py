def distance(strand_one, strand_two):
    distance = 0
    if len(strand_one) != len(strand_two):
        raise ValueError
    for c, k in zip(strand_one, strand_two):
        if c != k:
            distance += 1
    return distance
