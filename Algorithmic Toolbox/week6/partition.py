# python3


def partition_items(n, items_val):
    V = sum(items_val)
    V //= 3

    share = []
    for _ in range(2):    
        items = solution(V, len(items_val), items_val)
        share.append(sum(items))
        for i in items:
            items_val.remove(i)
    
    share.append(sum(items_val))

    if share[0] == share[1] and share[1] == share[2]:
        return 1
    
    return 0


def solution(V, n, items_val):
    value = [[0 for i in range(n+1)] for j in range(V+1)]

    for i in range(1, n+1):
        for v in range(1, V+1):
            value[v][i] = value[v][i-1]
            if items_val[i-1] <= v:
                val = value[v - items_val[i-1]][i-1] + items_val[i-1]
                if value[v][i] < val:
                    value[v][i] = val

    i, j = V, n
    items = []

    while i > 0 and j > 0:
        if value[i][j] != value[i][j-1]:
            items.append(items_val[j-1])
            i -= items_val[j-1]
            j -= 1
        else:
            j -= 1

    return items


if __name__ == "__main__":
    n = int(input())
    items_val = [int(i) for i in input().split()]

    print(partition_items(n, items_val))
