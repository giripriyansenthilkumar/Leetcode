class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        f=Counter(words)
        words.sort(key=lambda x:(-f[x],x))
        res=[]
        i=0
        for word in words:
            if word not in res:
                res.append(word)
                i+=1
            if i==k:
                break
        return res