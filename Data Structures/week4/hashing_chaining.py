# python3


class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        self.head = Node(key, self.head)

    def check(self):
        if not self.head:
            print()
        else:
            node = self.head

            while node:
                print(node.key, end=' ')
                node = node.next
            print()

    def delete(self, key):
        if self.head:
            if self.head.key == key:
                self.head = self.head.next
            else:
                node = self.head

                while node and node.next:
                    if node.next.key == key:
                        node.next = node.next.next
                        break
                    node = node.next

    def find(self, key):
        node = self.head

        while node:
            if node.key == key:
                return 'yes'
            node = node.next

        return 'no'


def polyhash(S, p, x):
    hash = 0
    for i in range(len(S)-1, -1, -1):
        hash = ((hash*x + ord(S[i])) % p)
    return hash

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    queries = [input() for i in range(n)]

    hash_map = [LinkedList() for i in range(m)]

    for i in queries:
        q = i.split()

        if q[0] == 'add':
            index = polyhash(q[1], 1000000007, 263) % m
            if hash_map[index].find(q[1]) == 'no':
                hash_map[index].insert(q[1])
        elif q[0] == 'del':
            hash_map[polyhash(q[1], 1000000007, 263) % m].delete(q[1])
        elif q[0] == 'find':
            print(hash_map[polyhash(q[1], 1000000007, 263) % m].find(q[1]))
        else:
            hash_map[int(q[1])].check()