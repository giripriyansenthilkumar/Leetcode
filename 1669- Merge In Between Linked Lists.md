# Intuition

To insert `list2` into `list1`, we first remove all nodes from index `a` to `b` in `list1`. Once this segment is removed, we connect the beginning of `list2` to the node before index `a` and connect the end of `list2` to the node after index `b`.

This allows us to merge the two linked lists without creating any new nodes, simply by updating the existing pointers.

# Approach

1. Traverse `list1` to find the node just before index `a` (`prev`).
2. Continue traversing to find the node immediately after index `b` (`after`).
3. Traverse `list2` to find its last node (`tail`).
4. Connect:
   - `prev.next` to the head of `list2`.
   - `tail.next` to `after`.
5. Return the head of `list1`.

# Complexity

- **Time Complexity:** `O(n + m)`
  - `O(n)` to locate the required positions in `list1`.
  - `O(m)` to find the last node of `list2`.

- **Space Complexity:** `O(1)`
  - Only a few pointer variables are used.

# Code

```python []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        # Find the node just before index a
        prev = list1
        for _ in range(a - 1):
            prev = prev.next

        # Find the node just after index b
        after = prev.next
        for _ in range(b - a + 1):
            after = after.next

        # Find the last node of list2
        tail = list2
        while tail.next:
            tail = tail.next

        # Insert list2 between prev and after
        prev.next = list2
        tail.next = after

        return list1
```