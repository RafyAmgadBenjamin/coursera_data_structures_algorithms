# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gdc_optimitzed(a, b):
    if b == 0:
        return a
    a_prim = a % b
    return gdc_optimitzed(b, a_prim)


if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(gdc_optimitzed(a, b))
