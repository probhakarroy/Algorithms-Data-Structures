# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node.key, end=' ')
    in_order(node.right)


def pre_order(node):
    if not node:
        return

    print(node.key, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    if not node:
        return

    post_order(node.left)
    post_order(node.right)
    print(node.key, end=' ')


def main():
    n = int(input())
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

    in_order(nodes[0])
    print()
    pre_order(nodes[0])
    print()
    post_order(nodes[0])
    print()

threading.Thread(target=main).start()