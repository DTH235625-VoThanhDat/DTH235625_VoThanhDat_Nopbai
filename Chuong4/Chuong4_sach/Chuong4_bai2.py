import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(math.sqrt(num))
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
    return True

def GenPrime(n):
    """Sinh n số nguyên tố đầu tiên: 2, 3, 5, 7, ..."""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1
