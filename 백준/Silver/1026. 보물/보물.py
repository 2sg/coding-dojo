length = int(input())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))


def min_value(length, array_a, array_b):
    array_a.sort()

    result = 0
    for i in range(length):
        b_max = max(array_b)
        result += array_a[i] * b_max
        array_b.remove(b_max)

    return result


print(min_value(length, array_a, array_b))
