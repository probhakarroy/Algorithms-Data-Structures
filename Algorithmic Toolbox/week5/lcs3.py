# python3
# needs to be implemented!!


def lcs(A, B):
    n, m = len(A), len(B)
    D = [[float('inf') for i in range(m+1)] for j in range(n+1)]
    seq = []

    for i in range(n+1):
        D[i][0] = i

    for j in range(m+1):
        D[0][j] = j

    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 2

            if A[i-1] == B[j-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    i, j = n, m

    while i > 0 and j > 0:
        if i > 0 and D[i][j] == D[i-1][j] + 1:
            i, j = i-1, j
        elif j > 0 and D[i][j] == D[i][j-1] + 1:
            i, j = i, j-1
        elif A[i-1] == B[j-1]:
            seq.append(A[i-1])
            i, j = i-1, j-1
        else:
            i, j = i-1, j-1

    return len(seq)


if __name__ == "__main__":
    n = int(input())
    A = [int(i) for i in input().split()]
    m = int(input())
    B = [int(i) for i in input().split()]
    o = int(input())
    C = [int(i) for i in input().split()]

    seq = lcs(A, B)
    seq1 = lcs(A, C)
    seq2 = lcs(B, C)

    print(min([seq, seq1, seq2]))
