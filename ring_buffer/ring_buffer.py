class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = list()[-self.capacity:]
        self.head = 0

    def append(self, item):
        # if full
        if len(self.storage) == self.capacity:
            # replace oldest
            self.storage[self.head] = item
        else:
            self.storage.append(item)
        # add append to head count and get remainder of capacity
        self.head = (self.head + 1) % self.capacity
                
    def get(self):
        return self.storage

if __name__ == "__main__":
    rb = RingBuffer(5)
    print(rb.storage)
    rb.append('a')
    # rb.append('b')
    # rb.append('c')
    # rb.append('d')
    # rb.append('e')
    # rb.append('f')
    # rb.append('g')
    # rb.append('h')
    rb.append('i')
    print(rb.get())# ['f', 'g', 'h', 'i', 'e'])
