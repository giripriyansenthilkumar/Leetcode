# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        # self.prev=None

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        temp=head
        n=0
        while temp:
            temp=temp.next
            n+=1
        frwd=head
        back=head
        for i in range(k-1):
            frwd=frwd.next
        for j in range(n-k):
            back=back.next
        # print(frwd.val,back.val)
        frwd.val,back.val=back.val,frwd.val
        return head
