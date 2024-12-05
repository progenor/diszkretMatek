def is_safe_prime(n):
    # Check if n is prime
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    # Check if (n-1)/2 is also prime
    m = (n - 1) // 2
    if m < 2:
        return False
    i = 3
    while i * i <= m:
        if m % i == 0:
            return False
        i += 2
    return True


print(is_safe_prime(107))
print(is_safe_prime(108))
