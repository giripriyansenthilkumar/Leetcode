class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        def backtrack(i,j,k):
            if i<0 or i>n-1 or j<0 or j>m-1:
                return False
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            temp=board[i][j]
            board[i][j]="#"
            if (backtrack(i+1,j,k+1) or backtrack(i-1,j,k+1) or backtrack(i,j+1,k+1) or backtrack(i,j-1,k+1)):
                return True
            board[i][j]=temp
            return False
            
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False