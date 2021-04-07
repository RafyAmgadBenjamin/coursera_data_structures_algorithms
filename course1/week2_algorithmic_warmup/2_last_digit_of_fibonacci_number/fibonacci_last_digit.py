# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def calc_fib_optimized(n):
    f = []
    f.append(0)
    f.append(1)

    for i in range(2, n + 1):
        f.append((f[i - 1] + f[i - 2]) % 10)
    return f[n]


if __name__ == "__main__":
    # input = sys.stdin.read()
    n = int(input())
    print(calc_fib_optimized(n))
