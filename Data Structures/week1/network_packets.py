# python3


class Node:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.size = size
        self.count = 0

    def enqueue(self, key):
        self.count += 1
        
        if not self.head:
            self.head = self.tail = Node(key)
        else:
            node = Node(key, None, self.tail)
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        self.count -= 1

        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return node.key

    def full(self):
        if self.count > self.size:
            return True
        return False


if __name__ == "__main__":
    S, n = [int(i) for i in input().split()]
    packets = [[int(i) for i in input().split()] for j in range(n)]
    
        

