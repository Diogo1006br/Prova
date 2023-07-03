import sys
import random
from math import gcd
from Crypto.Util import number

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

def calculate_public_key(phi):
    while True:
        e = random.randint(2, phi)
        if gcd(e, phi) == 1:
            return e

def calculate_private_key(e, phi):
    d = pow(e, -1, phi)  # Calculate the modular inverse of e
    return d

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
    d = calculate_private_key(e, phi)

    with open(public_key_file, 'w') as file:
        file.write(f"{e}\n{n}")

    with open(private_key_file, 'w') as file:
        file.write(f"{d}\n{n}")

    print("Keys generated successfully!")

if __name__ == '__main__':
    main()