# python3


def operator(a, op, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b


def min_and_max(m, M, i, j):
    minimum = float('inf')
    maximum = float('-inf')

    for k in range(i, j):
        a = operator(M[i][k], op[k], M[k+1][j])
        b = operator(M[i][k], op[k], m[k+1][j])
        c = operator(m[i][k], op[k], M[k+1][j])
        d = operator(m[i][k], op[k], m[k+1][j])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    
    return (minimum, maximum)


def parentheses(n, d, op):
    m = [[None for i in range(n)] for j in range(n)]
    M = [[None for i in range(n)] for j in range(n)]

    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(m, M, i, j)
    
    return M[0][n-1]

if __name__ == "__main__":
    s = input()
    d, op = [], []
    for i in s:
        try:
            d.append(int(i))
        except:
            op.append(i)
    
    print(parentheses(len(d), d, op))
