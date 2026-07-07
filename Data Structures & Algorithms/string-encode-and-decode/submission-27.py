class Solution:

    def encode(self, strs: List[str]) -> str:
        # [hello,world] --> 5#hello5#world
        res = ""
        for word in strs:
            res += str(len(word))+"#"+word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        searchstartindex = 0
        while searchstartindex < len(s):
            delimiter_index = s.find("#",searchstartindex)
            wordlen = int(s[searchstartindex:delimiter_index])
            word = s[delimiter_index+1:delimiter_index+wordlen+1]
            res.append(word)
            searchstartindex = delimiter_index+wordlen+1
        return res