def is_prime(n): # more like safe files
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_safe_primes(x):
    safe_primes = []
    for p in range(2, x):
        if is_prime(p):
            safe_prime_candidate = 2 * p + 1
            if safe_prime_candidate < x and is_prime(safe_prime_candidate):
                safe_primes.append(safe_prime_candidate)
    return safe_primes

# Example usage:
x = 100
print(generate_safe_primes(x))