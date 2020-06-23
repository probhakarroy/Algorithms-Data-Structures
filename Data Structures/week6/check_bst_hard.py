# python3

import sys
import threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def in_order(node, min_value, max_value):
    result = True
    if min_value <= node.key < max_value:
        if node.left:
            result = result and in_order(node.left, min_value, node.key)
        if node.right:
            result = result and in_order(node.right, node.key, max_value)
    else:
        result = False

    return result


def main():
    n = int(input())
    if n == 0:
        print('CORRECT')
        sys.exit()

    nodes = [Node() for i in range(n)]
    for i in range(n):
        key, left, right = [int(j) for j in input().split()]

        nodes[i].key = key
        if left == -1:
            nodes[i].left = None
        else:
            nodes[i].left = nodes[left]

        if right == -1:
            nodes[i].right = None
        else:
            nodes[i].right = nodes[right]

    if in_order(nodes[0], float('-inf'), float('inf')):
        print('CORRECT')
    else:
        print('INCORRECT')

threading.Thread(target=main).start()