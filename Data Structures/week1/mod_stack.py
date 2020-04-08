# python3


class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        self.max_head = None

    def push(self, key):
        self.head = Node(key, self.head)

        if not self.max_head:
            self.max_head = Node(key, self.max_head)
        elif self.max_head.key <= key:
            self.max_head = Node(key, self.max_head)

    def pop(self):
        if self.max_head.key == self.head.key:
            self.max_head = self.max_head.next

        self.head = self.head.next

    def max(self):
        return self.max_head.key


if __name__ == "__main__":
    n = int(input())
    stack = Stack()

    for _ in range(n):
        q = input().split()
        
        if len(q) == 2:
            stack.push(int(q[1]))
        elif q[0] == 'pop':
            stack.pop()
        else:
            print(stack.max())

