# DS-SEP-2025-31

1) Instructions (Setup, Run, Submit)

1.1 Prerequisites
   
python -m venv .venv

 Windows
 
.venv\Scripts\activate


1.2 Clone / Open the Project

git clone https://github.com/Deepalirole/DS-SEP-2025-31.git
cd DS-SEP-2025-31/src

1.3 Run the Benchmarks (Correctness + Timings)
python benchmark.py

What happens:

Sanity checks for Stack, Queue, BST (assertions to catch logic errors)

Timing for sorting (Bubble, Merge, Quick) on large random arrays

Timing for searching (Linear vs Binary) on large sorted arrays

2) Explanations (What’s implemented and why)
2.1 Repository Layout

   DS-SEP-2025-31/
├─ README.md

└─ src/

   ├─ stack_array.py            # Stack via dynamic array (Python list)
   
   ├─ stack_linkedlist.py     # Stack via singly-linked list
   
   ├─ queue_array.py          # Queue via circular buffer + auto-grow
   
   ├─ queue_linkedlist.py     # Queue via singly-linked list (head/tail)

   ├─ bst.py                  # Binary Search Tree + traversals + delete
   
   ├─ sorting.py              # Bubble, Merge, Quick
   
   ├─ searching.py            # Linear, Binary
   
   └─ benchmark.py            # Correctness checks + performance timings

2.2 Data Structures
Stack (LIFO)

Array-based (stack_array.py)
Uses Python list’s append/pop from the end → amortized O(1).

Linked-list (stack_linkedlist.py)
Push/Pop at head for strict O(1), independent of contiguous memory.

Public API: push(x), pop(), peek(), is_empty(), __len__()
When to use which?

Array stack is very fast & simple when capacity growth is fine.

Linked-list stack avoids resize costs, better when many unpredictable pushes/pops.

Queue (FIFO)

Array-based (queue_array.py)
Implements a circular buffer for O(1) enqueue/dequeue. Includes auto-grow when full (copies elements once while doubling capacity).

Linked-list (queue_linkedlist.py)
Tracks both head (front) and tail (back) → O(1) enqueue/dequeue without shifting.

Public API: enqueue(x), dequeue(), front(), is_empty(), __len__()
Trade-offs:

Array queue gives cache-friendly performance; occasional growth cost.

Linked-list queue gives stable O(1) ops without resizing but extra node overhead.

Binary Search Tree (bst.py)

Operations: insert, search, traversals (inorder, preorder, postorder)

Bonus: delete handles all three cases (0/1/2 children) by replacing with inorder successor when two children exist.

Note: This is an unbalanced BST. On adversarial insert order (e.g., sorted keys), height can degrade to O(n). Balanced trees (AVL/Red-Black) keep O(log n), but were not required here.

Typical uses: symbol tables, range queries (via inorder), hierarchical lookups.

2.3 Algorithms
Sorting (sorting.py)

Bubble Sort
Simple quadratic algorithm with early-exit optimization when no swaps occur in a pass. Good for teaching; poor at scale.

Merge Sort
Stable divide-and-conquer that guarantees O(n log n) time; needs O(n) extra space; excellent worst-case performance.

Quick Sort
In-place, average O(n log n) with very good constants. We randomize the pivot to reduce the chance of worst-case O(n²) on already-sorted inputs.

Searching (searching.py)

Linear Search
Scan left-to-right; useful for unsorted data or very small arrays.

Binary Search
Requires a sorted array; repeatedly halves the search space → O(log n).



3) Complexities (Big-O Time & Space)
3.1 Data Structures
   
| Structure / Operation   | Time (Best) | Time (Avg) | Time (Worst) | Space |
| ------------------------| ----------- | ---------- | ------------ | ----- |
| Stack (push/pop/peek)   | O(1)        | O(1)       | O(1)         | O(1)  |
| Queue (enqueue/dequeue) | O(1)        | O(1)       | O(1)         | O(1)  |
| BST search/insert       | O(log n)    | O(h)       | O(n)         | O(1)  |
| BST delete              | O(log n)    | O(h)       | O(n)         | O(1)  |

3.2 Algorithms


| Algorithm         | Best       | Average    | Worst      | Space     | Notes                            |
| ----------------- | ---------- | ---------- | ---------- | --------- | ---------------------------------|
| Bubble Sort   | O(n)       | O(n²)      | O(n²)      | O(1)      | Early-exit if already nearly sorted  |
| Merge Sort    | O(n log n) | O(n log n) | O(n log n) | O(n)      | Stable; predictable performance      |
| Quick Sort    | O(n log n) | O(n log n) | O(n²)      | O(log n)† | Random pivot reduces worst-case risk |
| Linear Search | O(1)       | O(n)       | O(n)       | O(1)      | No preprocessing required            |
| Binary Search | O(1)       | O(log n)   | O(log n)   | O(1)      | Requires sorted array                |


4) Edge Cases & Validation

Stack/Queue underflow: pop/dequeue/peek/front on empty raises IndexError.

Queue circular buffer growth: Automatically doubles capacity when full; amortized O(1).

BST duplicates: Ignored on insert (keeps set-like semantics).

BST delete two-children case: Uses inorder successor (smallest in right subtree).

Binary Search precondition: Array must be sorted; benchmark script ensures this.

5) Troubleshooting

python: command not found → Install Python or use py on Windows: py src\benchmark.py.

Slow benchmarks → Lower N_BUBBLE, N_DIVIDE, N_SEARCH in benchmark.py.

Import errors → Always run from inside src/ or adjust PYTHONPATH.



Author

Name: Deepali Role

Registration Number: BT/DATASTRUCTURE/SEP-2025/31




