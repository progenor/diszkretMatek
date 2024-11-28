import math


def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def find_carmichael_numbers(limit):
    primes = generate_primes(limit)
    prime_set = set(primes)
    carmichael_numbers = []

    for n in range(3, limit + 1, 2):
        if n in prime_set:
            continue
        factors = []
        is_carmichael = True
        temp = n

        for p in primes:
            if p * p > temp:
                break
            if temp % p == 0:
                factors.append(p)
                while temp % p == 0:
                    temp //= p

        if temp > 1:
            factors.append(temp)

        for p in factors:
            if (n - 1) % (p - 1) != 0:
                is_carmichael = False
                break

        if is_carmichael and len(factors) > 1:
            carmichael_numbers.append(n)

    return carmichael_numbers


carmichael_numbers = find_carmichael_numbers(1000)
print(carmichael_numbers)
