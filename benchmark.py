import time, random, statistics
from stack_array import StackArray
from stack_linkedlist import StackLinkedList
from queue_array import QueueArray
from queue_linkedlist import QueueLinkedList
from bst import BinarySearchTree
from sorting import bubble_sort, merge_sort, quick_sort
from searching import linear_search, binary_search

# ---------- Tunable sizes ----------
N_BUBBLE = 10_000
N_DIVIDE = 100_000   # for merge/quick
N_SEARCH = 100_000

def timeit(fn, *args, repeat=3, **kwargs):
    times = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        out = fn(*args, **kwargs)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return out, statistics.mean(times), min(times), max(times)

def sanity_structures():
    print("== Sanity: Stack & Queue ==")
    sa = StackArray()
    sa.push(1); sa.push(2); sa.push(3)
    assert sa.peek() == 3
    assert sa.pop() == 3
    assert sa.pop() == 2
    assert sa.pop() == 1
    try:
        sa.pop()
    except IndexError:
        pass
    sl = StackLinkedList()
    for i in [10,20,30]:
        sl.push(i)
    assert sl.peek() == 30 and sl.pop() == 30

    qa = QueueArray(4)
    for i in range(5):
        qa.enqueue(i) # tests auto-grow too
    assert qa.front() == 0 and qa.dequeue() == 0 and qa.dequeue() == 1

    ql = QueueLinkedList()
    for i in [7,8,9]:
        ql.enqueue(i)
    assert ql.front() == 7 and ql.dequeue() == 7
    print("OK")

def sanity_bst():
    print("== Sanity: BST ==")
    keys = [50, 30, 70, 20, 40, 60, 80]
    bst = BinarySearchTree(keys)
    assert bst.search(60) is True
    assert bst.search(99) is False
    assert bst.inorder() == [20,30,40,50,60,70,80]
    assert bst.preorder()[0] == 50
    assert bst.postorder()[-1] == 80
    # bonus: delete
    bst.delete(70)
    assert 70 not in bst.inorder()
    print("OK")

def bench_sorting():
    print("== Sorting Benchmarks ==")
    base_small = [random.randint(0, 10_000_000) for _ in range(N_BUBBLE)]
    base_large = [random.randint(0, 10_000_000) for _ in range(N_DIVIDE)]

    # bubble on smaller size for feasibility
    _, mean_bub, min_bub, max_bub = timeit(bubble_sort, base_small, repeat=1)
    print(f"Bubble Sort n={len(base_small)}   mean={mean_bub:.3f}s")

    # merge & quick on larger size
    _, mean_merge, *_ = timeit(merge_sort, base_large, repeat=3)
    _, mean_quick, *_ = timeit(quick_sort, base_large, repeat=3)
    print(f"Merge Sort  n={len(base_large)}   mean={mean_merge:.3f}s")
    print(f"Quick Sort  n={len(base_large)}   mean={mean_quick:.3f}s")

def bench_searching():
    print("== Searching Benchmarks ==")
    arr = sorted(random.randint(0, 10_000_000) for _ in range(N_SEARCH))
    target = arr[-1]  # worst-ish case for linear
    # Linear
    _, t_lin_mean, *_ = timeit(linear_search, arr, target, repeat=1)
    # Binary
    _, t_bin_mean, *_ = timeit(binary_search, arr, target, repeat=3)
    print(f"Linear Search  n={len(arr)}   time={t_lin_mean:.6f}s")
    print(f"Binary Search  n={len(arr)}   mean={t_bin_mean:.6f}s")

if __name__ == "__main__":
    sanity_structures()
    sanity_bst()
    bench_sorting()
    bench_searching()
