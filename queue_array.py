class QueueArray:
    """Queue using circular buffer on a Python list (FIFO)."""
    def __init__(self, capacity=1024):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._data = [None] * capacity
        self._cap = capacity
        self._head = 0  # index of front
        self._size = 0

    def enqueue(self, x):
        if self._size == self._cap:
            # auto-grow: double capacity
            self._grow()
        tail = (self._head + self._size) % self._cap
        self._data[tail] = x
        self._size += 1

    def _grow(self):
        new_cap = self._cap * 2
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._cap]
        self._data = new_data
        self._cap = new_cap
        self._head = 0

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        x = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._cap
        self._size -= 1
        return x

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._data[self._head]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __repr__(self):
        items = [self._data[(self._head + i) % self._cap] for i in range(self._size)]
        return f"QueueArray({items})"
