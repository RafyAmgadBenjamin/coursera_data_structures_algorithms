# Uses python3
import sys
from decimal import Decimal


def get_optimal_value(capacity, weights, values):
    value = 0.0
    data = []
    for i in range(len(weights)):
        data.append({"val_per_w": values[i] / weights[i], "w": weights[i], "val": values[i]})

    value = 0
    # items_values = list(data.keys())
    # items_values.sort(reverse=True)
    items_values = sorted(data, key=lambda k: k["val_per_w"], reverse=True)
    for item in items_values:
        item_weight = item.get("w")
        item_value = item.get("val")
        if capacity >= item_weight:
            capacity -= item_weight
            value += item_value
        else:
            amount = capacity / item_weight
            value += amount * item_value
            break

    # return round(Decimal(str(value), 4))
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

### important test case
# 3 10

# 1 9

# 2 9

# 1 9

# I have to change the data structure as the key may be repeated like in the above test case
