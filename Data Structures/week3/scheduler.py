# python3


class PriorityQueue:
    def __init__(self):
        self.H = []
        self.size = 0

    def parent(self, i):
        return (i - 1)//2

    def left_child(self, i):
        return 2*i + 1

    def right_child(self, i):
        return 2*i + 2

    def sift_up(self, i):
        while i > 0 and self.H[self.parent(i)] > self.H[i]:
            self.H[self.parent(i)], self.H[i] = self.H[i], self.H[self.parent(i)]
            i = self.parent(i)
    
    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l < self.size and self.H[l] < self.H[min_index]:
            min_index = l

        r = self.right_child(i)
        if r < self.size and self.H[r] < self.H[min_index]:
            min_index = r
        
        if i != min_index:
            self.H[i], self.H[min_index] = self.H[min_index], self.H[i]
            self.sift_down(min_index)
    
    def insert(self, p):
        self.size += 1
        self.H.append(p)
        self.sift_up(self.size)
    
    def extract_min(self):
        result = self.H[0]
        self.H[0] = self.H[self.size]
        self.size -= 1
        self.sift_down(0)
        return result


if __name__ == "__main__":
    n_thread, n_jobs = [int(i) for i in input().split()]
    jobs = [int(i) for i in input().split()]
    time = [0 for i in range(n_jobs)]

    priority_queue = PriorityQueue()
    for i in range(n_thread):
        priority_queue.insert(i)
    
    for i in jobs:
        k = priority_queue.extract_min()
        print(k, time[k])
        time[k] += i
    
    pass











        
