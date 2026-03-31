class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for stri in strs:
            str_as_list = str(sorted(list(stri)))
            if str_as_list not in list(mapping.keys()):
                mapping[str_as_list] = [stri]
            else:
                mapping[str_as_list].append(stri)
        ret = []
        for val in mapping.values():
            ret.append(val)
        return ret