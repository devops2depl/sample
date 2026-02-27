import random


def generate_random_6_digits() -> str:
    """Return a random 6-digit string, including leading zeros."""
    return f"{random.randint(0, 999999):06d}"


if __name__ == "__main__":
    print(generate_random_6_digits())
