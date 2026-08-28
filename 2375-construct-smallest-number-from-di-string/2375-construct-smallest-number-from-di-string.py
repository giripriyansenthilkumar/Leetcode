class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res=""
        n=len(pattern)
        def backtrack(curr,v,idx):
            nonlocal res
            if idx>n:
                return
            if str(v) in curr:
                return
            if v>9 or v<1:
                return
            if idx==n:
                curr+=str(v)
                if res=="" or int(curr)<int(res):
                    res=curr
                return
            if pattern[idx]=='I':
                for next_v in range(v+1,10):
                    backtrack(curr+str(v),next_v,idx+1)
            else:
                for next_v in range(v-1,0,-1):
                    backtrack(curr+str(v),next_v,idx+1)
        for i in range(1,10):
            backtrack("",i,0)
        return res