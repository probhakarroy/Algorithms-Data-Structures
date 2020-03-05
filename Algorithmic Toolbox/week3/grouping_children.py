# python3
# import itertools, random


# def naive_min_group(C):
#     m = len(C)

#     for i in range(1, len(C)):  #for all the partitions of C
#         #G = itertools.combinations(C, i)
        
#         print(list(G))
#         good, k = True, 0
#         for j in G:
#             k += 1
#             if max(j) - min(j) > 1:
#                 good = False

#         if good:
#             m = min(m, k)

#     return m


def min_group_sorted(x):
    R, i = [], 0
    while i < len(x):
        l, r = [x[i], x[i] + 1]
        R.append([l, r])

        while i < len(x) and x[i] <= r:
            i += 1

    return R 


# #STRESS TEST
# def stress_test(M, N):
#     while True:
#         C = [random.randint(1, M) for i in range(N)]
#         print(C, end=' -> ')

#         result1 = naive_min_group(C)
#         result2 = len(min_group_sorted(sorted(C)))

#         if result1 == result2:
#             print('PASS')
#         else:
#             print('FAIL!\tnaive sol: {}\tsol.: {}'.format(result1, result2))
#             break

if __name__ == "__main__":
    C = [int(i) for i in input().split()]
    # print(naive_min_group(C))
    print(min_group_sorted(C))

    # stress_test(10, 5)
