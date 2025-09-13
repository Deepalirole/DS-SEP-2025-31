import random

def bubble_sort(arr):
    a = arr[:]  # not in-place to keep input intact
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(L, R):
    i = j = 0
    out = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            out.append(L[i]); i += 1
        else:
            out.append(R[j]); j += 1
    out.extend(L[i:]); out.extend(R[j:])
    return out

def quick_sort(arr):
    a = arr[:]
    _qs(a, 0, len(a) - 1)
    return a

def _qs(a, lo, hi):
    if lo >= hi:
        return
    p = _partition(a, lo, hi)
    _qs(a, lo, p - 1)
    _qs(a, p + 1, hi)

def _partition(a, lo, hi):
    # randomized pivot to avoid worst-case on sorted inputs
    import random
    pivot_idx = random.randint(lo, hi)
    a[pivot_idx], a[hi] = a[hi], a[pivot_idx]
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i
