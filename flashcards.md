# Flashcards — Python Data Structures Quick Reference

## Time complexities

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| list (array) | O(1) | O(n) | O(1) append, O(n) middle | O(n) |
| tuple | O(1) | O(n) | immutable | immutable |
| str | O(1) | O(n) | immutable | immutable |
| set | — | O(1) avg | O(1) avg | O(1) avg |
| dict | O(1) | O(1) | O(1) | O(1) |
| deque | O(1) both ends | O(n) | O(1) both ends | O(1) both ends |
| heapq | — | O(n) | O(log n) | O(log n) |
| linked list | O(n) | O(n) | O(1) w/ ref | O(1) w/ ref |
| BST | O(h) | O(h) | O(h) | O(h) |
| balanced BST | O(log n) | O(log n) | O(log n) | O(log n) |

## Python idioms

```python
# Hash map
from collections import defaultdict, Counter
d = defaultdict(list)
d['key'].append(1)
c = Counter(nums)  # frequency map

# Two-pointer
left, right = 0, len(nums) - 1
while left < right:
    ...

# Sliding window
left = 0
for right, val in enumerate(nums):
    ...
    while condition:
        left += 1

# Stack
stack = []
stack.append(x)
x = stack.pop()
top = stack[-1]

# Queue
from collections import deque
q = deque()
q.append(x)      # enqueue
x = q.popleft()  # dequeue

# Heap (min-heap by default)
import heapq
heapq.heappush(h, x)
x = heapq.heappop(h)
heapq.heapify(lst)
# Max-heap: push -x

# Bisect
import bisect
i = bisect.bisect_left(a, x)   # first index >= x
i = bisect.bisect_right(a, x)  # first index > x
bisect.insort(a, x)            # sorted insert

# Linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS level order
from collections import deque
q = deque([root])
while q:
    level = []
    for _ in range(len(q)):
        node = q.popleft()
        level.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    result.append(level)

# DFS recursion
def dfs(node):
    if not node: return
    dfs(node.left)
    # process
    dfs(node.right)
```

## Common pitfalls

- `list.sort()` is in-place; `sorted()` returns new list
- `set` is unordered; use `sorted(set(x))` for deterministic output
- `dict` preserves insertion order in Python 3.7+
- `heapq` is min-heap only; negate for max-heap
- `deque.popleft()` is O(1); `list.pop(0)` is O(n)
- `defaultdict(int)` returns 0 for missing keys
- `Counter.most_common(k)` returns top-k
- `bisect` requires sorted input
- Recursion limit: `sys.setrecursionlimit(10**6)` for deep trees
