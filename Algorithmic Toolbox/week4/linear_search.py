# python3


def linear_search(arr, high, low, key):
    if high < low:
        return 'NOT_FOUND'
    elif arr[low] == key:
        return low
    else:
        return linear_search(arr, high, low+1, key)


def linear_search_it(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return 'NOT_FOUND'


if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    key = int(input())
    print(linear_search(arr, len(arr)-1, 0, key))
