#python3


def seg_len(n):
    min_seq_len = [float('inf')] * (n+1)
    min_seq_len[0], min_seq_len[1] = 0, 0
    prev = [None] * (n+1)
    seq = [n]

    for i in range(1, n+1):
        ops = [float('inf')] * 3
        ops[0] = min_seq_len[i - 1]

        if i%2 == 0:
            ops[1] = min_seq_len[i//2]
        
        if i%3 == 0:
            ops[2] = min_seq_len[i//3]
        
        minimum = min(ops)
        prev[i] = ops.index(minimum)

        if min_seq_len[i] > 1 + minimum:
            min_seq_len[i] = 1 + minimum

    j = n
    while j > 1 :
        if prev[j] == 0:
            j -= 1
        elif prev[j] == 1:
            j //= 2
        else:
            j //= 3
        
        seq.append(j)
    
    seq.reverse()
    return min_seq_len[n], seq


if __name__ == "__main__":
    n = int(input())
    op, seq = seg_len(n)
    print(op)
    [print(i, end=' ') for i in seq]
    print()