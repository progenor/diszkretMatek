def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def factorial_prime_factors(n):
    from collections import Counter
    total_factors = Counter()
    for i in range(2, n + 1):
        total_factors.update(prime_factors(i))
    return dict(total_factors)

# Példa használat
n = 10
print(f"A(z) {n} prímtényezős felbontása: {prime_factors(n)}")
print(f"A(z) {n}! prímtényezős felbontása: {factorial_prime_factors(n)}")