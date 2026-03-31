class Solution:

    def encode(self, strs: List[str]) -> str:
        #signature: (freq)X
        output = ""
        for word in strs:
            output += f"{len(word)}X{word}"
        return output

    def decode(self, s: str) -> List[str]:
        n = len(s)
        strings = []

        while len(s) > 0:
            index = s.find("X")
            num = int(s[:index])
            numlen = len(str(num))
            strings.append(s[numlen+1:numlen+1+num])
            s = s[numlen+1+num:]
        return strings
            


