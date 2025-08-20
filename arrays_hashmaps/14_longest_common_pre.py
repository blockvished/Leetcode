class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            for strrr in strs:
                if i == len(strrr) or strrr[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result