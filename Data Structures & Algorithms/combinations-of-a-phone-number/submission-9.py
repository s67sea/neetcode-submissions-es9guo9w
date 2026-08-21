class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        #bfs approach
        if not digits: return []
        res = [""]
        for digit in digits: #for every new digit
            temp = []
            for stump in res: #for each existing prefix
                for opt in hm[digit]: #for every option of the next letter
                    temp.append(stump+opt)
            res = temp
        return res

       
       
        # dfs approach
        
        # if not digits:
        #     return []

        # res = []
        # combo = ""

        # def dfs(i):
        #     nonlocal combo

        #     if len(combo) == len(digits):
        #         res.append(combo)
        #         return
            
        #     for opt in hm[digits[i]]:
        #         combo += opt
        #         dfs(i+1)
        #         combo = combo[:-1]
            
        # dfs(0)
        # return res