# LeetCode problem 14 Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list1 = strs
        strn1 = list1[0]
        result= ''
        list2= []
        for strns in list1:
            for i,let in enumerate(strn1):
                if i < len(strns):
                    if let==strns[i]:
                        result=result+let
                    else:
                        break
            list2.append(result)
            result= ''
        return min(list2)     