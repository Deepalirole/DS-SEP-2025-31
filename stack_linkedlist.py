class _Node:
    __slots__ = ("val", "next")
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class StackLinkedList:
    """Stack using singly-linked list head as top (LIFO)."""
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, x):
        self._head = _Node(x, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        x = self._head.val
        self._head = self._head.next
        self._size -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._head.val

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __repr__(self):
        vals = []
        cur = self._head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return f"StackLinkedList(top-> {vals})"
