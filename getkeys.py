import random
import sys


def get_prime_numbers(prime_file):
    primes = []
    with open(prime_file, 'r') as file:
        for line in file:
            prime = int(line.strip())
            primes.append(prime)
    return primes


def calculate_n(p, q):
    return p * q


def calculate_phi(p, q):
    return (p - 1) * (q - 1)


def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def calculate_public_key(phi):
    while True:
        e = random.randint(2, phi)
        if calculate_gcd(e, phi) == 1:
            return e


def calculate_extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = calculate_extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y


def calculate_modular_inverse(e, phi):
    _, x, _ = calculate_extended_gcd(e, phi)
    return x % phi


def main():
    if len(sys.argv) != 4:
        print("Usage: python getkeys.py <prime_file> <public_key_file> <private_key_file>")
        return

    prime_file = sys.argv[1]
    public_key_file = sys.argv[2]
    private_key_file = sys.argv[3]

    primes = get_prime_numbers(prime_file)
    p = random.choice(primes)
    primes.remove(p)
    q = random.choice(primes)

    n = calculate_n(p, q)
    phi = calculate_phi(p, q)
    e = calculate_public_key(phi)
    d = calculate_modular_inverse(e, phi)

    with open(public_key_file, 'w') as file:
        file.write(f"{e}\n{n}")

    with open(private_key_file, 'w') as file:
        file.write(f"{d}\n{n}")

    print("Keys generated successfully!")


if __name__ == '__main__':
    main()
