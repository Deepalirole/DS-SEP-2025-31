class _Node:
    __slots__ = ("val", "next")
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class QueueLinkedList:
    """Queue using singly-linked list with head (front) and tail (back)."""
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, x):
        node = _Node(x)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        x = self._head.val
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return x

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._head.val

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __repr__(self):
        vals, cur = [], self._head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return f"QueueLinkedList(front-> {vals} <-back)"
