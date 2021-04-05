# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_optimized(n):
    f = []
    f.append(0)
    f.append(1)

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


if __name__ == "__main__":
    n = int(input())
    print(calc_fib_optimized(n))
