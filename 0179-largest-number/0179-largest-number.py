from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        arr=list(map(str,nums))
        def compare(a,b):
            if a+b>b+a:
                return -1
            return 1
        arr.sort(key=cmp_to_key(compare))
        if arr[0]=="0":
            return "0"
        return "".join(arr)