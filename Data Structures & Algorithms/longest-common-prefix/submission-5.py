class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        minimum=min(len(s) for s in strs)
        for index in range(0,minimum):
            current=True
            for index2 in range(1,len(strs)):
                if strs[index2][index]!=strs[index2-1][index]:
                    return prefix
            prefix+=strs[0][index]
        return prefix