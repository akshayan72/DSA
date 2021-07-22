import math
import sys


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key, lo=0, hi=None):
    hi = hi or len(arr) - 1
    while lo <= hi and arr[lo] <= key <= arr[hi]:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def ternary_search(arr, key):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi and arr[lo] <= key <= arr[hi]:
        mid1 = lo + (hi - lo) // 3
        mid2 = hi - (hi - lo) // 3
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        if arr[mid2] < key:
            lo = mid2 + 1
        elif arr[mid1] > key:
            hi = mid1 - 1
        else:
            lo = mid1 + 1
            hi = mid2 - 1
    return -1


def interpolation_search(arr, key):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi and arr[lo] <= key <= arr[hi]:
        pos = lo + ((key - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])
        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(prev + step, n) - 1] < key:
        prev += step
        if prev > n:
            return -1

    while arr[prev] < key:
        prev += 1

    if arr[prev] == key:
        return prev
    return -1


def exponential_search(arr, key):
    n = len(arr)
    if arr[0] == key:
        return 0

    i = 1
    while i < n and arr[i] <= key:
        i *= 2

    return binary_search(arr, key, lo=int(i / 2), hi=min(i, n - 1))


def fibonacci_search(arr, key):
    # Find the smallest fibonacci number greater than or equal to thr lenght of
    fib = [0, 1]
    while fib[-1] < key:
        fib.append(sum(fib[-2:]))

    m = len(fib) - 1
    offset = -1
    while fib[m] > 1:
        i = min(offset + fib[m - 2], len(arr) -1)
        if arr[i] == key:
            return i
        elif arr[i] < key:
            m -= 1
            offset = i
        else:
            m -= 2

    # this will run if there is only one last element left
    if fib[m - 1] and arr[offset + 1] == key:
        return offset + 1
    return -1


if __name__ == "__main__":
    input_ = [2, 5, 8, 9, 10, 12, 23, 26, 29, 31, 37, 43, 44, 53, 59, 73, 89, 93, 95, 98]
    input_interpolation = range(2, 99, 3)
    search_ = 89, 35, 2, 1, 98, 100

    type_ = str(sys.argv[1]).lower() if len(sys.argv) > 1 else 'linear'
    search_dict = dict(linear=linear_search,
                       binary=binary_search,
                       ternary=ternary_search,
                       interpolation=interpolation_search,
                       jump=jump_search,
                       exponential=exponential_search,
                       fibonacci=fibonacci_search)

    for key_ in search_:
        index_ = search_dict.get(type_)(input_, key_)
        if index_ > -1:
            print(f"Item found at index", index_)
        else:
            print("Not found!!")
