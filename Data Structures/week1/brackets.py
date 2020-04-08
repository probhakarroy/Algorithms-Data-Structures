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


def is_balanced(str):
    stack = Stack()

    for count, char in enumerate(str):
        if char in ['(', '{', '[']:
            stack.push((count, char))
        elif char in [')', '}', ']']:
            if stack.empty():
                return count+1

            _, top = stack.pop()
            if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
                return count+1

    if stack.empty():
        return 'Success'
    else:
        count, _ = stack.pop()
        return count+1


if __name__ == "__main__":
    str = input()
    print(is_balanced(str))
