class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m=len(board)
        n=len(board[0])
        def backtrack(i,j):
            if i>=m or j>=n or i<0 or j<0:
                return
            if board[i][j]==".":
                return
            board[i][j]="."
            backtrack(i+1,j)
            backtrack(i-1,j)
            backtrack(i,j+1)
            backtrack(i,j-1)
        count=0
        for i in range(m):
            for j in range(n):
                if board[i][j]=="X":
                    count+=1
                    backtrack(i,j)
        return count
        