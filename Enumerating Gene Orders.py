from math import factorial


def n_of_perms(n: int) -> int:
    return factorial(n)


def perms(n: int) -> list:
    pass


if __name__ == "__main__":
    n = int(input())
    nps = n_of_perms(n)
