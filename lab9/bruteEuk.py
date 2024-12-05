import time
from math import gcd
def brute_force_mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse_extended_euclid(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Nincs inverz, ha a és m nem relatív prímek
    else:
        return x % m

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def mod_inverse_euler(a, m):
    if gcd(a, m) != 1:
        return None  # Nincs inverz, ha a és m nem relatív prímek
    else:
        return pow(a, euler_totient(m) - 1, m)

a = 17
m = 3120

# Brute-force
start_time = time.time()
brute_force_mod_inverse(a, m)
print("Brute-force idő:", time.time() - start_time)

# Kiterjesztett Eukleidész
start_time = time.time()
mod_inverse_extended_euclid(a, m)
print("Kiterjesztett Eukleidész idő:", time.time() - start_time)

# Euler-tétel
start_time = time.time()
mod_inverse_euler(a, m)
print("Euler-tétel idő: {:.3f}" , time.time() - start_time)
