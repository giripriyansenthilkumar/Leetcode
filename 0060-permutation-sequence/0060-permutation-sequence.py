class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s="".join(str(i) for i in range(1,n+1))
        res=["".join(p) for p in permutations(s)]
        return res[k-1]