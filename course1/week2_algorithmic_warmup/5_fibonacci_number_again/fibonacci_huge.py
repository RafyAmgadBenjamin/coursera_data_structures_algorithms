# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def calc_fib_optimized(n):
    f = []
    f.append(0)
    f.append(1)

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


# def get_perioud_len(m):
#     period = "01"
#     period_len = 2
#     for i in range(2, m * m):
#         if calc_fib_optimized(i) % m == 0 and calc_fib_optimized(i + 1) % m == 1:
#             period_len = len(period)
#             break
#         else:
#             period += str(calc_fib_optimized(i) % m)
#     return period_len


def get_perioud_len(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


if __name__ == "__main__":
    # input = sys.stdin.read()
    n, m = map(int, input().split())
    # print(get_fibonacci_huge_naive(n, m))
    # print(get_perioud_len(int(input())))
    # print(get_perioud_len(m))
    # print(pisanoPeriod(m))
    rem = n % get_perioud_len(m)
    print(calc_fib_optimized(rem) % m)

