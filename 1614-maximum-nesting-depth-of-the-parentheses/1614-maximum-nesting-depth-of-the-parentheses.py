class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot=[]
        v=0
        for i in range(len(s)):
            if s[i]=='(':
                v+=1
            elif s[i]==')':
                tot.append(v)
                v-=1
        if len(tot)==0:
            return 0
        return max(tot)