class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        ptr = 0
        while ptr < len(s):
            #find the curr num by going up to the #
            currNum = ""
            while s[ptr] != "#":
                currNum += s[ptr]
                ptr += 1
            currNum = int(currNum)
            ptr += 1 #move it from # to the first word of the string

            #read the currNum number of chars as the next word
            currWord = ""
            for i in range(currNum):
                currWord += s[ptr]
                ptr += 1
            res.append(currWord)
        
        return res

        