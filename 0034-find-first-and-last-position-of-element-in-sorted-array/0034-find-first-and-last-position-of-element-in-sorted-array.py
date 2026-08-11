class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=True
        res=[]
        # i=0
        while len(res)<2:
            low,high=0,len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if target>nums[mid]:
                    low=mid+1
                elif target<nums[mid]:
                    high=mid-1
                else:
                    ans=mid
                    if first:
                        high=mid-1
                    else:
                        low=mid+1
            res.append(ans)
            first=False
            # i+=1
        return res