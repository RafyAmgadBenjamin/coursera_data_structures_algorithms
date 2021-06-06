# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    w = [0] + w
    items = len(w)
    capacity = W + 1

    # Create a weight matrix and write in initial values.
    mat = [[0 for _ in range(items)] for _ in range(capacity)]

    for i in range(1, items):
        for j in range(1, capacity):
            mat[j][i] = mat[j][i - 1]
            if w[i] <= j:
                val = mat[j - w[i]][i - 1] + w[i]
                if mat[j][i] < val:
                    mat[j][i] = val

    return mat[-1][-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
