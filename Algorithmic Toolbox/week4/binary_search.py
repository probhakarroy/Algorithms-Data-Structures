# python3


def binary_search(arr, high, low, key):
    mid = (low + (high-low)//2)

    if high < low:
        return 'NOT_FOUND'
    elif arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search(arr, high, mid+1, key)
    else:
        return binary_search(arr, mid-1, low, key)


def binary_search_it(arr, high, low, key):
    while high >= low:
        mid = (low + (high-low)//2)

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid-1

    return -1


if __name__ == "__main__":
    # arr = [int(i) for i in input().split()]
    # key = int(input())

    # print(binary_search(arr, len(arr)-1, 0, key))

    n, *arr = [int(i) for i in input().split()]
    k, *keys = [int(i) for i in input().split()]

    indexes = [binary_search_it(arr, n-1, 0, i) for i in keys]
    [print(i, end=' ') for i in indexes]
    print()