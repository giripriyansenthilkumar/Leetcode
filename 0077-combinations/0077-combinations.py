class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(curr,v=1):
            nonlocal res
            if len(curr)==k:
                res.append(curr[:])
                return
            for i in range(v,n+1):
                backtrack(curr+[i],i+1)
            return
        backtrack([])
        return res