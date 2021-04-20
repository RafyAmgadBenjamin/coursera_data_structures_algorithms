# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gdc_optimitzed(a, b):
    if b == 0:
        return a
    a_prim = a % b
    return gdc_optimitzed(b, a_prim)


def lcm_optimized(a, b):
    return (a * b) / gdc_optimitzed(a, b)


if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(int(lcm_optimized(a, b)))
    # print(lcm_naive(a, b))
