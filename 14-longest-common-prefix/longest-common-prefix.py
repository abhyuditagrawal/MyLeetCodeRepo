class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs.sort()

        first, last = strs[0], strs[-1]

        for i in range (len(first)):
            if first[i] == last[i]:
                prefix = prefix + first[i]
            else:
                break
        
        return prefix