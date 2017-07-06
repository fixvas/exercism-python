def sieve(N):
    res = []
    sequence = {x: True for x in range(2, N+1)}
    for number in sequence:
        if sequence[number]:
            res.append(number)
            for non_prime in range(number**2, N+1, number):
                sequence[non_prime] = False
    return res
