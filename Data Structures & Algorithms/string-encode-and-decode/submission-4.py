class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for elem in strs:
            res += elem
            res += f"/#xxx#/"
        return res
    def decode(self, s: str) -> List[str]:
        return s.split("/#xxx#/")[:-1]
