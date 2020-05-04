# python3


class MinHeap:
    def __init__(self, n, array):
        self.size = n
        self.H = array
        self.swap = []

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2*i + 1
    
    def right_child(self, i):
        return 2*i + 2
    
    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l < self.size and self.H[l] < self.H[min_index]:
            min_index = l

        r = self.right_child(i)
        if r < self.size and self.H[r] < self.H[min_index]:
            min_index = r
        
        if i != min_index:
            self.swap.append((i, min_index))

            self.H[i], self.H[min_index] = self.H[min_index], self.H[i]
            self.sift_down(min_index)
    
    def build_heap(self):
        for i in range(self.size//2, -1, -1):
            self.sift_down(i)
        
        return self.swap
    

if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    min_heap = MinHeap(n, arr)
    swap = min_heap.build_heap()

    print(len(swap))
    for i, j in swap:
        print(i, j)

    
