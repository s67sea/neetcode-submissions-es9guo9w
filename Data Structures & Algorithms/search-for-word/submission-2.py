class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        combo = ""

        def dfs(curri,currj):
            nonlocal combo

            if combo == word: 
                return True
            if len(combo) > len(word):
                return False

            #from current location sample all possible neighbours
            state1 = state2 = state3 = state4 = False
            if curri>0 and (curri-1,currj) not in seen and board[curri-1][currj] == word[len(combo)]:
                #curri-1, currj
                combo += board[curri-1][currj]
                seen.add((curri-1,currj))
                state1 = dfs(curri-1,currj)
                combo = combo[:-1]
                seen.remove((curri-1,currj))
            if currj>0 and (curri,currj-1) not in seen and board[curri][currj-1] == word[len(combo)]:
                #curri,currj-1
                combo += board[curri][currj-1]
                seen.add((curri,currj-1))
                state2 = dfs(curri,currj-1)
                combo = combo[:-1]
                seen.remove((curri,currj-1))
            if curri<len(board)-1 and (curri+1,currj) not in seen and board[curri+1][currj] == word[len(combo)]:
                #curri+1,currj
                combo += board[curri+1][currj]
                seen.add((curri+1,currj))
                state3 = dfs(curri+1,currj)
                combo = combo[:-1]
                seen.remove((curri+1,currj))
            if currj<len(board[0])-1 and (curri,currj+1) not in seen and board[curri][currj+1] == word[len(combo)]:
                #curri,currj+1
                combo += board[curri][currj+1]
                seen.add((curri,currj+1))
                state4 = dfs(curri,currj+1)
                combo = combo[:-1]
                seen.remove((curri,currj+1))
            return (state1 or state2 or state3 or state4)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                seen.add((i,j))
                combo += board[i][j]
                if dfs(i,j): 
                    return True
                combo = ""
                seen.remove((i,j))
        return False
