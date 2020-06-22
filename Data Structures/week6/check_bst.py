# python3


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def in_order(node):
    if not node:
        return

    in_order(node.left)

    if (not node.left and node.key < node.right.key) \
            or (node.left.key < node.key and not node.right) \
            or (node.left.key < node.key < node.right.key):
        pass
    else:
        return False

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


if __name__ == "__main__":
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
