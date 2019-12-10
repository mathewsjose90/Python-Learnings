l = [12, 1, 4, 5, 2, 5, 7, 22]


def sum_of_2_numbers(l, s):
    d = {}
    for n in l:
        if s - n in d:
            return "Numbers {0} and {1}".format(s - n, n)
        else:
            d[n] = 1
    return "Not possible"

print(sum_of_2_numbers(l,3))