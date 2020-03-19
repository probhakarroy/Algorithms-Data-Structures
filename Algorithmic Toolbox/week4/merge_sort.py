#python3

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    
    m = n//2
    B = merge_sort(A[:m])
    C = merge_sort(A[m:])
    A_dash = merge(B, C)

    return A_dash


def merge(B, C):
    D = [0 for i in range(len(B)+len(C))]
    i = j = k = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D[k] = B[i]
            i += 1
            k += 1
        else:
            D[k] = C[j]
            j += 1
            k += 1
    
    while i < len(B):
        D[k] = B[i]
        i += 1
        k += 1

    while j < len(C):
        D[k] = C[j]
        j += 1
        k += 1
    
    return D

if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(merge_sort(arr))