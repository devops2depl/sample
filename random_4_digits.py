import random


def generate_random_4_digits() -> str:
    """Return a random 4-digit string, including leading zeros."""
    return f"{random.randint(0, 9999):04d}"


if __name__ == "__main__":
    print(generate_random_4_digits())
