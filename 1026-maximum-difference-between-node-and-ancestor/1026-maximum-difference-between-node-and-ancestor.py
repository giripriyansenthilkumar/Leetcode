# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node,mn,mx):
            nonlocal ans
            if not node:
                return
            mn=min(mn,node.val)
            mx=max(mx,node.val)
            a=abs(node.val-mn)
            b=abs(node.val-mx)
            ans=max(ans,a,b)
            dfs(node.left,mn,mx)
            dfs(node.right,mn,mx)
        dfs(root,root.val,root.val)
        return ans
