class DynamicArray:
    def __init__(self, size=0, capacity=2):
        self.size = size
        self.capacity = capacity
        self.arr = [None] * 2

    def get(self, i):
        if i < 0 or i >= self.size:
            raise Exception('ERROR! index out of bound.')

        return self.arr[i]

    def set(self, i, val):
        if i < 0 or i >= self.size:
            raise Exception('ERROR! index out of bound.')

        self.arr[i] = val

    def pushback(self, val):
        if self.size == self.capacity:
            new_arr = [None] * (2 * self.capacity)

            for i in range(0, self.size):
                new_arr[i] = self.arr[i]

            del self.arr
            self.arr = new_arr
            self.capacity *= 2
        
        self.arr[self.size] = val
        self.size += 1

    def remove(self, i):
        if i < 0 or i >= self.size:
            raise Exception('ERROR! index out of bound.')

        for j in range(i, self.size-1):
            self.arr[j] = self.arr[j+1]
        self.arr[self.size] = None

        self.size -= 1

    def get_size(self):
        return self.size

