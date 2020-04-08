# python3


class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, key):
        self.head = Node(key, self.head)

    def pop(self):
        if not self.head:
            print('ERROR: Empty stack!')
        else:
            node = self.head
            self.head = node.next
            return node.key

    def empty(self):
        if not self.head:
            return True
        return False


class TreeNode:
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def implement_tree(n, parent_index):
    nodes = [TreeNode() for i in range(n)]

    for child, parent in enumerate(parent_index):
        if parent == -1:
            root = nodes[child]
        else:
            nodes[parent].add_child(nodes[child])

    return root


def height(tree):
    max_height = height = 1
    stack = Stack()

    stack.push((height, tree))
    
    while not stack.empty():
        height, tree = stack.pop()
        
        if max_height < height:
            max_height = height
        
        for i in tree.children:
            stack.push((height+1, i))
    
    return max_height



if __name__ == "__main__":
    n = int(input())
    parent_index = [int(i) for i in input().split()]

    tree = implement_tree(n, parent_index)
    print(height(tree))
