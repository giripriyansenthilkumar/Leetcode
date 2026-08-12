class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        f={}
        n=len(nums)
        i=0
        res=0
        for j in range(n):
            f[nums[j]]=f.get(nums[j],0)+1
            while f[nums[j]]>k:
                f[nums[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res