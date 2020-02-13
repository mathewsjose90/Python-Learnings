import sys

min_drop_count_dp = {}


def min_egg_drop_count(n, k):
    '''
    :param n: number of eggs
    :param k: number of floors
    :return: min number of tries needed in worst case
    '''

    if (n, k) in min_drop_count_dp:
        return min_drop_count_dp[(n, k)]

    # if no floors or 1 floor then 0 or 1 try
    if k == 0 or k == 1:
        return k
    # if only 1 egg then all floors has to be tried
    if n == 1:
        return k
    min = sys.maxsize

    for floor in range(1, k + 1):
        res = max(min_egg_drop_count(n - 1, floor - 1), min_egg_drop_count(n, k - floor))
        if res < min:
            print(floor)
            min = res
    min_drop_count_dp[(n, k)] = min + 1
    return min + 1


print(min_egg_drop_count(2, 100))
