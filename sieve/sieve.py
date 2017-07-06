def sieve(N):
    res = []
    sequence = {x: True for x in range(2, N+1)}
    for number in sequence:
        if sequence[number]:
            res.append(number)
            factor = 2
            non_prime = number * factor
            while non_prime <= N:
                sequence[non_prime] = False
                factor += 1
                non_prime = number * factor
    return res
