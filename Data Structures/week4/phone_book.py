# python3

if __name__ == "__main__":
    n = int(input())
    queries = [input() for i in range(n)]

    map = [None] * 10**7

    for i in queries:
        q = i.split()

        if q[0] == 'add':
            map[int(q[1])] = q[2]
        elif q[0] == 'del':
            map[int(q[1])] = None
        else:
            if map[int(q[1])]:
                print(map[int(q[1])])
            else:
                print('not found')
