class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]

        def backtrack(lst,idx):
            nonlocal res
            # print(lst)
            if len(lst)>k:
                return
            if sum(lst)>n:
                return
            if len(lst)==k and sum(lst)==n:
                res.append(lst)
                return
            for i in range(idx+1,10):
                if len(lst)<k:
                    backtrack(lst+[i],i)
            return
        for i in range(1,10):
            backtrack([i],i)
        return res