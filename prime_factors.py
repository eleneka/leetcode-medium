# prime factorization


def is_prime(number: int) -> bool:
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, number // 2 + 1, 2):
        if number % i == 0:
            return False
    return True


def prime_factors(number: int) -> list:
    if is_prime(number):
        return [number]
    factors = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            factors.append(i)
    prime_factors = []
    while number > 1:
        for factor in factors:
            if is_prime(factor) and not (number % factor):
                prime_factors.append(factor)
                number //= factor
    return sorted(prime_factors)


print(" * ".join(str(i) for i in prime_factors(int(input()))))
