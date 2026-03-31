class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for elem in strs:
            res += f"${len(elem)}${elem}"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i]=="$":
                i+=1
                num = ""
                while s[i]!="$":
                    num += s[i]
                    i+=1
                i+=1
                num = int(num)
                newWord = ""
                for j in range(num):
                    newWord += s[i]
                    i+=1
                res.append(newWord)
        return res
        