class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res=set()
        n=len(tiles)
        def backtrack(curr,vis):
            for i in range(n):
                if i in vis:
                    continue
                w=curr+tiles[i]
                res.add(w)
                vis.append(i)
                backtrack(w,vis)
                vis.pop()
        backtrack("",[])
        return len(res)