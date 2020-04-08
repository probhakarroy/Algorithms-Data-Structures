# python3


class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.max_head = None

    def enqueue(self, key):
        if not self.head:
            self.head = self.tail = Node(key)
        else:
            node = Node(key)
            self.tail.next = node
            self.tail = node

        if not self.max_head:
            self.max_head = Node(key)
        elif self.max_head.key <= key:
            self.max_head = Node(key, self.max_head)
        elif not self.max_head.next:
            self.max_head.next = Node(key, self.max_head.next)
        elif self.max_head.next.key <= key <= self.max_head.key:
            self.max_head.next = Node(key, self.max_head.next)

    def dequeue(self):
        if self.head == self.tail:
            self.max_head = self.head = self.tail = None
        else:
            if self.max_head.key == self.head.key:
                self.max_head = self.max_head.next

            self.head = self.head.next

    def max(self):
        return self.max_head.key


if __name__ == "__main__":
    n = int(input())
    a = [int(i) for i in input().split()]
    size = int(input())

    queue = Queue()
    for i in a[:size]:
        queue.enqueue(i)

    print(queue.max(), end=' ')
    for i in a[size:]:
        queue.enqueue(i)
        queue.dequeue()
        print(queue.max(), end=' ')
    print()
