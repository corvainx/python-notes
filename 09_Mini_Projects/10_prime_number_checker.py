# Project 10: Optimized Prime Number Verifier
import math

def is_prime(n: int) -> bool:
    """Checks primality with O(sqrt(N)) trial division."""
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter an integer to test for primality: "))
    if is_prime(num):
        print(f"Result: {num} is a PRIME number.")
    else:
        print(f"Result: {num} is a COMPOSITE number.")
