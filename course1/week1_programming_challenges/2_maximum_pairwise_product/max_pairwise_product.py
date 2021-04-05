# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    max_no1 = -9999999999
    max_no1_index = -1
    max_no2 = -9999999999
    for i in range(len(numbers)):
        if numbers[i] > max_no1:
            max_no1 = numbers[i]
            max_no1_index = i

    for i in range(len(numbers)):
        if numbers[i] > max_no2 and i != max_no1_index:
            max_no2 = numbers[i]
    return max_no1 * max_no2


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
