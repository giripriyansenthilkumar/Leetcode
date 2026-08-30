class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        n_idx=nums.index(min(nums))
        x_idx=nums.index(max(nums))

        left=min(n_idx,x_idx)
        right=max(n_idx,x_idx)

        frwd=right+1
        back=n-left

        tot=(left+1)+(n-right)
        return min(frwd,back,tot)