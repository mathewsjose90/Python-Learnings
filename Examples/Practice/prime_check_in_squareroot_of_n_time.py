import math


def check_prime(n):
    check_untill = math.sqrt(n)
    factors = 2
    start = 2
    while start <= check_untill:
        if n % start == 0:
            factors += 1
            break
        start += 1
    return True if factors == 2 else False


print(check_prime(100))
print(check_prime(99))
print(check_prime(97))
