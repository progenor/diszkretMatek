from base64 import b64encode, b64decode
from decimal import Decimal, getcontext
from math import factorial, ceil, floor, gcd, isqrt
from random import randint, getrandbits


def cf_sqrt2(p):
    getcontext().prec = p
    val = Decimal(0)
    for x in range(p * p):
        val = 1 / (2 + val)
    return val + 1


def cf_sqrt_n(n, p):
    getcontext().prec = p
    res = Decimal(0)
    for i in range(p * p):
        res = (n - 1) / (2 + res)
    return 1 + res


def cf_euler(p):
    getcontext().prec = p
    res = Decimal(p * p)
    for i in range(p * p, 0, -1):
        res = i + i / res
    return 2 + 1 / res


def cf_pi(p):
    getcontext().prec = p
    res = Decimal(0)
    for i in range(p * p, 0, -1):
        res = (i * i) / (2 * i + 1 + res)
    return 4 / (1 + res)


def cf_phi(p):
    getcontext().prec = p
    res = Decimal(0)
    for i in range(p * p, 0, -1):
        res = 1 / (1 + res)
    return 1 + res


def ext_gcd(u, v):
    """visszateriti (g, x, y)-t, ugy hogy u*x + v*y = g = gcd(u, v)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while u != 0:
        (q, u), v = divmod(v, u), u
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return v, x0, y0


def inverse_gcd(u, v):
    """u inverze mod v"""
    if v == 0:
        raise ZeroDivisionError("Modulus cannot be zero")
    if v < 0:
        raise ValueError("Modulus cannot be negative")

    u3, v3 = u, v
    u1, v1 = 1, 0
    while v3 > 0:
        q = u3 // v3
        u1, v1 = v1, u1 - v1 * q
        u3, v3 = v3, u3 - v3 * q
    if u3 != 1:
        raise ValueError("No inverse value can be computed")
    while u1 < 0:
        u1 = u1 + v
    return u1


def diophantine(a, m, b):
    """
    a es m ket termek ara, b az osszeg (x * a + y * m = b)
    """
    d, xk, yk = ext_gcd(a, m)
    x0 = xk * (b // d)
    y0 = yk * (b // d)

    md = m // d
    ad = a // d

    n1 = ceil(-x0 / md)
    n2 = floor(y0 / ad)

    return [(x0 + n * md, y0 - n * ad) for n in range(n1, n2 + 1)]


def gen_sieve(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be positive integer')
    if n in {0, 1, 2}:
        return []
    elif n in {3, 4, 5}:
        return [2] if n == 3 else [2, 3]

    n, c = n - n % 6 + 6, 2 - (n % 6 > 1)
    s = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if s[i]:
            k = 3 * i + 1 | 1
            s[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            s[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * (
                    (n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - c) if s[i]]


sieve = gen_sieve(104730)  # elso 10000 primszam


def factorize(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError('n must be positive integer')

    a = []
    while num % 2 == 0:
        a.append(2)
        num //= 2
    f = 3
    while f * f <= num:
        if num % f == 0:
            a.append(f)
            num //= f
        else:
            f += 2
    if num != 1:
        a.append(num)
    return a


def wilson(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError('n must be positive integer')

    if factorial(num - 1) % num == num - 1:
        return True
    return False


def euler(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError('n must be positive integer')

    r = num
    p = 2
    while p * p <= num:
        if num % p == 0:
            while num % p == 0:
                num //= p
            r -= r // p
        p += 1
    if num > 1:
        r -= r // num
    return r


def crt(div, rem):
    if len(div) != len(rem):
        raise ValueError('Invalid system')

    k = len(div)
    p = 1
    for i in range(0, k):
        p = p * div[i]

    res = 0

    for i in range(0, k):
        pp = p // div[i]
        res = res + rem[i] * pow(pp, div[i]) * pp

    return res % p


def miller_rabin(num, it=10):
    if not isinstance(num, int) or num < 0:
        raise ValueError('n must be positive integer')

    if num in {1, 2, 3, 5}:
        return True

    if ~num & 1:
        return False

    m = num - 1
    a = 0
    while ~m & 1:
        m >>= 1
        a += 1

    for i in range(it):
        b = 1
        while b in (1, num - 1):
            b = randint(2, num - 2)
            assert (2 <= b <= num - 2)

        z = pow(b, m, num)
        if z in (1, num - 1):
            continue

        for j in range(1, a):
            z = pow(z, 2, num)
            if z == num - 1:
                break
            if z == 1:
                return False
        else:
            return False

    return True


def is_prob_prime(num):
    if num < 3 or num & 1 == 0:
        return num == 2
    for p in sieve:
        if num == p:
            return True
        if num % p == 0:
            return False

    bit_len = num.bit_length()

    for k, t in ((220, 30), (280, 20), (390, 15), (512, 10), (620, 7), (740, 6), (890, 5), (1200, 4), (1700, 3),
                 (3700, 2)):  # (k, t) szamparok, ahol k bites szamnak t miller-rabin iteracio kell
        if bit_len < k:
            return miller_rabin(num, t)
    return miller_rabin(num, 1)


def gen_prob_prime(bit_len):
    if bit_len < 2:
        raise ValueError("N must be larger than 1")

    while True:
        num = getrandbits(bit_len) | 1
        if is_prob_prime(num):
            return num


def gen_safe_prime(bit_len):
    while True:
        q = gen_prob_prime(bit_len - 1)
        p = q * 2 + 1
        if p.bit_length() != bit_len:
            continue
        if is_prob_prime(p):
            while True:
                g = randint(2, p - 2)
                if pow(g, q, p) != 1:
                    return p, g


def gen_xor_key(m_len, k=None):
    if k is None:
        return getrandbits(m_len * 8).to_bytes(m_len)
    elif m_len > len(k):
        print("Unsafe key!")
    return (k * (m_len // len(k)) + k[:m_len % len(k)]).encode()


def str_xor(m, k):
    return bytes([a ^ b for a, b in zip(m, k)])


def xor_ex():
    print('XOR ENCRYPTION:')
    m = "xor is awesome"
    key = gen_xor_key(len(m))
    m = str_xor(m.encode(), key)
    print(m)
    m = str_xor(m, key).decode()
    print(m, '\n')


def gen_rsa_key_pair(bit_len, e=65537):
    """
    :returns n, e, d, p, q, dp, dq, u
    """
    if bit_len < 1024:
        raise ValueError('RSA modulus length must be >= 1024')

    if ~e & 1 or e < 3:
        raise ValueError('RSA public exponent must be a positive, odd integer larger than 2.')

    d = n = 1

    while n.bit_length() != bit_len and d < (1 << (bit_len // 2)):
        q_sz = bit_len // 2
        p_sz = bit_len - q_sz

        p_min = q_min = isqrt(1 << (2 * q_sz - 1))
        if q_sz != p_sz:
            p_min = isqrt(1 << (2 * p_sz - 1))

        while True:
            p = gen_prob_prime(p_sz)
            if p > p_min and gcd(p - 1, e) == 1:
                break

        dist_min = 1 << (bit_len // 2 - 100)

        while True:
            q = gen_prob_prime(q_sz)
            if q > q_min and gcd(q - 1, e) == 1 and abs(q - p) > dist_min:
                break

        n = p * q
        phi = (p - 1) * (q - 1)  # lehetne lkkt-vel szamolni, de jo ez igy is
        d = pow(e, -1, phi)

        if p > q:
            p, q = q, p

        dp = d % (p - 1)
        dq = d % (q - 1)
        u = pow(q, -1, p)

        test_rsa_key_consistency(n, e, d, p, q)
        return n, e, d, p, q, dp, dq, u


def test_rsa_key_consistency(n, e, d, p, q):
    if e <= 1 or e >= n:
        raise ValueError("Invalid RSA public exponent")
    if gcd(n, e) != 1:
        raise ValueError("RSA public exponent is not coprime to modulus")
    if ~n & 1:
        raise ValueError("RSA modulus is not odd")
    if d <= 1 or d >= n:
        raise ValueError("Invalid RSA private exponent")
    if gcd(n, d) != 1:
        raise ValueError("RSA private exponent is not coprime to modulus")
    if p * q != n:
        raise ValueError("RSA factors do not match modulus")
    if not is_prob_prime(p):
        raise ValueError("RSA factor p is composite")
    if not is_prob_prime(q):
        raise ValueError("RSA factor q is composite")
    phi = (p - 1) * (q - 1)
    lcm = phi // gcd((p - 1), (q - 1))
    if (e * d % lcm) != 1:
        raise ValueError("Invalid RSA condition")


def int_to_b64(num):
    return b64encode(num.to_bytes((num.bit_length() + 7) // 8)).decode()


def b64_to_int(b64_str):
    return int.from_bytes(b64decode(b64_str.encode()))


def write_rsa_key_pair(bit_len):
    key = tuple(map(int_to_b64, gen_rsa_key_pair(bit_len)))

    file = open('RSA_Public_Key_' + str(bit_len) + '.txt', "wt")
    file.write(key[0] + '\n' + key[1])
    file.close()

    file = open('RSA_Private_Key_' + str(bit_len) + '.txt', "wt")
    for i in range(7):
        file.write(key[i] + '\n')
    file.write(key[7])
    file.close()


def read_rsa_public_key(path):
    file = open(path, "r")
    return tuple(map(b64_to_int, file.readlines()))


def read_rsa_private_key(path):
    file = open(path, "r")
    return tuple(map(b64_to_int, file.readlines()))


def rsa_encrypt(m, puk):
    n, e = puk
    m_len, m = len(m), int.from_bytes(m.encode())
    if m.bit_length() > n.bit_length():
        raise ValueError("Message too long")
    return pow(m, e, n).to_bytes((n.bit_length() + 7) // 8), m_len


def rsa_decrypt(c, c_len, prk):
    n, e, d, p, q, dp, dq, u = prk
    c = int.from_bytes(c)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    return (m2 + ((u * (m1 - m2)) % p) * q).to_bytes(c_len).decode()


def rsa_sign(m, prk):
    n, _, d, *_ = prk
    sm = int.from_bytes(m.encode())
    if sm.bit_length() > n.bit_length():
        raise ValueError("Message too long")
    return pow(sm, d, n).to_bytes((n.bit_length() + 7) // 8), m


def rsa_verify(sm, m, puk):
    n, e = puk
    sm = pow(int.from_bytes(sm), e, n).to_bytes(len(m)).decode()
    if sm == m:
        print('Valid Signature')
        return True
    else:
        print('Invalid Signature')
        return False


def rsa_crypt_ex():
    print('RSA Encryption / Decryption:')
    bit_len = 2048
    write_rsa_key_pair(bit_len)
    puk = read_rsa_public_key('RSA_Public_Key_' + str(bit_len) + '.txt')
    prk = read_rsa_private_key('RSA_Private_Key_' + str(bit_len) + '.txt')
    msg, msg_len = rsa_encrypt("Rivest-Shamir-Adleman", puk)
    print(rsa_decrypt(msg, msg_len, prk), '\n')


def rsa_sign_ex():
    print('RSA Signing:')
    bit_len = 2048
    write_rsa_key_pair(bit_len)
    puk = read_rsa_public_key('RSA_Public_Key_' + str(bit_len) + '.txt')
    prk = read_rsa_private_key('RSA_Private_Key_' + str(bit_len) + '.txt')
    c, m = rsa_sign("Rivest-Shamir-Adleman", prk)
    rsa_verify(c, m, puk)
    print()


def bsgs(g, h, p):
    """
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    """
    n = isqrt(p - 1) + 1

    tbl = {pow(g, i, p): i for i in range(n)}

    c = pow(g, n * (p - 2), p)

    for j in range(n):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * n + tbl[y]

    return None


# print(bsgs(7894352216, 355407489, 604604729))


def gen_dh_key_pair(bit_len):
    p, g = gen_safe_prime(bit_len)
    prk = randint(2, p - 1)
    puk = pow(g, prk, p)
    return prk, puk, p, g


def compute_dh_key_pair(p, g):
    prk = randint(2, p - 1)
    puk = pow(g, prk, p)
    return prk, puk


def compute_dh_shared_key(lc_prk, sh_puk, p):
    return pow(sh_puk, lc_prk, p)


def dh_ex():
    print('DH Exchanging:\n')
    bit_len = 1024

    # Alice szamitasai
    private_a, public_a, p, g = gen_dh_key_pair(bit_len)
    print('Safe prime:', p, '\nGenerator:', g, '\n')
    print("Alice's Private key:", private_a, "\nAlice's Public key:", public_a, '\n')

    # Bob szamitasai
    private_b, public_b = compute_dh_key_pair(p, g)
    print("Bos's Private key:", private_b, "\nBob's Public key:", public_b, '\n')

    # Alice szamitasai, miután megkapta Bob publikus kulcsát
    shared_key_a = compute_dh_shared_key(private_a, public_b, p)
    print("Alice's computed key:", shared_key_a, '\n')

    # Bob számításai, miután megkapta Alice publikus kulcsát
    shared_key_b = compute_dh_shared_key(private_b, public_a, p)
    print("Bob's computed key:  ", shared_key_b)


def encryption_ex():
    xor_ex()
    rsa_crypt_ex()
    rsa_sign_ex()
    dh_ex()

encryption_ex()
