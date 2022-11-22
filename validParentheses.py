# LeetCode problem 20 Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic1= {'(': ')', '{': '}', '[': ']'}
        for strn in s:
            if strn in dic1:
                stack.append(strn)
            elif not stack or dic1[stack[-1]]!=strn:
                return False
            else:
                stack.pop(-1)
        return not stack