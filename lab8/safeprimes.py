import sympy as smp


def generate_safe_primes(x):
    safe_primes = []
    for p in range(2, x):
        if is_prime(p):
            safe_prime_candidate = 2 * p + 1
            if safe_prime_candidate < x and is_prime(safe_prime_candidate):
                safe_primes.append(safe_prime_candidate)
# Example usage:
    return safe_primes
def main():
    # x = 100
    # print(generate_safe_primes(x))
    with open("lab8/in1.txt", 'r') as f:
        while(f.readline()):
            x = int(f.readline())
            print(f" {x} : {smp.isprime(x)}")

main()