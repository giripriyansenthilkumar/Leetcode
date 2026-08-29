class Solution:
    def simplifyPath(self, path: str) -> str:
        lst=list(map(str,path.split('/')))
        res=[]
        for i in range(len(lst)):
            if lst[i]=="":
                continue
            if lst[i]=='.':
                continue
            elif lst[i]=='..':
                if res:
                    res.pop()
            else:
                res.append('/'+lst[i])
        if not res:
            return '/'
        return ''.join(res)