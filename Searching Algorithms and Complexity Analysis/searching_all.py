import math
import sys


def linear_search(arr, key):
    # loop through all the elements of the array and compare with the search key
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key, lo=0, hi=None):
    hi = hi or len(arr) - 1
    # do not even enter into the loop if the search key falls beyond the extreme bounds of sorted array
    while lo <= hi and arr[lo] <= key <= arr[hi]:
        # find mid-point and compare. Repeat the same by eliminating an useless half
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
    # do not even enter into the loop if the search key falls beyond the extreme bounds of sorted array
    while lo <= hi and arr[lo] <= key <= arr[hi]:
        # find both mid-points and compare. Repeat the same by eliminating two third at a time
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
    # do not even enter into the loop if the search key falls beyond the extreme bounds of sorted array
    while lo <= hi and arr[lo] <= key <= arr[hi]:
        # Formula for the position is derived from the equation of a straight line (y=m*x+c),
        # given the fact if element distribution is equal, they would form a straight line
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
    # In the worst case, we have to do n/m jumps and if the last checked value is greater than
    # the element to be searched for, we perform m-1 comparisons more for linear search.
    # Therefore the total number of comparisons in the worst case will be ((n/m) + m-1).
    # The value of the function ((n/m) + m-1) will be minimum when m = √n. Therefore, the best step size is m = √n.
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
    # First check with the first element (i.e elem at index 0) separately.
    if arr[0] == key:
        return 0
    # start with index 1 and increase the index exponentially
    i = 1
    while i < n and arr[i] <= key:
        i *= 2

    return binary_search(arr, key, lo=int(i / 2), hi=min(i, n - 1))


def fibonacci_search(arr, key):
    # Find the smallest fibonacci number greater than or equal to thr length of arr
    fib = [0, 1]
    while fib[-1] < key:
        fib.append(sum(fib[-2:]))

    m = len(fib) - 1
    offset = -1
    while fib[m] > 1:
        # calculate the index to search for
        i = min(offset + fib[m - 2], len(arr) -1)
        if arr[i] == key:
            return i
        elif arr[i] < key:
            m -= 1
            offset = i
        else:
            m -= 2

    # Check for few corner cases when fibonacci pointer doesn't reach the extreme right index
    # example: for an arr of length 2^k and key to be searched is the very last element
    if fib[m - 1] and arr[len(arr) - 1] == key:
        return len(arr) - 1
    return -1


if __name__ == "__main__":
    input_ = [2, 5, 8, 9, 10, 12, 23, 26, 29, 31, 37, 43, 44, 53, 59, 73, 89, 93, 95, 98]
    input_interpolation = range(2, 99, 3)
    search_ = 89, 35, 2, 1, 98, 100
    print("Input array:", input_)
    search_dict = dict(linear=linear_search,
                       binary=binary_search,
                       ternary=ternary_search,
                       interpolation=interpolation_search,
                       jump=jump_search,
                       exponential=exponential_search,
                       fibonacci=fibonacci_search)

    type_ = str(sys.argv[1]).lower() if len(sys.argv) > 1 else ','.join(search_dict.keys())
    for t in type_.split(','):
        print(f"Performing {t} search")
        for key_ in search_:
            index_ = search_dict.get(t)(input_, key_)
            if index_ > -1:
                print(f"{key_} found at index", index_)
            else:
                print(f"{key_} not found!!")
        print()
