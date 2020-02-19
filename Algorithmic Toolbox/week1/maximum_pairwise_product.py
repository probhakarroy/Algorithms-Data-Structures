#python3
import random

def product(arr) :
    temp1 = max(arr)
    arr.remove(temp1)
    temp2 = max(arr)
    return temp1*temp2

def product_fast(n, arr):
    #use None for max_index as assigning negative index like -1 would
    #apply for negative indexing in python.

    max_index = None        #Do not use --> max_index = -1
    for i in range(n) :
        if max_index == None or arr[i] > arr[max_index] :
            max_index = i

    max_index_1 = None
    for j in range(n) :
        if (max_index != j) and (max_index_1 == None or arr[j] > arr[max_index_1]) :
            max_index_1 = j
    
    return arr[max_index] * arr[max_index_1]

def product_naive(n, arr):
    product = 0
    for i in range(n) :
        for j in range(i+1, n) :
            product = max(product, arr[i] * arr[j])
    return product


def stress_test(N, M) :
    while True :
        n = random.randint(2, N)
        l = [random.randint(0, M) for i in range(n)]

        result1 = product_fast(n, l)
        result2 = product_naive(n, l)
        
        if result1 == result2 :
            print('n : {};\tarray : {} --> PASS'.format(n, l))
        else :
            print('FAIL --> n : {}\narray : {}\nfast_solution : {} \t naive_solution : {}'.format(n, l, result1, result2))
            break


if __name__ == '__main__' :
    n = int(input())
    l = [int(i) for i in input().split()]
    print(product(l))

    #stress_test(100, 100000)