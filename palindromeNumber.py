# LeetCode problem 9 Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.num = x
        num1=str(self.num)
        return (num1[::-1]==num1)