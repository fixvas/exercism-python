def square_of_sum(N):
    return pow(sum(range(1, N + 1)), 2)


def sum_of_squares(N):
    return sum(map(lambda x: x**2, range(1, N + 1)))


def difference(N):
    return abs(sum_of_squares(N) - square_of_sum(N))
