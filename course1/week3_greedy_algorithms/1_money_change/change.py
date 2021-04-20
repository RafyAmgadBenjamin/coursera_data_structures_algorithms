# Uses python3
import sys


def get_change(m):
    # write your code here
    money_dom = {10: 0, 5: 0, 1: 0}
    for key, val in money_dom.items():
        amount = int(m / key)
        m = m % key
        money_dom[key] = amount

    return sum(money_dom.values())


if __name__ == "__main__":
    m = int(input())
    print(get_change(m))
